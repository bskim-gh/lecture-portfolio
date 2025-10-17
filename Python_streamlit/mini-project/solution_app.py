"""
매출 스냅샷 앱 - 솔루션 버전
추가 도전 과제를 포함한 완성된 버전
- 다중 필터 (날짜, 지역, 제품)
- KPI 델타 (이전 기간 대비)
- 상위 제품 차트
- CSV 다운로드 기능
"""
# app.py — Solution Branch
import io
import pandas as pd
import numpy as np
import streamlit as st
from datetime import timedelta

# ==================== 페이지 설정 ====================
st.set_page_config(page_title="Sales Snapshot — Solution", layout="wide")
st.title("매출 스냅샷 — 솔루션")
st.caption("CSV를 업로드하고, 날짜/지역/제품으로 필터링하여 KPI, 추세, 상위 제품을 탐색하세요. 추가 도전 과제 포함.")

# =========================
# 1) 파일 업로드 및 전처리
# =========================

uploaded = st.file_uploader("주문 CSV 업로드", type=["csv"])

REQUIRED_COLS = {"date", "region", "product", "units", "unit_price"}

@st.cache_data(show_spinner=False)
def prepare(raw_csv) -> pd.DataFrame:
    """
    CSV 입력을 읽어서 정제된 DataFrame을 반환합니다:
    - 정규화된 컬럼명
    - 파싱된 타입 (날짜, 숫자)
    - 계산된 'revenue' 컬럼
    필수 컬럼: date, region, product, units, unit_price
    """
    if isinstance(raw_csv, (io.BytesIO, io.StringIO)):
        df = pd.read_csv(raw_csv)
    else:
        df = pd.read_csv(raw_csv)

    # 헤더 정규화
    df.columns = [c.strip().lower() for c in df.columns]
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"필수 컬럼 누락: {', '.join(sorted(missing))}")

    # 타입 변환
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["units"] = pd.to_numeric(df["units"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # 불완전한 행 제거
    df = df.dropna(subset=["date", "region", "product", "units", "unit_price"])

    # 매출 계산
    df["revenue"] = df["units"] * df["unit_price"]

    # 예측 가능한 동작을 위해 정렬
    return df.sort_values("date").reset_index(drop=True)

if not uploaded:
    st.info("시작하려면 CSV를 업로드하세요. 필수 컬럼 (대소문자 무관): "
            "`date, region, product, units, unit_price`. 선택 사항: `order_id`.")
    with st.expander("예제 행"):
        st.code("""order_id,date,region,product,units,unit_price
10001,2024-01-03,북부,위젯,3,14.50
10002,2024-01-03,서부,가젯,2,29.00
10003,2024-01-04,남부,장치,5,9.99
""", language="csv")
    st.stop()

try:
    df = prepare(uploaded)
    st.success("CSV 로드 완료")
except Exception as e:
    st.error(f"CSV를 읽을 수 없습니다: {e}")
    st.stop()

# =========================
# 2) 사이드바 필터
# =========================

st.sidebar.header("필터")

# 날짜 범위는 데이터의 최소/최대값으로 기본 설정
dmin, dmax = df["date"].min().date(), df["date"].max().date()
date_range = st.sidebar.date_input(
    "날짜 범위",
    (dmin, dmax),
    min_value=dmin,
    max_value=dmax
)
if isinstance(date_range, tuple):
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start_date = end_date = pd.to_datetime(date_range)

# 지역 다중 선택 (기본값: 전체)
all_regions = sorted(df["region"].dropna().unique().tolist())
regions = st.sidebar.multiselect("지역", options=all_regions, default=all_regions)

# 제품 다중 선택 (기본값: 전체) — 추가 도전 과제
all_products = sorted(df["product"].dropna().unique().tolist())
products = st.sidebar.multiselect("제품", options=all_products, default=all_products)

# 필터 적용
mask = (
    df["date"].between(start_date, end_date)
    & df["region"].isin(regions)
    & df["product"].isin(products)
)
f = df.loc[mask].copy()

if f.empty:
    st.warning("필터와 일치하는 행이 없습니다. 날짜 범위를 확장하거나 더 많은 지역/제품을 선택해보세요.")
    st.stop()

# =========================
# 3) KPI (델타 포함)
# =========================

# 현재 기간 통계
total_revenue = float(f["revenue"].sum())
units_sold = int(f["units"].sum())
orders = f["order_id"].nunique() if "order_id" in f.columns else len(f)
aov = (total_revenue / orders) if orders else 0.0

# 이전 기간: start_date 직전의 동일 길이 기간 — 추가 도전 과제
period_days = max(1, (end_date.date() - start_date.date()).days + 1)
prev_start = start_date - timedelta(days=period_days)
prev_end = start_date - timedelta(days=1)

prev_mask = (
    df["date"].between(prev_start, prev_end)
    & df["region"].isin(regions)
    & df["product"].isin(products)
)
prev = df.loc[prev_mask]

prev_revenue = float(prev["revenue"].sum()) if not prev.empty else 0.0
prev_units = int(prev["units"].sum()) if not prev.empty else 0
prev_orders = (prev["order_id"].nunique() if "order_id" in df.columns else len(prev)) if not prev.empty else 0
prev_aov = (prev_revenue / prev_orders) if prev_orders else 0.0

# 델타 (변화량)
rev_delta = total_revenue - prev_revenue
units_delta = units_sold - prev_units
orders_delta = orders - prev_orders
aov_delta = aov - prev_aov

c1, c2, c3, c4 = st.columns(4)
c1.metric("총 매출", f"${total_revenue:,.2f}", delta=f"${rev_delta:,.2f}")
c2.metric("판매 수량", f"{units_sold:,}", delta=f"{units_delta:,}")
c3.metric("주문 수", f"{orders:,}", delta=f"{orders_delta:,}")
c4.metric("평균 주문 금액", f"${aov:,.2f}", delta=f"${aov_delta:,.2f}")

st.divider()

# =========================
# 4) 시각화
# =========================

left, right = st.columns((2, 1), gap="large")

with left:
    st.subheader("시간별 매출 추이")
    by_day = (
        f.groupby("date", as_index=False)["revenue"]
         .sum()
         .sort_values("date")
    )
    st.line_chart(by_day, x="date", y="revenue", height=300)

with right:
    st.subheader("매출 상위 제품 (Top 5)")
    top_prod = (
        f.groupby("product", as_index=False)["revenue"]
         .sum()
         .sort_values("revenue", ascending=False)
         .head(5)
    )
    if top_prod.empty:
        st.info("필터 적용 후 제품 데이터가 없습니다.")
    else:
        st.bar_chart(top_prod, x="product", y="revenue", height=300)

st.divider()

# =========================
# 5) 테이블 & 다운로드
# =========================

tab1, tab2 = st.tabs(["필터링된 데이터", "지역/제품 요약"])

with tab1:
    st.write("필터링된 처음 100개 행")
    st.dataframe(f.head(100), use_container_width=True)

    # 필터링된 CSV 다운로드 — 추가 도전 과제
    st.download_button(
        label="필터링된 데이터를 CSV로 다운로드",
        data=f.to_csv(index=False).encode("utf-8"),
        file_name="filtered_orders.csv",
        mime="text/csv",
        use_container_width=True
    )

with tab2:
    # 지역별 요약
    reg = (
        f.groupby("region", as_index=False)
         .agg(revenue=("revenue", "sum"), units=("units", "sum"))
         .sort_values("revenue", ascending=False)
    )
    st.write("지역별")
    st.dataframe(reg, use_container_width=True)

    # 제품별 요약
    prod = (
        f.groupby("product", as_index=False)
         .agg(revenue=("revenue", "sum"), units=("units", "sum"))
         .sort_values("revenue", ascending=False)
    )
    st.write("제품별")
    st.dataframe(prod, use_container_width=True)

# =========================
# 6) 참고 사항
# =========================

with st.expander("참고 사항 & 팁"):
    st.markdown("""
- 필수 컬럼: **date, region, product, units, unit_price**. 선택 사항: **order_id**.
- KPI 델타는 동일한 길이의 직전 기간과 비교합니다.
- 사이드바를 사용하여 날짜, 지역, 제품으로 좁힐 수 있습니다.
- 필터가 변경되면 차트와 메트릭이 즉시 업데이트됩니다.
""")
