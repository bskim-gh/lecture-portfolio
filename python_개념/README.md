# Python 개념 교육 과정

## 📚 과정 개요

본 교육 과정은 Python 프로그래밍의 핵심 개념을 체계적으로 학습하는 과정입니다. 환경 설정부터 데이터베이스 연동까지 Python의 기본 개념과 실무 활용을 위한 필수 지식을 다룹니다.

**총 7개 Section**으로 구성된 체계적인 Python 학습 커리큘럼

---

## 📖 교안 구성

### Section 1: Python 기초 - 환경 설정 및 기본 문법

**학습 목표:**
- Python의 특징과 활용 분야 이해
- Anaconda를 통한 Python 개발 환경 설정
- 변수, 자료형, 연산자의 기본 개념 숙지
- 조건문과 반복문을 활용한 흐름 제어
- 함수와 모듈을 통한 코드 재사용

**주요 내용:**
- **파이썬 소개와 설치**
  - 파이썬의 특징과 장점
  - 아나콘다(Anaconda) 설치 및 설정
  - Jupyter Notebook 소개
  - 가상 환경 생성과 관리

- **변수, 자료형, 연산자**
  - 변수 선언과 할당
  - 기본 자료형 (int, float, str, bool)
  - 산술, 비교, 논리, 할당, 멤버십 연산자
  - 컬렉션 자료형 (list, tuple, dict, set)

- **조건문과 반복문**
  - if, elif, else 조건문
  - while 루프와 for 루프
  - range(), enumerate(), zip() 함수
  - break, continue 제어문

- **함수와 모듈**
  - 함수 정의와 호출
  - 매개변수와 반환값
  - 기본값 인자
  - 가변 인자 (*args, **kwargs)
  - 람다 함수
  - 재귀 함수
  - 모듈 임포트와 사용

- **실전 예제**
  - 문자열 처리 (슬라이싱, 포맷팅, 메서드)
  - 수학 함수 활용
  - 다양한 함수 패턴

---

### Section 2: Python 자료구조와 파일 처리

**학습 목표:**
- 리스트, 튜플, 딕셔너리, 집합 등 Python의 핵심 자료구조 이해
- 리스트와 딕셔너리 컴프리헨션을 활용한 효율적인 코드 작성
- 파일 입출력과 다양한 인코딩 처리 방법 학습
- 대용량 파일 처리 기법 습득

**주요 내용:**
- **자료 구조**
  - 리스트 (Lists): 생성, 인덱싱, 슬라이싱, 메서드
  - 튜플 (Tuples): 불변 자료형, 언패킹
  - 딕셔너리 (Dictionaries): 키-값 쌍, 메서드
  - 집합 (Sets): 중복 제거, 집합 연산

- **컴프리헨션**
  - 리스트 컴프리헨션
  - 조건부 리스트 컴프리헨션
  - 딕셔너리 컴프리헨션

- **파일 입출력**
  - 파일 열기와 닫기
  - with 구문을 사용한 파일 처리
  - read(), readline(), readlines() 메서드
  - write() 메서드
  - 인코딩 처리 (UTF-8, EUC-KR, CP949)

- **대용량 파일 처리**
  - chunk 단위 읽기
  - read() 메서드 활용
  - iter() 함수 활용

---

### Section 3: 객체지향 프로그래밍 (OOP)

**학습 목표:**
- 클래스와 객체의 개념 이해
- 상속과 다형성을 통한 코드 재사용
- OOP를 활용한 실전 프로젝트 구현

**주요 내용:**
- **클래스와 객체**
  - 클래스 정의
  - 객체 생성 (인스턴스화)
  - `__init__()` 생성자
  - self 키워드
  - 인스턴스 변수와 메서드

- **상속과 다형성**
  - 상속 (Inheritance)
  - 하위 클래스와 상위 클래스
  - IS-A 관계
  - 메서드 오버라이딩 (Overriding)
  - 다형성 (Polymorphism)

- **실전 프로젝트**
  - 직원 관리 시스템
  - Employee 클래스
  - Company 클래스
  - 객체 간 관계 설정

---

### Section 4: 데이터 분석 기초

**학습 목표:**
- NumPy와 Pandas의 기본 개념과 활용 이해
- 데이터 전처리 및 정제 기법 학습
- Matplotlib와 Seaborn을 활용한 데이터 시각화

**주요 내용:**
- **NumPy**
  - 다차원 배열 (ndarray)
  - 배열 생성과 연산
  - 브로드캐스팅 (Broadcasting)
  - 벡터화 (Vectorization)
  - 선형대수, 통계 함수

- **Pandas**
  - Series와 DataFrame
  - DataFrame 생성과 조작
  - 데이터 필터링과 정렬
  - 데이터 그룹화와 집계

- **데이터 전처리**
  - 결측치 확인 (isna())
  - 결측치 처리 (fillna())
  - 평균/중앙값으로 대체
  - 중복 데이터 제거 (drop_duplicates())

- **데이터 시각화**
  - Matplotlib: 선 그래프, 산점도, 막대 그래프
  - Seaborn: 통계 그래프, 히트맵
  - 그래프 커스터마이징 (제목, 라벨, 색상)

---

### Section 5: 머신러닝 기초

**학습 목표:**
- Scikit-learn을 사용한 지도학습과 비지도학습 이해
- 회귀, 분류, 군집화 등 기본 알고리즘 학습
- 모델 평가 및 성능 향상 기법 습득

**주요 내용:**
- **지도학습 (Supervised Learning)**
  - K-Nearest Neighbors (KNN) 분류
  - 데이터 분할 (train_test_split)
  - 모델 학습과 예측
  - 정확도 평가

- **비지도학습 (Unsupervised Learning)**
  - K-Means 군집화
  - 클러스터 할당
  - 군집 중심 확인
  - 결과 시각화

- **기본 알고리즘**
  - 회귀 (Regression): Linear Regression
  - 분류 (Classification): Logistic Regression
  - 군집화 (Clustering): K-Means

- **모델 평가**
  - Accuracy (정확도)
  - Precision (정밀도)
  - Recall (재현율)
  - F1 Score
  - Confusion Matrix (혼동 행렬)

- **성능 향상**
  - 하이퍼파라미터 튜닝
  - GridSearchCV
  - 최적의 파라미터 찾기
  - Random Forest 분류

---

### Section 6: 웹 개발 기초

**학습 목표:**
- Flask와 Django 웹 프레임워크 이해
- 웹 애플리케이션 구축과 데이터 표시 방법 학습
- 사용자 입력 처리와 데이터 저장 구현

**주요 내용:**
- **Flask 소개**
  - 마이크로 웹 프레임워크
  - 라우팅 (Routing)
  - 간단한 웹 애플리케이션 구축
  - 템플릿 사용

- **Django 소개**
  - 풀스택 웹 프레임워크
  - MVT (Model-View-Template) 패턴
  - ORM (Object-Relational Mapping)
  - Admin 인터페이스
  - 보안 기능

- **웹 애플리케이션 구축**
  - Flask 설치 및 설정
  - 프로젝트 구조 설계
  - 라우팅과 뷰 함수
  - 템플릿 렌더링
  - CSV 데이터 표시

- **사용자 입력 처리**
  - HTML 폼 생성
  - POST 요청 처리
  - request 객체 사용
  - 데이터 파일 저장
  - 성공 페이지 표시

---

### Section 7: 데이터베이스 연동

**학습 목표:**
- SQL 기본 문법 이해
- SQLite와 MySQL 데이터베이스 사용법 학습
- Python과 데이터베이스 연동 방법 습득

**주요 내용:**
- **SQL 기본 문법**
  - CREATE DATABASE / TABLE
  - INSERT INTO
  - SELECT FROM WHERE
  - UPDATE SET
  - DELETE FROM
  - 데이터 타입과 제약 조건

- **SQLite 사용**
  - 경량 데이터베이스
  - 파일 기반 데이터베이스
  - Python 내장 모듈
  - sqlite3 모듈 사용
  - 커서 생성 및 쿼리 실행

- **MySQL 사용**
  - 서버 기반 데이터베이스
  - mysql-connector-python 설치
  - MySQL 서버 연결
  - CRUD 작업 수행

- **Python 연동**
  - connect() 함수
  - cursor() 메서드
  - execute() / executemany()
  - fetchone() / fetchall()
  - commit() / rollback()
  - close() 연결 종료

- **실습 예제**
  - 학생 데이터베이스 생성
  - 데이터 삽입/조회/수정/삭제
  - 트랜잭션 관리

---

## 🎯 학습 포인트

### 핵심 개념
1. **Python 기초**: 변수, 자료형, 연산자, 제어문
2. **자료구조**: list, tuple, dict, set, 컴프리헨션
3. **OOP**: 클래스, 객체, 상속, 다형성
4. **데이터 분석**: NumPy, Pandas, 시각화
5. **머신러닝**: 지도/비지도학습, 모델 평가
6. **웹 개발**: Flask, Django, 라우팅, 템플릿
7. **데이터베이스**: SQL, SQLite, MySQL, CRUD

### 실무 활용
- **데이터 처리**: 파일 입출력, 인코딩, 대용량 파일
- **데이터 분석**: 전처리, 정제, 시각화
- **웹 개발**: 사용자 입력 처리, 데이터 표시
- **데이터베이스**: Python과 DB 연동, 데이터 관리

---

## 📊 학습 진행 방법

### 권장 학습 순서
1. **Section 1-2**: Python 기초 문법과 자료구조 (1-2주)
2. **Section 3**: 객체지향 프로그래밍 (1주)
3. **Section 4**: 데이터 분석 기초 (1-2주)
4. **Section 5**: 머신러닝 기초 (2주)
5. **Section 6**: 웹 개발 기초 (1-2주)
6. **Section 7**: 데이터베이스 연동 (1주)

### 학습 팁
- 각 Section의 예제 코드를 직접 타이핑하며 실습
- Quiz 문제를 통해 학습 내용 점검
- 실전 프로젝트를 통해 개념 적용 연습
- 에러 메시지를 읽고 디버깅 연습

---

## 🛠️ 필요한 라이브러리

```bash
# 기본 과학 계산 및 데이터 분석
pip install numpy pandas matplotlib seaborn

# 머신러닝
pip install scikit-learn

# 웹 개발
pip install flask

# 데이터베이스 (MySQL)
pip install mysql-connector-python
```

---

## 💡 추가 학습 자료

### 공식 문서
- Python 공식 문서: https://docs.python.org/ko/3/
- NumPy 문서: https://numpy.org/doc/
- Pandas 문서: https://pandas.pydata.org/docs/
- Scikit-learn 문서: https://scikit-learn.org/
- Flask 문서: https://flask.palletsprojects.com/

### 추천 학습 경로
- 기초부터 차근차근 따라가며 학습
- 각 Section의 실습 예제를 반드시 직접 코딩
- 프로젝트를 통해 실무 적용 능력 향상
- 커뮤니티와 공식 문서 활용

---

## 📝 정리

본 교육 과정은 Python의 기초 개념부터 실무 활용까지 체계적으로 다루는 종합 과정입니다. 환경 설정, 기본 문법, 자료구조, OOP, 데이터 분석, 머신러닝, 웹 개발, 데이터베이스 연동 등 Python 개발자로서 필요한 모든 핵심 개념을 학습할 수 있습니다.

각 Section을 순서대로 학습하며 예제를 직접 실습하면 Python의 핵심 개념을 확실하게 익힐 수 있습니다.

