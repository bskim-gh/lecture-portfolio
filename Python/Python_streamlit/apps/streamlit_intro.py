"""
Streamlit 입문 - 기본 위젯과 인터랙티브 기능 학습
"""
import streamlit as st

# ==================== 첫 앱 만들기 실습 ====================
name = "여기에 이름을 입력하세요"
st.title(f"안녕하세요 {name}!")
st.header("이것은 헤더입니다")
st.subheader("이것은 서브헤더입니다")
st.write("그리고 이것은 일반 텍스트 블록입니다.")

# ==================== 위젯과 인터랙티브 기능 ====================

# 예제 1: 버튼
if st.button("클릭하세요!"):
    st.write("버튼이 클릭되었습니다")

# 예제 2: 텍스트 입력 + 버튼
name = st.text_input("이름을 입력하세요:")
if st.button("인사하기"):
    st.write(f"안녕하세요, {name}님")

# 예제 3: 슬라이더
age = st.slider("나이를 선택하세요:", 0, 100, 25)
st.write(f"당신은 {age}살입니다.")

# 예제 4: 선택 박스
color = st.selectbox("색상을 선택하세요:", ["빨강","초록","파랑"])
st.write(f"선택한 색상: {color}")

