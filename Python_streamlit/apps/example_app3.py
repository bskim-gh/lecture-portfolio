"""
데이터 시각화 예제
데이터프레임과 차트를 표시하는 다양한 방법
"""
import streamlit as st
import pandas as pd

# 샘플 데이터 생성
df = pd.DataFrame({
    "month": ["1월","2월","3월"], 
    "revenue":[12000, 14500, 13200]
})

# ==================== 데이터프레임 표시 ====================
st.dataframe(df, use_container_width=True)

# ==================== 빠른 차트 (Quick Charts) ====================
# Streamlit 내장 차트 함수 사용
st.line_chart(df, x="month", y="revenue")

# ==================== Altair 차트 ====================
# 더 세밀한 커스터마이징이 가능한 Altair 라이브러리
import altair as alt
chart = alt.Chart(df).mark_bar().encode(x="month", y="revenue")
st.altair_chart(chart, use_container_width=True)
