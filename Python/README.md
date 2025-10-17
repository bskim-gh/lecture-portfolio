# Python 종합 교육 과정

## 📚 과정 개요

본 교육 자료는 Python 프로그래밍의 기초부터 실무 활용까지 다루는 종합 교육 과정입니다. 비전공자와 비개발 부서 실무자도 학습할 수 있도록 단계별로 구성되었으며, 데이터 분석, 웹 개발, 웹 크롤링 등 다양한 실무 분야를 포괄합니다.

**총 47개 파일**로 구성된 체계적인 Python 학습 커리큘럼 (초급 → 고급, 약 6-9개월 과정)

---

## 🎓 교육 주제 및 커리큘럼

### 📌 Level 1: Python 기초 (초급)

**1-1. 환경 설정 및 시작**
- Python/Anaconda 설치, IDE 선택 (Cursor, VS Code, PyCharm)
- 가상환경 관리 (venv, conda), pip 패키지 설치
- Hello World, print() 함수, 주석

**1-2. 기본 문법**
- **자료형**: int, float, bool, str, None
- **연산자**: 산술(+,-,*,/,//,%,**), 비교(==,!=,>,<), 논리(and,or,not), 멤버십(in)
- **문자열**: 인덱싱, 슬라이싱, 메서드(upper, lower, strip, split, replace), f-string
- **입출력**: input(), print()

**1-3. 자료구조**
- **리스트**: 생성, 인덱싱, 슬라이싱, append(), extend(), insert(), remove(), sort(), 리스트 컴프리헨션
- **튜플**: 불변 자료형, 언패킹
- **딕셔너리**: 키-값 쌍, keys(), values(), items(), get(), 딕셔너리 컴프리헨션
- **집합**: 중복 제거, 집합 연산(합집합|, 교집합&, 차집합-)

**1-4. 제어문**
- **조건문**: if-elif-else, 중첩 조건문, 삼항 연산자
- **반복문**: while, for, range(), enumerate(), zip(), break, continue, else

**1-5. 실습 예제**
- 구구단, 별 패턴, 피보나치 수열, 로또 번호 생성기

---

### 📌 Level 2: 함수와 모듈 (중급)

**2-1. 함수**
- 함수 정의/호출, 매개변수(위치/키워드/기본값), 반환값
- 가변 매개변수: `*args`, `**kwargs`
- 람다 함수, 재귀 함수 (팩토리얼, GCD)
- 스코프: local, global, nonlocal

**2-2. 고급 함수**
- 중첩 함수, 클로저, 데코레이터 (@decorator)
- 일급 함수 (함수를 변수에 저장, 인자로 전달)

**2-3. 모듈과 패키지**
- 모듈 생성, import, from ... import, as
- 패키지 구조, `__init__.py`, `__name__` == `__main__`
- **내장 모듈**: math, random, time, datetime, os, sys, json, re

**2-4. 유용한 내장 함수**
- map(), filter(), sorted(), zip(), enumerate()
- abs(), sum(), max(), min(), len(), range()
- type(), isinstance(), dir(), help()

---

### 📌 Level 3: 객체지향 프로그래밍 (중-고급)

**3-1. 클래스 기초**
- 클래스 정의, 객체 생성, `__init__()` 생성자, self
- 인스턴스 변수 vs 클래스 변수
- 인스턴스 메서드, 클래스 메서드 (@classmethod), 정적 메서드 (@staticmethod)

**3-2. 캡슐화와 상속**
- **캡슐화**: private 변수 (`__변수`), getter/setter, @property
- **상속**: 부모-자식 클래스, super(), 메서드 오버라이딩
- **다형성**: Duck Typing, 오버라이딩
- **다중 상속**: MRO (Method Resolution Order)

**3-3. 특수 메서드**
- `__str__`, `__repr__`, `__len__`, `__getitem__`, `__add__` (연산자 오버로딩)

**3-4. 실전 예제**
- 계산기 클래스, 은행 계좌 클래스, 학생 관리 시스템, 직원 관리 시스템

---

### 📌 Level 4: 파일 처리 및 예외 처리 (중급)

**4-1. 파일 입출력**
- **텍스트 파일**: open(), read(), readline(), readlines(), write(), close(), with 구문
- 파일 모드: 'r', 'w', 'a', 'r+', 'w+', 'a+'
- 인코딩: UTF-8, EUC-KR, CP949
- 대용량 파일: chunk 단위 읽기

**4-2. 데이터 파일**
- **CSV**: csv.reader(), csv.writer(), csv.DictReader()
- **Excel**: pandas (read_excel, to_excel), openpyxl, xlsxwriter
- **JSON**: json.load(), json.dump(), json.loads(), json.dumps()
- **직렬화**: pickle.dump(), pickle.load()

**4-3. 예외 처리**
- try-except-else-finally
- 예외 종류: SyntaxError, NameError, TypeError, ValueError, IndexError, KeyError, ZeroDivisionError, FileNotFoundError
- raise 예외 발생, 사용자 정의 예외

**4-4. 정규표현식**
- **re 모듈**: match(), search(), findall(), sub(), split()
- **패턴**: \d(숫자), \w(문자), \s(공백), .(임의문자), *(0회이상), +(1회이상), ?(0또는1), {n,m}
- **응용**: 이메일 검증, 전화번호 검증, 주민번호 검증

---

### 📌 Level 5: 데이터베이스 (중급)

**5-1. SQL 기초**
- CREATE DATABASE/TABLE, INSERT INTO, SELECT FROM WHERE, UPDATE SET, DELETE FROM, DROP

**5-2. SQLite**
- sqlite3 모듈, connect(), cursor(), execute(), fetchone(), fetchall(), commit(), close()
- 실습: 주소록, 게임 기록 저장

**5-3. MySQL/MariaDB**
- pymysql 모듈, 연결 파라미터 (host, user, password, database)
- 실습: 사용자 등록/조회 프로그램

---

### 📌 Level 6: 데이터 분석 (고급)

**6-1. NumPy**
- ndarray 배열: 생성 (array, zeros, ones, arange), 인덱싱, 슬라이싱, reshape
- 배열 연산: 브로드캐스팅, 벡터화, 산술 연산
- 집계 함수: sum(), mean(), std(), var()

**6-2. Pandas**
- **Series & DataFrame**: 생성, 인덱싱 (loc, iloc), 열/행 추가/삭제
- **데이터 로딩**: read_csv(), read_excel(), to_csv(), to_excel()
- **데이터 전처리**:
  - 결측치: isna(), fillna(), dropna()
  - 중복 제거: drop_duplicates()
  - 정렬: sort_values(), sort_index()
  - 필터링, 그룹화 (groupby), 피봇 (pivot_table), 병합 (merge, concat)

**6-3. 데이터 시각화**
- **Matplotlib**: plot(), scatter(), bar(), hist(), pie(), 그래프 커스터마이징
- **Seaborn**: scatterplot(), lineplot(), barplot(), boxplot(), heatmap(), pairplot()

---

### 📌 Level 7: 머신러닝 기초 (고급)

**7-1. Scikit-learn**
- 데이터셋 로딩, train_test_split()
- **지도학습**:
  - 회귀: Linear Regression (MSE, RMSE, R²)
  - 분류: Logistic Regression, K-Nearest Neighbors, Decision Tree, Random Forest
  - 평가: Accuracy, Precision, Recall, F1 Score, Confusion Matrix
- **비지도학습**: K-Means Clustering, 계층적 군집화

**7-2. 모델 최적화**
- 교차 검증: K-Fold, Stratified K-Fold
- 하이퍼파라미터 튜닝: GridSearchCV, RandomizedSearchCV
- 특성 선택: 특성 중요도, PCA

---

### 📌 Level 8: 웹 개발 (고급)

**8-1. Flask**
- 라우팅: @app.route(), URL 파라미터, GET/POST
- 템플릿: render_template(), Jinja2 문법
- 폼 처리: request 객체, 파일 업로드
- 정적 파일: url_for()
- 실습: 블로그, 데이터 표시 웹앱, 사용자 입력 처리

**8-2. Django** (선택)
- MVT 패턴, 모델(ORM), 뷰, 템플릿, URL 설정

---

### 📌 Level 9: 웹 크롤링 (고급)

**9-1. 기본 크롤링**
- **urllib**: urlopen(), urlretrieve(), urlparse(), urlencode()
- HTTP 상태 코드, 헤더, 예외 처리 (HTTPError, URLError)

**9-2. requests**
- GET, POST, PUT, DELETE 요청
- Response: status_code, text, content, json()
- Session: 쿠키 유지, 로그인 세션
- 헤더 설정: User-Agent, Referer
- timeout, stream, iter_lines()

**9-3. BeautifulSoup**
- HTML 파싱: BeautifulSoup 객체, prettify()
- 태그 접근: find(), find_all(), select(), select_one()
- CSS 선택자: 자식(>), ID(#), 클래스(.), 속성([]), nth-of-type()
- 데이터 추출: .text, .string, ['속성']

**9-4. lxml**
- HTML 파싱: fromstring(), cssselect(), xpath()

**9-5. Selenium (동적 크롤링)**
- WebDriver 설정 (Chrome, Firefox)
- 페이지 제어: get(), set_window_size(), implicitly_wait(), WebDriverWait
- 요소 찾기: find_element_by_id/name/class_name/css_selector/xpath
- 요소 조작: send_keys(), click(), submit(), clear()
- 페이지 정보: page_source, current_url, title, get_cookies()
- 스크린샷: save_screenshot()
- Headless 모드: --headless 옵션

**9-6. 크롤링 실전**
- 네이버 뉴스 수집, 이미지 다운로드, 쇼핑몰 상품 정보, 주식 정보
- 로그인 처리, 다중 페이지 크롤링
- Excel/DB 저장, fake_useragent

---

### 📌 Level 10: 실전 프로젝트

**10-1. 게임 프로젝트**
- 타이핑 게임 (time 모듈, winsound, SQLite 기록 저장)
- 숫자 맞추기 게임 (예외 처리)

**10-2. 데이터 관리**
- 주소록 프로그램 (클래스, pickle 직렬화)
- 학생 관리 시스템, 직원 관리 시스템

**10-3. 크롤링 프로젝트**
- 뉴스 수집 및 분석, 부동산 정보 수집
- 쇼핑몰 가격 비교, 날씨 정보 대시보드

**10-4. 데이터 분석 프로젝트**
- 판매 데이터 시각화, 고객 데이터 분석, 추천 시스템

**10-5. 업무 자동화**
- Excel 리포트 자동 생성, 이메일 자동 발송
- 파일 정리 자동화, 웹 폼 자동 제출

---

## 🛠️ 필수 라이브러리

```bash
# 데이터 분석
pip install numpy pandas matplotlib seaborn scikit-learn

# 웹 크롤링
pip install requests beautifulsoup4 lxml selenium fake-useragent

# 파일 처리
pip install openpyxl xlsxwriter xlrd

# 데이터베이스
pip install pymysql  # sqlite3는 기본 내장

# 웹 프레임워크
pip install flask django
```

---

## 📖 학습 로드맵

### 🔰 Step 1: 기초 (1-2개월)
- Python 설치 (Python/Anaconda) + IDE (Cursor/VS Code/PyCharm)
- 변수, 자료형, 연산자, 문자열
- 리스트, 딕셔너리, 집합
- 조건문, 반복문
- **실습**: 구구단, 계산기, 로또 생성기

### 🔸 Step 2: 중급 (2-3개월)
- 함수 (기본, 람다, 재귀)
- 모듈, 내장 함수
- 클래스, 상속, 다형성
- 파일 처리, 예외 처리
- **실습**: 주소록, 은행 계좌 시스템

### 🔶 Step 3: 실무 (2-3개월)
- 데이터베이스 (SQLite, MySQL)
- NumPy, Pandas, 데이터 시각화
- Excel 자동화
- 정규표현식
- **실습**: 데이터 분석 리포트, Excel 자동화

### 🔺 Step 4: 고급 (3-4개월)
- 웹 크롤링 (requests, BeautifulSoup, Selenium)
- 머신러닝 기초 (Scikit-learn)
- 웹 개발 (Flask)
- API 호출 및 개발
- **실습**: 크롤링 자동화, 웹 애플리케이션

### 🎯 Step 5: 프로젝트 (1-2개월)
- 포트폴리오 프로젝트 개발
- GitHub 저장소 구축
- 문서화 및 발표 자료 작성

---

## 💡 목표별 학습 경로

### 🎯 업무 자동화
**경로**: 기초 → 파일처리 → Excel (pandas, openpyxl) → 크롤링 기초 → 이메일 자동화  
**프로젝트**: Excel 리포트 자동 생성, 이메일 발송, 웹 데이터 수집

### 🎯 데이터 분석가
**경로**: 기초 → 함수 → NumPy/Pandas → 시각화 → 통계 → 머신러닝 → SQL  
**프로젝트**: 판매 데이터 분석, 고객 세그멘테이션, 예측 모델

### 🎯 웹 개발자
**경로**: 기초 → OOP → DB (SQL) → Flask/Django → HTML/CSS/JS → API 개발  
**프로젝트**: 블로그, 쇼핑몰, REST API 서버

### 🎯 웹 크롤링 전문가
**경로**: 기초 → 정규표현식 → requests/BeautifulSoup → Selenium → DB 저장  
**프로젝트**: 뉴스 수집, 부동산 정보 크롤링, 가격 모니터링

### 🎯 데이터 과학자
**경로**: 기초 → NumPy/Pandas → 시각화 → 통계 → 머신러닝 → 딥러닝  
**프로젝트**: 예측 모델, 이미지 분류, 자연어 처리, 추천 시스템

---

## 📚 효과적인 학습 방법

### ✅ 학습 원칙
1. **직접 타이핑**: 복붙 NO, 직접 타이핑하며 체득
2. **실험하기**: 예제 코드 변형, "만약 ~라면?" 질문
3. **문서 읽기**: 공식 문서, dir(), help() 활용
4. **디버깅**: 에러 메시지 읽기, print()로 중간 값 확인

### 📅 일일 루틴 (1-3시간)
- **오전 (30분-1시간)**: 새로운 개념 학습, 튜토리얼
- **점심 (30분)**: 코딩 문제 풀이
- **저녁 (1-2시간)**: 프로젝트 작업, 블로그 정리
- **주말**: 프로젝트 집중, 복습

### 🎨 프로젝트 기반 학습
1. 관심 분야 프로젝트 선정
2. 최소 기능(MVP)으로 시작
3. 기능 하나씩 추가
4. Git으로 버전 관리
5. README 작성

---

## 🔧 개발 환경 구성

### Python 설치

**Python 공식** (경량, 빠른 시작)
- https://www.python.org/downloads/
- 설치 시 "Add Python to PATH" 체크 필수

**Anaconda** (데이터 분석 권장)
- https://www.anaconda.com/download
- NumPy, Pandas, Jupyter Notebook 포함

### IDE 및 에디터

| IDE | 특징 | 추천 대상 | 다운로드 |
|-----|------|----------|---------|
| **Cursor** | AI 코딩 어시스턴트, 실시간 자동완성 | 초보자, 학습용 | https://cursor.sh |
| **VS Code** | 무료, 강력한 확장, Git 통합 | 범용 개발 | https://code.visualstudio.com |
| **Jupyter** | 셀 단위 실행, 시각화 즉시 확인 | 데이터 분석 | Anaconda 포함 |
| **PyCharm** | 전문 Python IDE, 강력한 디버깅 | 전문 개발자 | https://www.jetbrains.com/pycharm/ |
| **Colab** | 브라우저 실행, GPU 무료, 설치 불필요 | 학습, ML | https://colab.research.google.com |

### VS Code / Cursor 필수 확장
- Python (Microsoft)
- Pylance
- Jupyter
- GitLens
- Python Indent
---
