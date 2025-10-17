"""
파일 업로드 예제
CSV 파일을 업로드하고 데이터를 표시하는 기능
"""
import streamlit as st
import pandas as pd

# ==================== 파일 업로더 ====================
# CSV 파일만 업로드 가능하도록 제한
uploaded = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded:
    # 업로드된 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded)
    st.success(f"{len(df):,}개의 행이 로드되었습니다")
    
    # 상위 5개 행 미리보기
    st.dataframe(df.head())

    # 상위 20개 행 미리보기
    st.dataframe(df.head(20))
