"""
비즈니스 KPI 대시보드
주문 데이터를 분석하여 핵심 성과 지표를 시각화하는 종합 예제
"""
# app.py
import streamlit as st
import pandas as pd

# ==================== 페이지 설정 ====================
st.set_page_config(page_title="KPI Dashboard", layout="wide")
st.title("비즈니스 KPI 대시보드")

# ==================== 파일 업로드 ====================
uploaded = st.file_uploader("주문 CSV 파일 업로드", type=["csv"])

# ==================== 데이터 로드 함수 ====================
# @st.cache_data 데코레이터로 데이터를 캐싱하여 성능 향상
@st.cache_data
def load_data(file):
    """CSV 파일을 읽고 매출 계산"""
    df = pd.read_csv(file, parse_dates=["date"])
    df["revenue"] = df["units"] * df["unit_price"]  # 매출 = 수량 x 단가
    return df

if uploaded:
    # 데이터 로드
    df = load_data(uploaded)
    
    # ==================== 사이드바 필터 ====================
    with st.sidebar:
        st.header("필터")
        
        # 지역 선택
        regions = ["전체"] + sorted(df["region"].dropna().unique().tolist())
        region = st.selectbox("지역", regions)
        
        # 날짜 범위 선택
        date_min, date_max = df["date"].min(), df["date"].max()
        date_range = st.date_input("날짜 범위", (date_min, date_max))

    # ==================== 데이터 필터링 ====================
    d1, d2 = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    f = (df["date"].between(d1, d2))
    if region != "전체":
        f &= (df["region"] == region)
    view = df.loc[f].copy()

    # ==================== KPI 계산 ====================
    total_rev = view["revenue"].sum()  # 총 매출
    orders = view["order_id"].nunique()  # 주문 수
    avg_order = total_rev / max(orders, 1)  # 평균 주문 금액

    # KPI 메트릭 표시 (3개 컬럼)
    c1, c2, c3 = st.columns(3)
    c1.metric("총 매출", f"${total_rev:,.0f}")
    c2.metric("주문 수", f"{orders:,}")
    c3.metric("평균 주문 금액", f"${avg_order:,.2f}")

    # ==================== 차트 ====================
    # 시간별 매출 추이
    rev_by_date = view.groupby(view["date"].dt.to_period("D"))["revenue"].sum().reset_index()
    rev_by_date["date"] = rev_by_date["date"].dt.to_timestamp()
    st.subheader("시간별 매출 추이")
    st.line_chart(rev_by_date, x="date", y="revenue")

    # 제품별 매출
    st.subheader("제품별 매출")
    rev_by_prod = view.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    st.bar_chart(rev_by_prod, x="product", y="revenue")

    # ==================== 상세 데이터 ====================
    with st.expander("샘플 데이터 보기"):
        st.dataframe(view.head(50), use_container_width=True)
else:
    st.info("CSV 파일을 업로드하세요. 필요한 컬럼: order_id, date, region, product, units, unit_price")
