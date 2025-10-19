"""
레이아웃 데모 앱
사이드바, 컬럼, 탭 등의 레이아웃 기능을 보여주는 예제
"""
import streamlit as st

st.title("레이아웃 데모")

# ==================== 사이드바 ====================
with st.sidebar:
    st.header("컨트롤")
    region = st.selectbox("지역", ["북부", "남부", "동부", "서부"])
    show_raw = st.checkbox("원본 데이터 표시")

# ==================== 컬럼 ====================
# 1:2 비율로 두 개의 컬럼 생성
left, right = st.columns([1,2])
left.metric("활성 사용자", 1243, delta=+35)
right.info(f"선택한 지역: {region}")

# ==================== 탭 ====================
tab1, tab2 = st.tabs(["요약", "상세"])
with tab1:
    st.write("KPI, 차트 등...")
with tab2:
    st.write("테이블, 설명 등...")
