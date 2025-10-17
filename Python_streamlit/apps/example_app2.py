"""
폼과 입력 위젯 예제
고객 정보 입력과 주문 폼을 보여주는 예제
"""
import streamlit as st

# ==================== 기본 입력 위젯 ====================
name = st.text_input("고객명", placeholder="홍길동")
qty  = st.number_input("수량", min_value=1, value=10)
price = st.number_input("단가 ($)", min_value=0.0, value=19.99)
confirm = st.button("장바구니에 추가")

if confirm:
    st.success(f"{name}님의 주문: {qty}개 x ${price:.2f} 추가됨")

# ==================== 폼 (Form) ====================
# 폼을 사용하면 여러 입력을 한 번에 제출할 수 있습니다
with st.form("order_form"):
    sku = st.text_input("상품 코드 (SKU)")
    qty = st.number_input("수량", 1, 100, 5)
    submitted = st.form_submit_button("주문 제출")
    
if submitted:
    st.success(f"주문 완료: {sku} x {qty}개")
