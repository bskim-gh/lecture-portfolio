"""
미니 매출 대시보드 실습
파일 업로드, 필터링, KPI 표시, 차트 생성을 종합한 실습 프로젝트
"""
import pandas as pd
import numpy as np
import streamlit as st

st.title("미니 매출 대시보드")

# ==================== 데이터 업로드 ====================
uploaded = st.file_uploader("매출 CSV 업로드", type=["csv"])

if uploaded:
    # CSV 파일 읽기
    df = pd.read_csv(uploaded)
    # 매출 계산 (수량 x 단가)
    df['revenue'] = df['units'] * df["unit_price"]
    st.write("데이터 미리보기:", df.head())

    # ==================== 필터 ====================
    all_regions = df['region'].unique().tolist()
    region = st.sidebar.selectbox("지역", ["전체"] + all_regions)
    if region != "전체":
        df = df[df["region"]== region]
   
    # ==================== KPI (핵심 성과 지표) ====================
    st.metric("총 매출:", f"${df['revenue'].sum():,.2f}")
    st.metric("주문 수",len(df))

    # ==================== 차트: 일별 매출 추이 ====================
    by_day = df.groupby("date", as_index=False)['revenue'].sum().sort_values('date')
    st.line_chart(by_day, x="date",y="revenue")