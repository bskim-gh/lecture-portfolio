"""
레이아웃과 조직화 실습
사이드바, 컬럼, 메트릭, 차트를 활용한 레이아웃 구성 예제
"""
import streamlit as st
import pandas as pd
import numpy as np

# ==================== 예제 1: 사이드바 ====================
st.title("나의 대시보드")
option = st.sidebar.selectbox("보기 선택", ["개요", "상세"])

st.write("선택한 보기:", option)

# ==================== 예제 2: 컬럼 ====================

col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

# ==================== 예제 3: 메트릭 ====================

col1, col2 = st.columns(2)

with col1:
    st.metric("매출","200K")

with col2:
    st.metric("이익","50k")

# ==================== 예제 4: 컬럼 차트 ====================

# 샘플 차트 데이터 생성
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns = ["제품 A","제품 B","제품 C"]
)

# 동일한 너비의 2개 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    st.header("막대 차트")
    st.bar_chart(chart_data)

with col2:
    st.header("선 차트")
    st.line_chart(chart_data)