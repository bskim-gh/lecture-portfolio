# Python 실습 교육 과정

## 📚 과정 개요

본 교육 과정은 Python 프로그래밍의 기초부터 실전 응용까지 체계적으로 학습하는 실습 중심 과정입니다. 각 챕터별로 실습 예제를 직접 코딩하며 Python의 핵심 개념을 익히고, 실무에 필요한 프로그래밍 능력을 키울 수 있습니다.

**총 10개 Chapter**로 구성된 실습 중심 Python 학습 커리큘럼

---

## 📖 Chapter 구성

### Ch01: Python 기초

**주요 내용:**
- Hello World 출력
- print() 함수 기본 사용법
- print() 함수의 end 파라미터를 이용한 출력 제어

**학습 포인트:**
- Python 프로그램의 첫 시작
- 출력 함수의 기본 사용법
- end 파라미터로 줄바꿈 제어

---

### Ch02: Python 변수와 자료구조

**주요 내용:**
- **변수(Variable)**
  - 변수 선언 및 메모리 주소
  - id() 함수로 메모리 주소 확인
  - 예약어 확인 (keyword.kwlist)

- **자료형(Data Type)**
  - 정수형(int)
  - 실수형(float)
  - 논리형(bool)
  - 문자열(string)
  - 자료형 변환 (type casting)

- **연산자**
  - 대입 연산자 (=)
  - 산술 연산자 (+, -, *, /, //, %, **)
  - 비교 연산자 (==, !=, >, <, >=, <=)
  - 논리 연산자 (and, or, not)
  - 복합 대입 연산자 (+=, -=, *=, /=)

- **문자열 처리**
  - 문자열 인덱싱과 슬라이싱
  - 문자열 연산 (결합, 반복)
  - 문자열 메서드 (upper, lower, split, replace, strip)
  - 문자열 포맷팅 (%, .format(), f-string)
  - 이스케이프 문자 (\n, \t, \\, \', \")

- **표준 입출력**
  - input() - 사용자 입력
  - print() - 화면 출력
  - sep, end 파라미터

- **자료구조**
  - **리스트(List)**: 순서O, 중복O, 수정O
    - append(), extend(), insert(), remove(), pop()
  - **튜플(Tuple)**: 순서O, 중복O, 수정X
    - 불변 자료형, 언패킹
  - **딕셔너리(Dictionary)**: 키-값 쌍
    - keys(), values(), items(), get()
  - **집합(Set)**: 중복X, 순서X
    - 집합 연산 (합집합|, 교집합&, 차집합-)

---

### Ch03: Python 제어문

**주요 내용:**
- **조건문(Conditional Statement)**
  - if 문
  - if-else 문
  - if-elif-else 문
  - 단일 조건문과 중첩 조건문
  - 삼항 조건문 (조건부 표현식)

- **반복문(Loop)**
  - **while 반복문**
    - 무한 루프 (infinite loop)
    - break와 continue
  - **for 반복문**
    - range() 함수
    - 리스트/튜플 순회
    - enumerate() - 인덱스와 값 동시 반환
    - 이중 for문 (구구단, 별 삼각형)

- **random 모듈**
  - random.random()
  - random.randint()
  - random.choice()

**실습 예제:**
- 구구단 출력
- 별 삼각형 패턴
- 로또 번호 생성기

---

### Ch04: Python 자료구조 심화

**주요 내용:**
- **문자열 클래스 객체**
  - str() 생성자
  - 문자열 인덱싱

- **리스트 심화**
  - 단일 리스트와 중첩 리스트
  - 리스트 메서드 상세
    - append() - 끝에 추가
    - remove() - 값 삭제
    - insert() - 특정 위치 삽입
    - extend() - 리스트 확장
  - 리스트 정렬
    - sort() - 원본 정렬
    - sorted() - 정렬된 복사본
    - reverse() - 역순 정렬
  - **리스트 내포(List Comprehension)**
    - 간결한 리스트 생성
    - 조건부 리스트 내포

- **튜플 심화**
  - 튜플 관련 함수
  - 튜플의 불변성
  - 튜플 언패킹

- **집합(Set) 심화**
  - 집합 연산 (합집합, 교집합, 차집합)
  - 중복 제거 활용
  - add(), remove() 메서드

- **딕셔너리 심화**
  - 딕셔너리 메서드
  - 단어 빈도수 구하기

- **복사(Copy)**
  - 얕은 복사 (shallow copy)
  - 깊은 복사 (deep copy)
  - copy 모듈 사용

---

### Ch05: Python 함수와 모듈

**주요 내용:**
- **함수 기본**
  - 함수 정의 (def)
  - 함수 호출
  - 매개변수와 인자
  - 반환값 (return)

- **함수 4가지 유형**
  1. 매개변수 O, 리턴값 O
  2. 매개변수 O, 리턴값 X
  3. 매개변수 X, 리턴값 O
  4. 매개변수 X, 리턴값 X

- **매개변수 활용**
  - 디폴트 매개변수 (default parameter)
  - 가변 매개변수 (*args)
  - 다중 리턴값 (튜플, 리스트, 딕셔너리)

- **람다 함수 (Lambda Function)**
  - 익명 함수
  - 한 줄로 함수 정의
  - 함수를 변수에 저장

- **모듈(Module)**
  - import 문
  - from ... import ...
  - 별칭 (as)

- **내장 함수**
  - abs(), min(), max(), sum()
  - len(), type(), range()
  - map(), filter(), sorted()

- **표준 라이브러리**
  - **time 모듈**: time(), sleep()
  - **math 모듈**: sqrt(), pow(), ceil(), floor(), pi
  - **random 모듈**: random(), randint(), choice()
  - **statistics 모듈**: mean(), median(), variance(), stdev()

- **고급 함수 개념**
  - 함수 스코프 (global, local, nonlocal)
  - 일급 함수 (First-class Function)
  - 클로저 (Closure)
  - 함수 장식자 (Decorator) @decorator
  - 재귀 함수 (Recursive Function)

**실습 예제:**
- 피타고라스 정리 함수
- 몬테카를로 시뮬레이션
- 분산과 표준편차 계산
- 팩토리얼 재귀 함수

---

### Ch06: Python 객체지향 프로그래밍

**주요 내용:**
- **클래스 기본**
  - 함수 방식 vs 클래스 방식
  - 클래스 정의 (class)
  - 객체 생성 (인스턴스화)
  - 생성자 (`__init__()`)
  - self 키워드

- **속성과 메서드**
  - 인스턴스 속성
  - 인스턴스 메서드
  - 클래스 변수 vs 인스턴스 변수
  - 클래스 메서드 (@classmethod)

- **캡슐화(Encapsulation)**
  - 정보 은닉
  - private 변수 (__변수명)
  - getter/setter 메서드
  - @property 데코레이터

- **상속(Inheritance)**
  - 부모 클래스와 자식 클래스
  - super() 함수
  - 메서드 재정의 (Method Overriding)

- **다형성(Polymorphism)**
  - 메서드 오버라이딩
  - Duck Typing

**실습 예제:**
- 계산기 클래스
- 자동차 클래스
- 은행 계좌 클래스
- 사람/학생 클래스 (상속)

---

### Ch07: Python 정규표현식

**주요 내용:**
- **정규표현식 기본**
  - re 모듈 import
  - 패턴 매칭 개념

- **주요 함수**
  - findall() - 모든 매칭 문자열 찾기
  - match() - 문자열 시작부터 매칭
  - search() - 문자열 전체에서 첫 매칭
  - sub() - 문자열 치환

- **패턴 문법**
  - **숫자**: [0-9], \d
  - **문자**: [a-z], [A-Z], [가-힣]
  - **수량자**: {n}, {n,}, {n,m}
  - **위치**: ^(시작), $(끝)
  - **단어 문자**: \w
  - **공백**: \s

- **실습 예제**
  - 주민등록번호 유효성 검사
  - 이메일 주소 검증
  - 전화번호 추출
  - 문자열 전처리

---

### Ch08: Python 예외처리와 파일 입출력

**주요 내용:**
- **예외처리(Exception Handling)**
  - try-except 구문
  - try-except-finally 구문
  - try-except-else 구문
  - 예외 객체 활용
  - 사용자 정의 예외

- **파일 입출력**
  - **텍스트 파일 읽기**
    - open() 함수
    - read() - 전체 읽기
    - readline() - 한 줄 읽기
    - readlines() - 모든 줄 읽기
  - **텍스트 파일 쓰기**
    - write() - 문자열 쓰기
    - writelines() - 여러 줄 쓰기
  - **파일 모드**
    - 'r' - 읽기 모드
    - 'w' - 쓰기 모드 (덮어쓰기)
    - 'a' - 추가 모드
  - **파일 인코딩**
    - UTF-8, CP949, EUC-KR

- **CSV 파일 처리**
  - csv 모듈
  - csv.reader() - 읽기
  - csv.writer() - 쓰기

- **Excel 파일 처리**
  - pandas 라이브러리
    - read_excel() - 읽기
    - to_excel() - 쓰기
  - openpyxl 라이브러리
    - Workbook, Sheet 객체
    - 셀 읽기/쓰기

---

### Ch09: Python 웹 크롤링

**주요 내용:**
- **웹 크롤링 기초**
  - 웹 크롤링 개념
  - HTTP 요청/응답

- **requests 모듈**
  - GET 요청
  - 응답 객체 (status_code, text, content)
  - headers 설정

- **BeautifulSoup**
  - HTML 파싱
  - 태그 선택
    - select_one() - 단일 선택
    - select() - 다중 선택
  - CSS Selector 활용
  - 태그 속성 추출

- **Selenium**
  - 가상 브라우저 (ChromeDriver)
  - 웹 요소 찾기
    - find_element_by_css_selector()
    - find_element_by_id()
    - find_element_by_xpath()
  - 웹 요소 조작
    - click() - 클릭
    - send_keys() - 입력
    - clear() - 지우기
  - 대기 (implicitly_wait, WebDriverWait)

**실습 예제:**
- 네이버 뉴스 크롤링
- 인터파크 항공권 크롤링
- 날씨 정보 크롤링
- 크롤링 데이터 Excel 저장
- 크롤링 데이터 DB 저장

---

### Ch10: Python 데이터베이스 프로그래밍

**주요 내용:**
- **MySQL 연동**
  - pymysql 모듈
  - 데이터베이스 연결
  - cursor 객체 생성
  - CRUD 작업
    - INSERT - 데이터 삽입
    - SELECT - 데이터 조회
    - UPDATE - 데이터 수정
    - DELETE - 데이터 삭제
  - commit() - 변경사항 확정
  - fetchall() - 전체 결과 조회
  - fetchone() - 단일 결과 조회

- **SQLite 연동**
  - sqlite3 모듈 (Python 내장)
  - 데이터베이스 생성
  - 테이블 생성
  - CRUD 프로그래밍
  - 트랜잭션 관리

**실습 예제:**
- 사용자 등록 프로그램
- 사용자 조회 프로그램
- SQLite 데이터베이스 생성
- CRUD 작업 실습

---

## 🎯 학습 포인트

### 핵심 개념
1. **Python 기초**: 변수, 자료형, 연산자, 입출력
2. **제어문**: if, while, for, break, continue
3. **자료구조**: list, tuple, dict, set, comprehension
4. **함수**: def, return, lambda, *args, decorator
5. **OOP**: class, 상속, 캡슐화, 다형성
6. **정규표현식**: re 모듈, 패턴 매칭
7. **예외처리**: try-except-finally
8. **파일 처리**: 텍스트, CSV, Excel
9. **웹 크롤링**: requests, BeautifulSoup, Selenium
10. **데이터베이스**: MySQL, SQLite, CRUD

### 실무 활용
- **데이터 처리**: CSV/Excel 파일 읽기/쓰기
- **웹 크롤링**: 웹 데이터 수집 및 분석
- **데이터베이스**: 데이터 저장 및 관리
- **자동화**: 반복 작업 자동화

---

## 📊 권장 학습 순서

### 1단계: 기초 (1-2주)
- **Ch01-Ch02**: Python 기초 및 변수/자료구조
- 목표: 변수, 자료형, 연산자, 기본 자료구조 이해

### 2단계: 제어문 (1주)
- **Ch03**: 조건문과 반복문
- 목표: if, while, for 문 완전 숙달

### 3단계: 자료구조 심화 (1주)
- **Ch04**: 자료구조 심화
- 목표: 리스트 내포, 복사, 고급 메서드 활용

### 4단계: 함수 (1-2주)
- **Ch05**: 함수와 모듈
- 목표: 함수 정의, 람다, 재귀, 모듈 활용

### 5단계: 객체지향 (2주)
- **Ch06**: 클래스와 OOP
- 목표: 클래스 설계, 상속, 캡슐화

### 6단계: 고급 활용 (2주)
- **Ch07-Ch08**: 정규표현식, 예외처리, 파일 입출력
- 목표: 정규표현식 활용, 안정적인 파일 처리

### 7단계: 실전 응용 (3-4주)
- **Ch09-Ch10**: 웹 크롤링, 데이터베이스
- 목표: 실전 프로젝트 구현 능력

---

## 💡 학습 방법

### 효과적인 학습 전략
1. **직접 타이핑**: 코드를 직접 타이핑하며 체득
2. **실험하기**: 코드를 변형하며 결과 확인
3. **디버깅**: 에러 메시지를 읽고 문제 해결
4. **프로젝트**: 배운 내용을 조합한 미니 프로젝트

### 실습 루틴
- **Step 1**: 예제 코드 읽고 이해
- **Step 2**: 예제 코드 직접 타이핑 및 실행
- **Step 3**: 코드 변형하며 실험
- **Step 4**: 직접 문제 만들고 풀기

---

## 🛠️ 필요한 라이브러리

```bash
# 웹 크롤링
pip install requests beautifulsoup4 lxml selenium

# 파일 처리
pip install pandas openpyxl xlrd xlsxwriter

# 데이터베이스
pip install pymysql  # sqlite3는 기본 내장

# 웹 드라이버
# ChromeDriver 다운로드 필요
# https://chromedriver.chromium.org/
```

---

## 📂 파일 구조

```
Python_실습/
├── Ch01_교안.py (Python 기초)
├── Ch02_교안.py (변수와 자료구조)
├── Ch03_교안.py (제어문)
├── Ch04_교안.py (자료구조 심화)
├── Ch05_교안.py (함수와 모듈)
├── Ch06_교안.py (객체지향 프로그래밍)
├── Ch07_교안.py (정규표현식)
├── Ch08_교안.py (예외처리와 파일 입출력)
├── Ch09_교안.py (웹 크롤링)
├── Ch10_교안.py (데이터베이스 프로그래밍)
├── chromedriver.exe (Selenium용 웹 드라이버)
└── 종합_테스트.py (종합 실습)
```

---

## 🎯 활용 분야

### 데이터 분석
- CSV/Excel 파일 처리
- 데이터 정제 및 전처리
- 통계 분석

### 웹 크롤링
- 뉴스 수집
- 가격 정보 수집
- 데이터 모니터링

### 업무 자동화
- 반복 작업 자동화
- 보고서 자동 생성
- 데이터 일괄 처리

### 데이터베이스 관리
- 데이터 저장 및 조회
- 데이터 분석 및 리포팅

---

## 📝 정리

본 교육 과정은 Python 프로그래밍의 기초부터 실전 응용까지 체계적으로 학습하는 실습 중심 과정입니다. 각 Chapter를 순서대로 학습하며 예제 코드를 직접 실습하면 Python 개발 능력을 확실하게 키울 수 있습니다.

**특징:**
- 실습 중심의 체계적인 커리큘럼
- 단계별로 난이도 상승
- 실무에 바로 적용 가능한 예제
- 웹 크롤링과 데이터베이스 연동 포함

각 Chapter의 예제를 직접 코딩하고 변형하며 자신만의 프로젝트를 만들어보세요!

