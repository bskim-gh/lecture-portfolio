# Streamlit으로 인터랙티브 대시보드 만들기

Python으로 웹 기반 데이터 대시보드를 쉽게 만들 수 있는 Streamlit 라이브러리 교안입니다.

---

## 📚 목차

1. [Streamlit 소개](#1-streamlit-소개)
2. [시작하기](#2-시작하기)
3. [위젯과 인터랙티브 기능](#3-위젯과-인터랙티브-기능)
4. [데이터 표시하기](#4-데이터-표시하기)
5. [파일 업로드와 필터링](#5-파일-업로드와-필터링)
6. [레이아웃과 구조](#6-레이아웃과-구조)
7. [미니 프로젝트](#7-미니-프로젝트)
8. [마무리](#8-마무리)

---

## 1. Streamlit 소개

### Streamlit이란?

Streamlit은 Python으로 데이터 앱을 빠르게 만들 수 있는 오픈소스 프레임워크입니다.

### 왜 Streamlit을 사용하나요?

- **간단함**: HTML, CSS, JavaScript 없이 순수 Python만으로 웹 앱 제작
- **빠른 프로토타이핑**: 몇 분 만에 대시보드 구축 가능
- **데이터 중심**: pandas, numpy, matplotlib 등과 완벽한 통합

### 실제 사용 사례

- 데이터 대시보드
- 내부 도구
- 머신러닝 모델 데모
- 데이터 분석 리포트

### 설치 및 첫 실행

```bash
# Streamlit 설치
pip install streamlit

# 데모 앱 실행
streamlit hello
```

---

## 2. 시작하기

### Streamlit 워크플로우

```bash
# 앱 실행 명령어
streamlit run app.py
```

### 첫 번째 앱 만들기

**파일: `apps/streamlit_intro.py`**

```python
import streamlit as st

st.title("나의 첫 Streamlit 앱")
st.write("안녕하세요! 이것은 간단한 인터랙티브 웹 앱입니다.")
```

### 실습

1. 위 코드를 복사하여 `my_first_app.py` 파일을 만드세요
2. 터미널에서 `streamlit run my_first_app.py` 실행
3. 브라우저가 자동으로 열리고 앱이 표시됩니다

---

## 3. 위젯과 인터랙티브 기능

### 주요 입력 위젯

| 위젯 | 설명 | 코드 예제 |
|------|------|----------|
| Button | 클릭 버튼 | `st.button("클릭")` |
| Text Input | 텍스트 입력 | `st.text_input("이름")` |
| Slider | 슬라이더 | `st.slider("나이", 0, 100)` |
| Selectbox | 선택 박스 | `st.selectbox("색상", ["빨강","파랑"])` |
| Checkbox | 체크박스 | `st.checkbox("동의")` |
| Radio | 라디오 버튼 | `st.radio("선택", ["A","B"])` |
| Number Input | 숫자 입력 | `st.number_input("수량", 1, 100)` |

### 실습 예제

**파일: `apps/streamlit_intro.py`** (주석 해제하여 실행)

```python
import streamlit as st

# 텍스트 입력
name = st.text_input("이름을 입력하세요:")

# 슬라이더
age = st.slider("나이를 선택하세요:", 0, 100, 25)

# 버튼
if st.button("제출"):
    st.write(f"안녕하세요, {name}님! 당신은 {age}살입니다.")
```

### 실습 과제

- 좋아하는 색상을 선택하는 드롭다운 추가하기
- 선택한 색상을 화면에 표시하기

**참고 파일**: 
- `apps/example_app2.py` - 폼과 입력 위젯 예제

---

## 4. 데이터 표시하기

### 텍스트와 테이블

```python
import streamlit as st
import pandas as pd

# 데이터프레임 생성
df = pd.DataFrame({
    "제품": ["A", "B", "C"],
    "매출": [100, 200, 150]
})

# 테이블 표시
st.table(df)

# 인터랙티브 데이터프레임
st.dataframe(df)
```

### 차트 그리기

#### 빠른 차트 (Quick Charts)

```python
import numpy as np

# 샘플 데이터
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["제품 A", "제품 B", "제품 C"]
)

# 선 차트
st.line_chart(chart_data)

# 막대 차트
st.bar_chart(chart_data)

# 영역 차트
st.area_chart(chart_data)
```

#### 고급 차트 (Altair, Plotly)

```python
import altair as alt

chart = alt.Chart(df).mark_bar().encode(
    x="제품",
    y="매출"
)
st.altair_chart(chart, use_container_width=True)
```

### 실습 과제

- 자신만의 데이터프레임을 만들어보세요
- 다른 차트 타입(막대, 영역)을 시도해보세요

**참고 파일**: 
- `apps/streamlit_with_data.py` - 데이터 표시 예제
- `apps/example_app3.py` - 차트 예제

---

## 5. 파일 업로드와 필터링

### 파일 업로더

```python
import streamlit as st
import pandas as pd

# CSV 파일 업로드
uploaded = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded:
    # 데이터 읽기
    data = pd.read_csv(uploaded)
    st.write("데이터 미리보기")
    st.dataframe(data.head())
    
    # 컬럼 선택 필터
    column = st.selectbox("컬럼 선택", data.columns)
    st.write(data[column])
```

### 데이터 필터링

```python
# 지역 필터
regions = ["전체"] + list(data["region"].unique())
selected_region = st.selectbox("지역 선택", regions)

if selected_region != "전체":
    filtered_data = data[data["region"] == selected_region]
else:
    filtered_data = data

st.dataframe(filtered_data)
```

### 실습 과제

- 자신의 CSV 파일을 업로드해보세요
- 컬럼을 선택하여 데이터를 필터링해보세요

**참고 파일**: 
- `apps/example_app4.py` - 파일 업로드 예제

---

## 6. 레이아웃과 구조

### 사이드바

```python
import streamlit as st

# 사이드바에 위젯 추가
with st.sidebar:
    st.header("필터")
    region = st.selectbox("지역", ["북부", "남부", "동부", "서부"])
    show_data = st.checkbox("데이터 표시")
```

### 컬럼

```python
# 2개의 컬럼 생성
col1, col2 = st.columns(2)

col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

# 비율 지정 (1:2)
left, right = st.columns([1, 2])
```

### 메트릭

```python
# KPI 메트릭 표시
col1, col2, col3 = st.columns(3)

col1.metric("총 매출", "₩200,000", delta="+15%")
col2.metric("주문 수", "450", delta="+10")
col3.metric("평균 주문 금액", "₩50,000", delta="-5%")
```

### 탭

```python
# 탭 생성
tab1, tab2, tab3 = st.tabs(["요약", "상세", "설정"])

with tab1:
    st.write("요약 정보")

with tab2:
    st.write("상세 정보")

with tab3:
    st.write("설정")
```

### 확장 패널 (Expander)

```python
with st.expander("자세히 보기"):
    st.write("여기에 추가 정보가 표시됩니다")
```

### 실습 과제

- 위젯 중 하나를 사이드바로 이동해보세요
- 메트릭을 사용하여 KPI를 표시해보세요

**참고 파일**: 
- `apps/example_app1.py` - 레이아웃 데모
- `apps/streamlit_layouts_organization.py` - 레이아웃 실습

---

## 7. 미니 프로젝트

### 프로젝트: 매출 스냅샷 대시보드

주문 데이터를 분석하는 인터랙티브 대시보드를 만들어봅시다!

#### 목표

- CSV 파일 업로드
- 날짜와 지역으로 필터링
- 4개의 KPI 표시 (총 매출, 판매 수량, 주문 수, 평균 주문 금액)
- 시간별 매출 추이 차트
- 데이터 테이블

#### 필수 컬럼

- `date`: 주문 날짜
- `region`: 지역
- `product`: 제품명
- `units`: 수량
- `unit_price`: 단가

#### 샘플 데이터

프로젝트 폴더에 포함된 샘플 데이터를 사용하세요:
- `data/orders_sample.csv` - 작은 샘플 데이터
- `data/orders_large.csv` - 큰 샘플 데이터

#### 단계별 구현

1. **파일 업로드** - `st.file_uploader` 사용
2. **데이터 전처리** - 날짜 파싱, 매출 계산
3. **사이드바 필터** - 날짜 범위, 지역 선택
4. **KPI 계산** - 필터링된 데이터에서 메트릭 계산
5. **차트 생성** - 시간별 매출 추이
6. **테이블 표시** - 필터링된 데이터

#### 추가 도전 과제

- 상위 5개 제품 막대 차트 추가
- CSV 다운로드 버튼
- 이전 기간 대비 KPI 델타 표시
- 제품 다중 선택 필터

#### 프로젝트 파일

- `mini-project/project_README.md` - 프로젝트 상세 설명
- `mini-project/scaffold_app.py` - 스캐폴드 코드 (실습용)
- `mini-project/solution_app.py` - 완성된 솔루션

#### 실행 방법

```bash
# 스캐폴드 버전 (실습용)
streamlit run mini-project/scaffold_app.py

# 솔루션 버전 (참고용)
streamlit run mini-project/solution_app.py
```

#### 완성 예제

**참고 파일**:
- `apps/example_app5.py` - 비즈니스 KPI 대시보드
- `scratch.py` - 레이아웃 예제

---

## 8. 마무리

### 학습 정리

이 교안을 통해 다음을 배웠습니다:

✅ Streamlit 앱을 로컬에서 실행하기  
✅ 기본 위젯으로 인터랙티브 기능 추가하기  
✅ 테이블과 차트로 데이터 표시하기  
✅ CSV 파일 업로드 및 데이터 필터링하기  
✅ 사이드바와 레이아웃으로 앱 구조화하기  
✅ 실전 대시보드 프로젝트 구축하기  

### 추가 학습 자료

- **공식 문서**: https://docs.streamlit.io
- **갤러리**: https://streamlit.io/gallery
- **포럼**: https://discuss.streamlit.io
- **GitHub**: https://github.com/streamlit/streamlit

### 배포하기

#### Streamlit Community Cloud

무료로 Streamlit 앱을 배포할 수 있습니다!

1. GitHub에 코드를 푸시
2. https://share.streamlit.io 방문
3. 저장소 연결
4. 배포!

#### 필요한 파일

```
your-app/
├── app.py
├── requirements.txt  # 필요한 패키지 목록
└── README.md
```

**requirements.txt 예제**:
```
streamlit==1.28.0
pandas==2.0.3
numpy==1.24.3
altair==5.0.1
```

### 베스트 프랙티스

1. **캐싱 사용**: `@st.cache_data`로 데이터 로딩 최적화
2. **세션 상태**: `st.session_state`로 상태 관리
3. **에러 처리**: `try-except`로 사용자 친화적인 에러 메시지
4. **로딩 표시**: `st.spinner()`로 진행 상황 표시
5. **반응형 레이아웃**: `use_container_width=True` 사용

### 성능 최적화 팁

```python
# 데이터 캐싱
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# 함수 캐싱
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

# 진행 상황 표시
with st.spinner("데이터 로딩 중..."):
    data = load_large_dataset()
```

---

## 📁 프로젝트 구조

```
Python_streamlit/
├── apps/                          # 예제 앱들
│   ├── example_app.py            # 기본 할인 계산기
│   ├── example_app1.py           # 레이아웃 데모
│   ├── example_app2.py           # 폼과 입력 위젯
│   ├── example_app3.py           # 데이터 시각화
│   ├── example_app4.py           # 파일 업로드
│   ├── example_app5.py           # KPI 대시보드
│   ├── streamlit_intro.py        # 입문 실습
│   ├── streamlit_with_data.py    # 데이터 다루기
│   ├── streamlit_layouts_organization.py  # 레이아웃 실습
│   └── streamlit_mini_project.py # 미니 프로젝트 실습
├── data/                          # 샘플 데이터
│   ├── orders_sample.csv         # 작은 샘플
│   └── orders_large.csv          # 큰 샘플
├── mini-project/                  # 미니 프로젝트
│   ├── project_README.md         # 프로젝트 설명
│   ├── scaffold_app.py           # 실습용 스캐폴드
│   └── solution_app.py           # 완성 솔루션
├── scratch.py                     # 연습용 스크래치 파일
├── README.md                      # 이 파일
└── streamlit_lecture_part_1.html  # 강의 자료 (파트 1)
└── streamlit_lecture_part_2.html  # 강의 자료 (파트 2)
```

---

## 💡 자주 묻는 질문 (FAQ)

### Q: Streamlit 앱이 자동으로 새로고침되나요?
A: 네! 코드를 저장하면 브라우저에서 "Rerun" 버튼이 나타나며, 클릭하면 앱이 업데이트됩니다.

### Q: 여러 페이지를 만들 수 있나요?
A: 네! `pages/` 폴더를 만들고 각 페이지를 별도 파일로 저장하면 자동으로 다중 페이지 앱이 됩니다.

### Q: 데이터베이스에 연결할 수 있나요?
A: 네! SQLite, PostgreSQL, MySQL 등 모든 Python 데이터베이스 라이브러리를 사용할 수 있습니다.

### Q: 인증 기능을 추가할 수 있나요?
A: 네! `streamlit-authenticator` 같은 패키지를 사용하거나 커스텀 인증을 구현할 수 있습니다.

---

## 🎯 다음 단계

1. **예제 앱 실행**: `apps/` 폴더의 모든 예제를 실행해보세요
2. **미니 프로젝트 완성**: `mini-project/scaffold_app.py`를 완성하세요
3. **자신만의 앱 만들기**: 관심 있는 데이터로 대시보드를 만들어보세요
4. **배포하기**: Streamlit Community Cloud에 앱을 배포해보세요

---

## 📞 문의 및 지원

- **버그 리포트**: GitHub Issues에 문제를 제기하세요
- **질문**: Streamlit 포럼이나 Stack Overflow를 활용하세요
- **기여**: Pull Request는 언제나 환영합니다!

---

## 📄 라이선스

이 교안은 교육 목적으로 자유롭게 사용할 수 있습니다.

---

**즐거운 Streamlit 개발 되세요!** 🚀
