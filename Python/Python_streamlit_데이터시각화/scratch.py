"""
연습용 스크래치 파일
인터랙티브 매출 대시보드 - 레이아웃 예제
실제 데이터 파일(orders_large.csv)을 사용한 대시보드 구현
"""
import streamlit as st  # Streamlit 라이브러리 가져오기
import pandas as pd

# ==================== 데이터 로드 및 전처리 ====================
df = pd.read_csv("data/orders_large.csv")
df["date"] = pd.to_datetime(df["date"])  # 날짜 형식으로 변환
df["revenue"] = df["units"] * df["unit_price"]  # 매출 계산

# 필터 옵션 준비
regions = ["전체"] + sorted(df["region"].unique().tolist())
products = ["전체"] + sorted(df["product"].unique().tolist())

# ==================== 페이지 타이틀 ====================
st.title("레이아웃 예제")

# ==================== 사이드바 필터 ====================
st.sidebar.header("필터")
region = st.sidebar.selectbox("지역 선택", regions)
product = st.sidebar.selectbox("제품 선택", products)
date_range = st.sidebar.date_input("날짜 범위", (df["date"].min(), df["date"].max()))

# ==================== 데이터 필터링 ====================
filtered = df.copy()

if region != "전체":
    filtered = filtered[filtered["region"] == region]
if product != "전체":
    filtered = filtered[filtered["product"] == product]

# 날짜 범위 필터 적용
filtered = filtered[filtered["date"].between(
    pd.to_datetime(date_range[0]), 
    pd.to_datetime(date_range[1])
)]

# ==================== KPI 계산 ====================
total_revenue = filtered["revenue"].sum()  # 총 매출
total_units = int(filtered["units"].sum())  # 총 판매 수량
orders = len(filtered)  # 주문 수
avg_order_value = total_revenue / orders  # 평균 주문 금액

# ==================== KPI 메트릭 표시 ====================
c1, c2, c3 = st.columns(3)
c1.metric("총 매출", f"${total_revenue:,.2f}")
c2.metric("판매 수량", f"{total_units:,}")
c3.metric("평균 주문 금액", f"${avg_order_value:,.2f}")

# ==================== 탭 레이아웃 ====================
tab1, tab2 = st.tabs(["요약", "상세"])
tab1.write("주요 결과 개요입니다.")
tab2.write("상세 데이터 분석 내용이 여기에 표시됩니다.")

st.title("인터랙티브 매출 대시보드")



