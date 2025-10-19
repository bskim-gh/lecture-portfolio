# 비개발부서를 위한 Python 교육 과정

## 📚 과정 개요

본 교육 과정은 비개발 부서 실무자를 위한 Python 기초부터 실무 활용까지 체계적으로 구성된 교육 프로그램입니다. 프로그래밍 경험이 없는 비전공자도 Python을 활용하여 업무 자동화와 데이터 처리를 할 수 있도록 설계되었습니다.

**총 9개 Section**으로 구성된 실무 중심 Python 학습 커리큘럼

---

## 📖 Section 구성

### Section 1: Python 소개 및 기본 문법

**학습 목표:**
- Python 설치 및 개발 환경 설정
- 기본 출력 함수 활용 (print)
- 인코딩과 기본 문법 이해
- 가상환경 설정 및 패키지 관리 (pip)

**주요 내용:**
- **Python 소개 및 기본 출력**
  - Hello Python! 첫 프로그램
  - print 함수의 다양한 활용법
  - sep, end, file 옵션 사용
  - format 함수와 문자열 포맷팅

- **기본 코딩 실습**
  - Python 2.x vs 3.x 차이
  - 입출력 인코딩 (stdin, stdout)
  - 변수 선언 (한글 변수명 가능)
  - 기본 조건문과 반복문
  - 함수와 클래스 기초
  - 객체 정보 확인 (id, dir, class)

- **가상환경과 패키지 관리**
  - 가상환경 생성 및 활성화
  - pip 명령어 (search, install, uninstall)
  - 패키지 버전 관리
  - requirements.txt 생성 및 활용

---

### Section 2: 데이터 타입

**학습 목표:**
- Python의 기본 데이터 타입 이해
- 숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합 활용

**주요 내용:**
- **숫자형 (Numeric Types)**
  - int (정수), float (실수), complex (복소수)
  - 산술 연산자 (+, -, *, /, //, %, **)
  - 형 변환 (int, float, complex)
  - 수학 함수 (abs, divmod, pow, math 모듈)
  - 진법 변환 (bin, oct, hex)

- **문자열 (String)**
  - 문자열 생성 및 출력
  - 이스케이프 문자 (\n, \t, \", \')
  - Raw String (r'...')
  - 멀티라인 문자열
  - 문자열 연산 및 메서드
  - 슬라이싱과 인덱싱
  - immutable 특성
  - 아스키 코드 (ord, chr)

- **리스트와 튜플**
  - 리스트: 순서O, 중복O, 수정O, 삭제O
  - 튜플: 순서O, 중복O, 수정X, 삭제X
  - 인덱싱과 슬라이싱
  - 리스트 메서드 (append, sort, reverse, insert, remove, pop)
  - 튜플 언패킹

- **딕셔너리와 집합**
  - 딕셔너리: 키-값 쌍, 순서X, 중복X
  - keys(), values(), items() 메서드
  - 집합: 중복X, 순서X
  - 집합 연산 (합집합, 교집합, 차집합)

- **실습 문제**
  - 16가지 실전 퀴즈 및 정답
  - 문자열 처리, 리스트 조작, 딕셔너리 활용

---

### Section 3: 흐름 제어

**학습 목표:**
- 조건문과 반복문을 활용한 프로그램 흐름 제어
- 다양한 반복문 패턴 이해

**주요 내용:**
- **조건문**
  - if, elif, else 구문
  - 관계 연산자 (>, >=, <, <=, ==, !=)
  - 논리 연산자 (and, or, not)
  - 참/거짓 판별 ("", [], (), {}, 0, None)
  - 다중 조건문과 중첩 조건문
  - in, not in 연산자

- **반복문**
  - while 루프
  - for 루프와 range 함수
  - 시퀀스 자료형 순회 (문자열, 리스트, 튜플, 딕셔너리)
  - break와 continue
  - for-else, while-else 구문
  - flag 변수 활용
  - 중첩 반복문 (구구단 예제)

- **iterable 함수**
  - range, reversed, enumerate, filter, map, zip

- **실습 문제**
  - 조건문 문제 (5문제)
  - 반복문 문제 (5문제)
  - 정답 및 해설 포함

---

### Section 4: 함수

**학습 목표:**
- 함수의 정의 및 호출
- 다양한 매개변수 활용법
- 람다식(Lambda) 이해

**주요 내용:**
- **함수 기본**
  - 함수 정의 (def)
  - 함수 호출
  - 매개변수와 인자
  - 반환값 (return)

- **다중 반환**
  - 튜플 반환
  - 리스트 반환
  - 딕셔너리 반환
  - 다중 값 언패킹

- **가변 매개변수**
  - *args: 가변 위치 인자
  - **kwargs: 가변 키워드 인자
  - 매개변수 순서: 일반 → *args → **kwargs

- **고급 함수**
  - 중첩 함수 (Nested Function)
  - 람다 함수 (Lambda Expression)
  - 람다 함수와 map, filter 활용

---

### Section 5: 클래스

**학습 목표:**
- 객체지향 프로그래밍 기초
- 클래스와 인스턴스 이해
- 상속 개념 및 활용

**주요 내용:**
- **클래스 기본**
  - 클래스 정의와 인스턴스 생성
  - `__init__()` 생성자
  - self 이해
  - `__del__()` 소멸자
  - 네임스페이스

- **클래스 변수 vs 인스턴스 변수**
  - 클래스 변수: 모든 인스턴스가 공유
  - 인스턴스 변수: 각 객체마다 독립적
  - `__dict__` 속성

- **상속 (Inheritance)**
  - 부모 클래스와 자식 클래스
  - super() 함수
  - 메서드 오버라이딩
  - 다중 상속
  - MRO (Method Resolution Order)

- **특수 메서드**
  - `__str__()`, `__repr__()`
  - 연산자 오버로딩

---

### Section 6: 모듈과 파일

**학습 목표:**
- 모듈과 패키지 개념 이해
- 파일 읽기 및 쓰기 작업

**주요 내용:**
- **모듈과 패키지**
  - 모듈 import 방법
  - from ... import ...
  - import ... as ... (별칭)
  - 패키지 구조 (상대 경로, 절대 경로)
  - `__init__.py`

- **파일 입출력**
  - 파일 열기 모드 (r, w, a, r+, w+, a+)
  - 파일 읽기 (read, readline, readlines)
  - 파일 쓰기 (write, writelines)
  - with 구문 활용 (자동 close)
  - 파일 포인터 이동 (seek, tell)

- **텍스트 파일 처리**
  - 상대 경로와 절대 경로
  - 인코딩 처리 (UTF-8, CP949)
  - 파일 반복문 순회
  - 파일 존재 확인

---

### Section 7: 예외처리 및 데이터 파일

**학습 목표:**
- 예외 상황 처리 방법
- CSV 및 Excel 파일 다루기

**주요 내용:**
- **예외처리**
  - 예외 종류 (SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError, ZeroDivisionError, FileNotFoundError)
  - try, except, else, finally 구문
  - 예외 메시지 출력
  - raise로 예외 발생시키기
  - 사용자 정의 예외
  - EAFP 코딩 스타일

- **CSV 파일 처리**
  - csv 모듈
  - csv.reader() - 읽기
  - csv.writer() - 쓰기
  - DictReader, DictWriter
  - delimiter, quotechar 옵션

- **Excel 파일 처리**
  - pandas 라이브러리
  - read_excel() - 읽기
  - to_excel() - 쓰기
  - DataFrame 조작
  - 데이터 필터링 및 정렬

---

### Section 8: 데이터베이스

**학습 목표:**
- SQLite 데이터베이스 기초
- Python으로 데이터베이스 연동

**주요 내용:**
- **SQLite 기초**
  - sqlite3 모듈
  - 데이터베이스 생성 및 연결
  - 커서 (Cursor) 객체
  - Auto Commit 설정

- **테이블 생성 및 데이터 삽입**
  - CREATE TABLE 문
  - 데이터 타입 (TEXT, NUMERIC, INTEGER, REAL, BLOB)
  - INSERT INTO 문
  - executemany() - 여러 행 삽입
  - 매개변수 바인딩 (?)

- **데이터 조회**
  - SELECT 문
  - fetchone(), fetchmany(), fetchall()
  - WHERE 조건절
  - ORDER BY 정렬
  - 반복문으로 결과 순회

- **데이터 수정 및 삭제**
  - UPDATE 문
  - DELETE 문
  - rowcount 속성
  - commit()과 rollback()
  - 트랜잭션 관리

---

### Section 9: 프로젝트 실습

**학습 목표:**
- 실무 프로젝트 제작
- 배운 내용 종합 활용

**주요 내용:**
- **타이핑 게임 제작**
  - **기본 버전**
    - 단어 파일 읽기
    - 랜덤 단어 선택
    - 사용자 입력 체크
    - 시간 측정 (time 모듈)
    - 정답 개수 카운트

  - **고급 버전 (사운드 & DB 연동)**
    - winsound 모듈로 사운드 효과
    - SQLite DB에 게임 기록 저장
    - 게임 기록 조회
    - 순위 표시
    - 랭킹 시스템

- **주소록 프로그램 제작**
  - **기능**
    - 연락처 추가
    - 연락처 조회 (전체, 검색)
    - 연락처 수정
    - 연락처 삭제
  
  - **기술**
    - 클래스 기반 설계 (Contact, ContactBook)
    - pickle 모듈로 파일 저장/불러오기
    - 메뉴 시스템 구현
    - 예외처리
    - 데이터 영속성

---

## 🎯 학습 포인트

### 핵심 개념
1. **Python 기초**: print, 변수, 자료형, 연산자
2. **데이터 타입**: int, float, str, list, tuple, dict, set
3. **흐름 제어**: if, while, for, break, continue
4. **함수**: def, return, *args, **kwargs, lambda
5. **클래스**: class, self, 상속, 메서드
6. **파일/모듈**: import, open, with, csv
7. **예외처리**: try, except, finally
8. **데이터베이스**: SQLite, CRUD 작업

### 실무 활용
- **업무 자동화**: 파일 처리, 데이터 정리
- **데이터 관리**: CSV/Excel 파일 처리
- **데이터베이스**: 데이터 저장 및 조회
- **프로젝트**: 타이핑 게임, 주소록 프로그램

---

## 📊 권장 학습 순서

### 1단계: 기초 (1-2주)
- **Section 1-2**: Python 기본 문법 및 데이터 타입
- 목표: 변수, 자료형, 연산자 이해

### 2단계: 중급 (2주)
- **Section 3-4**: 흐름 제어 및 함수
- 목표: 조건문, 반복문, 함수 작성 능력

### 3단계: 객체지향 (1-2주)
- **Section 5-6**: 클래스 및 모듈
- 목표: 클래스 설계 및 파일 처리

### 4단계: 실무 (2주)
- **Section 7-8**: 예외처리 및 데이터베이스
- 목표: 안정적인 프로그램 작성

### 5단계: 프로젝트 (1-2주)
- **Section 9**: 종합 프로젝트 실습
- 목표: 배운 내용을 활용한 실전 프로그램 제작

---

## 💡 학습 방법

### 효과적인 학습 전략
1. **직접 타이핑**: 코드를 복사하지 말고 직접 타이핑
2. **실험하기**: 코드를 변형하며 결과 확인
3. **퀴즈 풀기**: 각 Section의 퀴즈 문제 도전
4. **프로젝트 수정**: 기본 프로젝트를 자신만의 방식으로 커스터마이징

### 일일 학습 루틴 (1-2시간)
- **30분**: 새로운 개념 학습 및 예제 실습
- **30분**: 퀴즈 문제 풀이
- **30분**: 자유 코딩 및 실험

---

## 📂 파일 구조

```
Python_비개발부서용/
├── 00_전체_교안_개요.md (본 문서)
├── 01_Section1_교안.py (Python 소개 및 기본 문법)
├── 02_Section2_교안.py (데이터 타입)
├── 03_Section3_교안.py (흐름 제어)
├── 04_Section4_교안.py (함수)
├── 05_Section5_교안.py (클래스)
├── 06_Section6_교안.py (모듈과 파일)
├── 07_Section7_교안.py (예외처리 및 데이터 파일)
├── 08_Section8_교안.py (데이터베이스)
└── 09_Section9_교안.py (프로젝트 실습)
```

---

## 🛠️ 필요한 라이브러리

```bash
# 기본 라이브러리 (Python 내장)
# - sqlite3, csv, pickle, time, datetime, random

# 외부 라이브러리
pip install pandas openpyxl  # Excel 파일 처리
pip install simplejson  # JSON 처리
```

---

## 🎯 활용 분야

### 업무 자동화
- 반복적인 파일 처리 작업 자동화
- 데이터 정리 및 정제
- 보고서 자동 생성

### 데이터 관리
- CSV/Excel 파일 읽기 및 쓰기
- 데이터베이스 연동
- 데이터 분석 기초

### 간단한 프로그램 제작
- 주소록, 일정 관리 등 개인 도구
- 간단한 게임
- 데이터 수집 스크립트

---

## 📝 정리

본 교육 과정은 비개발 부서 실무자를 위한 Python 입문 과정입니다. 프로그래밍 경험이 없어도 단계별로 학습하면 Python을 활용한 업무 자동화와 데이터 처리가 가능합니다.

**모든 코드는 주석 없이 실행 가능한 상태로 제공되며**, 각 Section별로 실습 파일이 분리되어 있어 체계적인 학습이 가능합니다.

각 Section의 퀴즈 문제와 프로젝트 실습을 통해 실전 감각을 키우고, 자신만의 프로그램을 만들어보세요!

