"""
매출 스냅샷 앱 - 스캐폴드 버전
학생들이 TODO 부분을 채워서 완성하는 실습용 파일
"""
# app.py
import pandas as pd
import streamlit as st

# ==================== 페이지 설정 ====================
st.set_page_config(page_title="Sales Snapshot", layout="wide")
st.title("매출 스냅샷")
st.caption("CSV를 업로드하고, 날짜와 지역으로 필터링하여 KPI와 추세를 탐색하세요.")

# ==================== 1) 파일 업로드 ====================
uploaded = st.file_uploader("주문 CSV 업로드", type=["csv"])

def prepare(df: pd.DataFrame) -> pd.DataFrame:
    """
    CSV 데이터를 전처리하는 함수
    - 컬럼명 정규화
    - 필수 컬럼 검증
    - 데이터 타입 변환
    - 매출 계산
    """
    # 컬럼명 정규화 (소문자 변환 및 공백 제거)
    df.columns = [c.strip().lower() for c in df.columns]
    
    # 필수 컬럼 검증
    required = {"date", "region", "product", "units", "unit_price"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"필수 컬럼 누락: {', '.join(sorted(missing))}")
    
    # 데이터 타입 변환
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["units"] = pd.to_numeric(df["units"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    
    # 결측치 제거
    df = df.dropna(subset=["date", "region", "product", "units", "unit_price"])
    
    # 매출 계산
    df["revenue"] = df["units"] * df["unit_price"]
    return df

if uploaded:
    try:
        df = prepare(pd.read_csv(uploaded))
        st.success("CSV 로드 완료")
    except Exception as e:
        st.error(f"CSV를 읽을 수 없습니다: {e}")
        st.stop()
else:
    st.info("시작하려면 CSV를 업로드하세요. 아래에서 필요한 컬럼을 확인하세요.")
    with st.expander("필요한 컬럼"):
        st.code("date, region, product, units, unit_price", language="text")
    st.stop()

# ==================== 2) 필터 (사이드바) ====================
st.sidebar.header("필터")

# 날짜 범위
dmin, dmax = df["date"].min().date(), df["date"].max().date()
date_range = st.sidebar.date_input("날짜 범위", (dmin, dmax), min_value=dmin, max_value=dmax)
if isinstance(date_range, tuple):
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
else:
    start = end = pd.to_datetime(date_range)

# 지역
regions = ["전체"] + sorted(df["region"].dropna().unique().tolist())
region = st.sidebar.selectbox("지역", regions, index=0)

# 필터 적용
mask = df["date"].between(start, end)
if region != "전체":
    mask &= df["region"].eq(region)

f = df.loc[mask].copy()

if f.empty:
    st.warning("필터와 일치하는 행이 없습니다. 날짜 범위를 확장하거나 다른 지역을 선택해보세요.")
    st.stop()

# ==================== 3) KPI ====================
total_revenue = f["revenue"].sum()  # 총 매출
units_sold = int(f["units"].sum())  # 판매 수량
orders = len(f)  # 주문 수 (또는 order_id가 있으면 f["order_id"].nunique())
aov = (total_revenue / orders) if orders else 0.0  # 평균 주문 금액

c1, c2, c3, c4 = st.columns(4)
c1.metric("총 매출", f"${total_revenue:,.2f}")
c2.metric("판매 수량", f"{units_sold:,}")
c3.metric("주문 수", f"{orders:,}")
c4.metric("평균 주문 금액", f"${aov:,.2f}")

st.divider()

# ==================== 4) 차트 ====================
st.subheader("시간별 매출 추이")
by_day = f.groupby("date", as_index=False)["revenue"].sum().sort_values("date")
st.line_chart(by_day, x="date", y="revenue", height=260)

# ==================== 5) 테이블 ====================
st.subheader("필터링된 처음 50개 행")
st.dataframe(f.head(50), use_container_width=True)
