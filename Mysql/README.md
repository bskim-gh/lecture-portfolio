# MySQL 종합 교육 과정

## 📚 과정 개요

본 교육 자료는 MySQL/MariaDB 데이터베이스의 기본 쿼리 문법과 데이터 조작 방법을 다루는 실무 중심 교육 과정입니다. SQL 초보자와 비전공자도 쉽게 학습할 수 있도록 단계별로 구성되었으며, 실제 업무에서 자주 사용하는 SELECT 쿼리를 중심으로 구성되었습니다.

**총 11개 섹션**으로 구성된 체계적인 MySQL 학습 커리큘럼 (초급 과정, 약 2-4주)

---

## 🎓 교육 주제 및 커리큘럼

### 📌 Section 1: 기본 데이터 조회 (SELECT)

**01_Select.md - MySQL SELECT 문**
- SELECT 문 기본 구문
- 단일 컬럼 조회
- 여러 컬럼 조회
- 모든 컬럼 조회 (\*)
- 결과 집합(Result Set) 이해

**주요 학습 내용:**
```sql
SELECT lastName, firstName 
FROM employees;
```

---

### 📌 Section 2: 데이터 정렬 (ORDER BY)

**02_OrderBy.md - MySQL ORDER BY 절**
- 오름차순(ASC) / 내림차순(DESC) 정렬
- 단일 컬럼 정렬
- 여러 컬럼 정렬
- 표현식(Expression)으로 정렬
- FIELD() 함수를 이용한 사용자 정의 정렬
- NULL 값 정렬 처리

**주요 학습 내용:**
```sql
SELECT customerName, creditLimit
FROM customers
ORDER BY creditLimit DESC;
```

---

### 📌 Section 3: 조건부 데이터 조회 (WHERE)

**03_Where.md - MySQL WHERE 절**
- WHERE 절 기본 문법
- 등호 연산자(=)
- 비교 연산자(<, >, <=, >=, <>, !=)
- AND 연산자
- OR 연산자
- BETWEEN 연산자
- LIKE 연산자
- IN 연산자
- IS NULL 연산자

**주요 학습 내용:**
```sql
SELECT lastName, firstName, jobTitle
FROM employees
WHERE jobTitle = 'Sales Rep' AND officeCode = 1;
```

---

### 📌 Section 4: 중복 제거 (DISTINCT)

**04_Distinct.md - MySQL DISTINCT 절**
- DISTINCT 절 기본 개념
- 단일 컬럼 중복 제거
- 여러 컬럼 조합 중복 제거
- DISTINCT와 NULL 값 처리

**주요 학습 내용:**
```sql
SELECT DISTINCT state, city
FROM customers
WHERE state IS NOT NULL;
```

---

### 📌 Section 5: 논리 연산자 (AND)

**05_AND.md - MySQL AND 연산자**
- AND 연산자 개념
- 여러 조건 결합
- 단락 평가(Short-circuit Evaluation)
- AND 연산자 진리표
- 실무 활용 예제

**주요 학습 내용:**
```sql
SELECT customername, country, state, creditlimit
FROM customers
WHERE country = 'USA' AND state = 'CA' AND creditlimit > 100000;
```

---

### 📌 Section 6: 논리 연산자 (OR)

**06_OR.md - MySQL OR 연산자**
- OR 연산자 개념
- 여러 조건 중 하나만 만족
- 단락 평가
- AND와 OR의 연산자 우선순위
- 괄호를 이용한 우선순위 제어
- OR 연산자 진리표

**주요 학습 내용:**
```sql
SELECT customername, country, creditLimit
FROM customers
WHERE (country = 'USA' OR country = 'France')
      AND creditlimit > 100000;
```

---

### 📌 Section 7: 값 목록 검색 (IN)

**07_In.md - MySQL IN 연산자**
- IN 연산자 개념
- 값 목록으로 조건 검색
- IN과 OR의 차이
- IN 연산자와 NULL 처리
- 서브쿼리와 IN 연산자

**주요 학습 내용:**
```sql
SELECT officeCode, city, phone, country
FROM offices
WHERE country IN ('USA', 'France');
```

---

### 📌 Section 8: 범위 검색 (BETWEEN)

**08_Between.md - MySQL BETWEEN 연산자**
- BETWEEN 연산자 개념
- 숫자 범위 검색
- 날짜 범위 검색
- NOT BETWEEN
- CAST() 함수를 이용한 날짜 처리

**주요 학습 내용:**
```sql
SELECT productCode, productName, buyPrice
FROM products
WHERE buyPrice BETWEEN 90 AND 100;
```

---

### 📌 Section 9: 패턴 매칭 (LIKE)

**09_Like.md - MySQL LIKE 연산자**
- LIKE 연산자 개념
- 퍼센트(%) 와일드카드
- 밑줄(\_) 와일드카드
- NOT LIKE
- ESCAPE 절
- 패턴 검색 실무 예제

**주요 학습 내용:**
```sql
SELECT employeeNumber, lastName, firstName
FROM employees
WHERE firstName LIKE 'a%';

SELECT employeeNumber, lastName, firstName
FROM employees
WHERE lastname LIKE '%on%';
```

---

### 📌 Section 10: 결과 제한 (LIMIT)

**10_Limit.md - MySQL LIMIT 절**
- LIMIT 절 기본 개념
- 상위 N개 행 조회
- OFFSET을 이용한 특정 위치부터 조회
- 페이지네이션(Pagination) 구현
- N번째 최고/최저 값 조회
- LIMIT과 ORDER BY 조합
- LIMIT과 DISTINCT 조합

**주요 학습 내용:**
```sql
-- 상위 5명 조회
SELECT customerNumber, customerName, creditLimit
FROM customers
ORDER BY creditLimit DESC
LIMIT 5;

-- 페이지네이션 (11~20번째 행)
SELECT customerNumber, customerName
FROM customers
ORDER BY customerName
LIMIT 10, 10;
```

---

### 📌 Section 11: 스키마 및 테이블 구조 (Schema)

**11_Schema.md - MySQL 스키마 이해**
- 데이터베이스 스키마 개념
- 테이블 생성 (CREATE TABLE)
- 컬럼 데이터 타입
  - 숫자형 (INT, DECIMAL, FLOAT, DOUBLE)
  - 문자형 (CHAR, VARCHAR, TEXT)
  - 날짜/시간형 (DATE, TIME, DATETIME, TIMESTAMP)
- 키(Key) 유형
  - PRIMARY KEY (기본 키)
  - FOREIGN KEY (외래 키)
  - UNIQUE KEY (고유 키)
  - INDEX (인덱스)
- 테이블 관계 (Relationships)
  - 일대다 (One-to-Many)
  - 다대다 (Many-to-Many)
  - 일대일 (One-to-One)
- CASCADE 옵션
  - ON DELETE CASCADE
  - ON DELETE SET NULL
  - ON DELETE RESTRICT
  - ON UPDATE CASCADE
- 스키마 설계 모범 사례

**주요 학습 내용:**
```sql
-- 테이블 생성 및 관계 정의
CREATE TABLE employees (
    employeeNumber INT NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    officeCode VARCHAR(10) NOT NULL,
    reportsTo INT NULL,
    PRIMARY KEY (employeeNumber),
    FOREIGN KEY (officeCode) 
        REFERENCES offices(officeCode)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (reportsTo) 
        REFERENCES employees(employeeNumber)
        ON DELETE SET NULL
);
```

---

## 🗄️ 샘플 데이터베이스

### cardbdemo.sql
샘플 데이터베이스는 다음 7개의 테이블로 구성되어 있습니다:

**1. customers (고객 정보)**
- 고객 번호, 고객명, 연락처, 주소, 담당 영업사원, 신용한도 등

**2. employees (직원 정보)**
- 직원 번호, 이름, 이메일, 직책, 사무실 코드, 상사 정보 등

**3. offices (사무실 정보)**
- 사무실 코드, 도시, 전화번호, 주소, 국가, 지역 등

**4. orders (주문 정보)**
- 주문 번호, 주문일, 배송일, 상태, 고객 번호 등

**5. orderdetails (주문 상세)**
- 주문 번호, 제품 코드, 수량, 가격, 순서 등

**6. products (제품 정보)**
- 제품 코드, 제품명, 제품 라인, 재고, 구매가격, 판매가격 등

**7. payments (결제 정보)**
- 고객 번호, 수표 번호, 결제일, 결제 금액 등

**8. productlines (제품 라인)**
- 제품 라인, 설명, 이미지 등

---

## 📖 학습 로드맵

### 🔰 Week 1: 기본 조회 및 정렬 (1주차)
- **Day 1-2**: SELECT 문 (01_Select.md)
  - 기본 조회 문법 익히기
  - 단일/여러 컬럼 선택
  - 실습: employees 테이블 조회
  
- **Day 3-4**: ORDER BY 절 (02_OrderBy.md)
  - 오름차순/내림차순 정렬
  - 여러 컬럼 정렬
  - 실습: customers를 creditLimit으로 정렬
  
- **Day 5-7**: WHERE 절 (03_Where.md)
  - 조건부 검색 기초
  - 비교 연산자 활용
  - 실습: 특정 직책의 직원 찾기

---

### 🔸 Week 2: 중급 조회 기법 (2주차)
- **Day 1-2**: DISTINCT (04_Distinct.md)
  - 중복 제거
  - 실습: 고유한 도시/주 조회
  
- **Day 3-4**: AND & OR (05_AND.md, 06_OR.md)
  - 논리 연산자
  - 연산자 우선순위
  - 실습: 복합 조건 쿼리 작성
  
- **Day 5-7**: IN, BETWEEN, LIKE (07-09)
  - 값 목록 검색
  - 범위 검색
  - 패턴 매칭
  - 실습: 다양한 검색 조건 적용

---

### 🔶 Week 3-4: 고급 활용 및 실전 (3-4주차)
- **Day 1-3**: LIMIT (10_Limit.md)
  - 상위/하위 N개 조회
  - 페이지네이션 구현
  - 실습: 톱 10 고객 조회
  
- **Day 4-7**: 종합 실습
  - 여러 절 조합
  - 실무 시나리오 쿼리 작성
  - 샘플 데이터베이스 전체 탐색

---

## 💡 실무 활용 예제

### 📊 비즈니스 쿼리 예제

**1. 매출 상위 10개 제품 조회**
```sql
SELECT p.productName, SUM(od.quantityOrdered * od.priceEach) AS revenue
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
GROUP BY p.productCode
ORDER BY revenue DESC
LIMIT 10;
```

**2. 지역별 고객 수 조회**
```sql
SELECT country, COUNT(*) AS customerCount
FROM customers
GROUP BY country
ORDER BY customerCount DESC;
```

**3. 배송 지연 주문 조회**
```sql
SELECT orderNumber, orderDate, shippedDate, 
       DATEDIFF(shippedDate, orderDate) AS daysDelay
FROM orders
WHERE status = 'Shipped' 
  AND DATEDIFF(shippedDate, orderDate) > 5
ORDER BY daysDelay DESC;
```

**4. 우수 고객 (신용한도 상위 5%) 조회**
```sql
SELECT customerName, creditLimit
FROM customers
WHERE creditLimit IS NOT NULL
ORDER BY creditLimit DESC
LIMIT 5;
```

---

## 🔧 환경 설정

### 샘플 데이터베이스 설치

```bash
# MySQL/MariaDB 접속
mysql -u root -p

# 데이터베이스 생성
CREATE DATABASE cardbdemo;

# 데이터베이스 선택
USE cardbdemo;

# SQL 파일 실행
source /path/to/cardbdemo.sql;

# 또는 외부에서 실행
mysql -u root -p cardbdemo < cardbdemo.sql
```

---

### GUI 도구

| 도구 | 특징 | 운영체제 | 다운로드 |
|------|------|---------|---------|
| **MySQL Workbench** | 공식 GUI, 무료, ERD 지원 | Win/Mac/Linux | https://dev.mysql.com/downloads/workbench/ |
| **HeidiSQL** | 가볍고 빠름, 무료 | Windows | https://www.heidisql.com/ |
| **DBeaver** | 다중 DB 지원, 무료 | Win/Mac/Linux | https://dbeaver.io/ |
| **phpMyAdmin** | 웹 기반, 무료 | 웹브라우저 | https://www.phpmyadmin.net/ |
| **Navicat** | 강력한 기능, 유료 | Win/Mac/Linux | https://www.navicat.com/ |
| **DataGrip** | JetBrains 제품, 유료 | Win/Mac/Linux | https://www.jetbrains.com/datagrip/ |

---

## 🐍 Python에서 MySQL/MariaDB 연결하기

### pymysql 설치

```bash
pip install pymysql
```

---

### 기본 연결 템플릿

**1. 기본 연결 및 조회**

```python
import pymysql

# 데이터베이스 연결
connection = pymysql.connect(
    host='localhost',      # 호스트명
    user='root',           # 사용자명
    password='your_password',  # 비밀번호
    database='cardbdemo',  # 데이터베이스명
    charset='utf8mb4',     # 문자셋
    cursorclass=pymysql.cursors.DictCursor  # 딕셔너리 형태로 결과 반환
)

try:
    # 커서 생성
    with connection.cursor() as cursor:
        # SQL 쿼리 실행
        sql = "SELECT * FROM customers LIMIT 5"
        cursor.execute(sql)
        
        # 결과 가져오기
        result = cursor.fetchall()
        
        # 결과 출력
        for row in result:
            print(row)
            
finally:
    # 연결 종료
    connection.close()
```

---

**2. 파라미터를 사용한 안전한 쿼리 (SQL Injection 방지)**

```python
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='cardbdemo',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        # 파라미터를 사용한 안전한 쿼리
        sql = "SELECT * FROM customers WHERE country = %s AND creditLimit > %s"
        cursor.execute(sql, ('USA', 50000))
        
        result = cursor.fetchall()
        print(f"검색 결과: {len(result)}건")
        
        for row in result:
            print(row)
            
finally:
    connection.close()
```

---

**3. 데이터 삽입 (INSERT)**

```python
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='cardbdemo',
    charset='utf8mb4'
)

try:
    with connection.cursor() as cursor:
        # 데이터 삽입
        sql = """INSERT INTO customers 
                 (customerNumber, customerName, contactLastName, contactFirstName, 
                  phone, addressLine1, city, country, salesRepEmployeeNumber, creditLimit)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        cursor.execute(sql, (
            500, 'Test Company', 'Kim', 'Chulsoo', 
            '010-1234-5678', '123 Main St', 'Seoul', 'South Korea', 
            1370, 50000.00
        ))
    
    # 변경사항 커밋 (중요!)
    connection.commit()
    print("데이터가 성공적으로 삽입되었습니다.")
    
except Exception as e:
    # 오류 발생 시 롤백
    connection.rollback()
    print(f"오류 발생: {e}")
    
finally:
    connection.close()
```

---

**4. Context Manager를 사용한 자동 연결 종료**

```python
import pymysql
from contextlib import closing

# with 구문으로 자동 연결 종료
with closing(pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='cardbdemo',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)) as connection:
    
    with connection.cursor() as cursor:
        # 직원 정보 조회
        cursor.execute("SELECT * FROM employees WHERE jobTitle = %s", ('Sales Rep',))
        employees = cursor.fetchall()
        
        print(f"Sales Rep 수: {len(employees)}명")
        for emp in employees:
            print(f"{emp['firstName']} {emp['lastName']} - {emp['email']}")
```

---

**5. 실무 활용 - 함수로 재사용 가능한 코드**

```python
import pymysql
from typing import List, Dict, Any

def get_db_connection():
    """데이터베이스 연결 생성"""
    return pymysql.connect(
        host='localhost',
        user='root',
        password='your_password',
        database='cardbdemo',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(sql: str, params: tuple = None) -> List[Dict[str, Any]]:
    """SELECT 쿼리 실행"""
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()
    finally:
        connection.close()

def execute_update(sql: str, params: tuple = None) -> int:
    """INSERT, UPDATE, DELETE 쿼리 실행"""
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            affected_rows = cursor.execute(sql, params)
            connection.commit()
            return affected_rows
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        connection.close()

# 사용 예제
if __name__ == "__main__":
    # 고객 조회
    customers = execute_query(
        "SELECT * FROM customers WHERE country = %s ORDER BY creditLimit DESC LIMIT 10",
        ('USA',)
    )
    
    for customer in customers:
        print(f"{customer['customerName']}: ${customer['creditLimit']:,.2f}")
    
    # 데이터 업데이트
    rows_affected = execute_update(
        "UPDATE customers SET creditLimit = creditLimit * 1.1 WHERE country = %s",
        ('USA',)
    )
    print(f"{rows_affected}개 행이 업데이트되었습니다.")
```

---

**6. Pandas와 함께 사용하기**

```python
import pymysql
import pandas as pd

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='cardbdemo',
    charset='utf8mb4'
)

# Pandas DataFrame으로 직접 읽기
df = pd.read_sql("SELECT * FROM customers WHERE country = 'USA'", connection)

print(df.head())
print(f"\n총 {len(df)}개의 레코드")

# 통계 정보
print(df['creditLimit'].describe())

connection.close()
```

---

### 주요 메서드 정리

| 메서드 | 설명 |
|--------|------|
| `cursor.execute(sql, params)` | SQL 쿼리 실행 |
| `cursor.fetchone()` | 결과에서 1개 행 가져오기 |
| `cursor.fetchall()` | 결과에서 모든 행 가져오기 |
| `cursor.fetchmany(size)` | 결과에서 지정한 개수만큼 가져오기 |
| `connection.commit()` | 변경사항 커밋 (INSERT, UPDATE, DELETE 후 필수) |
| `connection.rollback()` | 변경사항 롤백 (오류 시) |
| `connection.close()` | 연결 종료 |

---

### 환경변수로 접속 정보 관리 (보안 강화)

**config.py**
```python
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'cardbdemo'),
    'charset': 'utf8mb4'
}
```

**.env 파일**
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=cardbdemo
```

**사용 예제**
```python
import pymysql
from config import DB_CONFIG

connection = pymysql.connect(**DB_CONFIG)
# ... 나머지 코드
```

**필요한 패키지 설치**
```bash
pip install pymysql python-dotenv pandas
```

---

## 🤔 사내 MariaDB와 MySQL은 다른것인가??

### 🔹 1. 기원

**MySQL**은 1995년 MySQL AB가 만든 오픈소스 DB입니다.

2008년 **오라클(Oracle)**이 MySQL AB를 인수했습니다.

이때 "오픈소스 정신이 훼손될 것"을 우려한 개발자들이 MySQL을 Fork(복제) 해서 만든 게 바로 **MariaDB**입니다.
→ 즉, **MariaDB는 MySQL의 오픈소스 분기(fork) 버전**입니다.

---

### 🔹 2. 호환성

MariaDB는 MySQL 5.5 버전까지 완전 호환을 목표로 했기 때문에,

**CREATE, SELECT, UPDATE, DELETE 같은 SQL 문법은 동일합니다.**

`mysql` 클라이언트, `pymysql`, `SQLAlchemy`, `phpMyAdmin` 등도 그대로 쓸 수 있습니다.

실제로 MariaDB 서버에 접속하면 프롬프트가 `MariaDB [(db명)]>`으로만 다르고 나머지는 동일하게 작동합니다.

---

### 🔹 3. 차이점 (버전이 올라가면서 점점 커짐)

| 구분 | MySQL | MariaDB |
|------|-------|---------|
| **라이선스** | GPL + Oracle 상용라이선스 | 100% GPL (오픈소스 유지) |
| **소유** | Oracle | MariaDB Foundation |
| **스토리지 엔진** | InnoDB 중심 | InnoDB + Aria, XtraDB, ColumnStore 등 |
| **JSON 처리** | 5.7 이후 고도화 | 10.2 이후 자체 함수 제공 |
| **성능 및 기능** | 안정성 위주 | 기능 추가 및 성능 개선 중심 |
| **버전 표기** | 5.7 → 8.0 | 10.0 → 11.x (독자 버전 체계) |

---

### 🔹 4. 실제 사용 시 차이

`mysqlclient`나 `pymysql` 같은 파이썬 라이브러리로 접속 시에도
접속 문자열만 다를 뿐 거의 차이 없이 동작합니다.

```python
# MySQL
pymysql.connect(host='localhost', user='root', password='pw', db='testdb')

# MariaDB (동일하게 작동)
pymysql.connect(host='localhost', user='root', password='pw', db='testdb')
```

---

### 🔹 5. 정리 요약

✅ **구조와 명령어는 거의 같음**  
✅ **MariaDB는 MySQL의 오픈소스 자유 버전**  
✅ **MySQL은 Oracle 관리 하에 있고, MariaDB는 커뮤니티 중심으로 발전**  
✅ **기업에서는 라이선스 비용 회피나 오픈소스 선호 시 MariaDB,  
상용 지원 및 안정성 중시 시 MySQL을 선택**

---

## 📚 추가 학습 자료

### 공식 문서
- **MySQL 공식 문서**: https://dev.mysql.com/doc/
- **MariaDB 공식 문서**: https://mariadb.org/documentation/

### 온라인 학습
- **W3Schools SQL**: https://www.w3schools.com/sql/
- **SQLZoo**: https://sqlzoo.net/
- **LeetCode SQL**: https://leetcode.com/problemset/database/
- **HackerRank SQL**: https://www.hackerrank.com/domains/sql

### 책
- "SQL 첫걸음" - 아사이 아츠시
- "모두의 SQL" - 오가와 모모요시
- "Learning SQL" - Alan Beaulieu

---

## 💡 학습 팁

### ✅ 효과적인 학습 방법

1. **직접 타이핑**: 예제를 복사하지 말고 직접 타이핑하며 익히기
2. **샘플 데이터 활용**: cardbdemo.sql로 다양한 쿼리 실험하기
3. **오류 메시지 읽기**: 에러를 두려워하지 말고 메시지를 읽고 이해하기
4. **EXPLAIN 활용**: 쿼리 실행 계획 확인하는 습관 들이기

### 📅 일일 학습 루틴 (30분-1시간)

- **10분**: 이론 학습 (MD 파일 읽기)
- **20분**: 예제 따라하기 및 변형
- **20분**: 샘플 데이터로 응용 쿼리 작성
- **10분**: 오늘 배운 내용 정리 (노트 작성)

### 🎯 단계별 학습 전략

**초급 (1-2주)**
- SELECT, FROM, WHERE 완벽하게 익히기
- ORDER BY로 정렬 연습
- 기본 비교 연산자 활용

**중급 (3-4주)**
- 논리 연산자 조합 연습
- LIKE, IN, BETWEEN으로 다양한 검색
- LIMIT으로 결과 제한

**고급 (추후 학습)**
- JOIN으로 여러 테이블 결합
- GROUP BY로 데이터 집계
- 서브쿼리 활용
- 인덱스 최적화

---

## 🎓 학습 후 다음 단계

### 더 배워야 할 주제들

1. **JOIN** - 여러 테이블 결합
   - INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN
   
2. **집계 함수** - 데이터 통계
   - COUNT, SUM, AVG, MIN, MAX
   - GROUP BY, HAVING

3. **서브쿼리** - 중첩 쿼리
   - 스칼라 서브쿼리, 인라인 뷰, 중첩 서브쿼리

4. **데이터 조작** - DML
   - INSERT, UPDATE, DELETE

5. **데이터 정의** - DDL
   - CREATE, ALTER, DROP

6. **트랜잭션** - 데이터 무결성
   - COMMIT, ROLLBACK, SAVEPOINT

7. **인덱스** - 성능 최적화
   - 인덱스 생성 및 활용

8. **프로시저/함수** - 저장 프로그램
   - Stored Procedure, Function, Trigger

---

## 📬 문의 및 피드백

궁금한 점이나 개선 사항이 있으시면 언제든지 문의해 주세요!

---

**Happy Learning! 즐거운 MySQL 학습 되세요! 🚀**

