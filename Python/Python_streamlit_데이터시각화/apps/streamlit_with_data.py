"""
데이터 다루기 실습
테이블, 차트, 파일 업로드 등 데이터 표시 방법을 배우는 예제
"""
import streamlit as st
import pandas as pd
import numpy as np

# ==================== 예제 1: 테이블 ====================
df = pd.DataFrame({
    "제품":["A","B","C"],
    "매출":[100,200, 300]
})

st.table(df)

# ==================== 예제 2: 선 차트 ====================
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ["제품 A","제품 B","제품 C"]
)

st.line_chart(chart_data)

# ==================== 예제 3: 막대 차트 ====================
st.bar_chart(df.set_index("제품"))

# ==================== 예제 4: 파일 업로드 ====================
uploaded = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded:
    data = pd.read_csv(uploaded)
    st.write("데이터 미리보기", data.head())