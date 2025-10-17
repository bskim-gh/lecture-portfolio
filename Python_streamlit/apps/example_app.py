"""
Streamlit 기본 예제 앱
간단한 할인 계산기 대시보드
"""
import streamlit as st
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="Hello Streamlit", page_icon="📊", layout="wide")

st.title("안녕하세요, Streamlit!")
st.write("이것은 간단한 인터랙티브 앱입니다.")

# 위젯: 슬라이더로 할인율 선택
discount = st.slider("할인율 (%)", 0, 50, 10)

# 데이터: 샘플 가격 데이터 생성
df = pd.DataFrame({
    "price": np.random.randint(50, 200, 20)
})
# 할인 후 가격 계산
df["price_after_discount"] = df["price"] * (1 - discount/100)

st.subheader("샘플 데이터")
st.dataframe(df)

# 할인 후 가격을 막대 차트로 표시
st.bar_chart(df.set_index(df.index)["price_after_discount"])
