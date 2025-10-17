# Section 7: 데이터베이스 연동

## 📚 학습 목표
- SQL 기본 문법 이해
- SQLite와 MySQL 데이터베이스 사용법 학습
- Python과 데이터베이스 연동 방법 습득

---

## 7-1. SQL 소개

SQL(Structured Query Language)은 관계형 데이터베이스 관리 시스템(RDBMS)에서 데이터를 조작, 관리, 조회하는데 사용되는 언어입니다.

### SQL 기본 문법

**1. 데이터베이스 생성**

```sql
CREATE DATABASE database_name;
```

**2. 테이블 생성**

```sql
CREATE TABLE table_name (
    column1 datatype1 constraints,
    column2 datatype2 constraints,
    ...
);
```

**3. 데이터 삽입**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**4. 데이터 조회**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**5. 데이터 수정**

```sql
UPDATE table_name
SET column1 = new_value1, column2 = new_value2, ...
WHERE condition;
```

**6. 데이터 삭제**

```sql
DELETE FROM table_name
WHERE condition;
```

### SQL 예제: 학생 데이터베이스

**1. 데이터베이스 생성**

```sql
CREATE DATABASE school_db;
```

**2. 데이터베이스 사용**

```sql
USE school_db;
```

**3. 학생 정보 테이블 생성**

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);
```

**4. 학생 정보 삽입**

```sql
INSERT INTO students (id, name, age, gender)
VALUES (1, 'Alice', 20, 'Female'),
       (2, 'Bob', 22, 'Male'),
       (3, 'Charlie', 21, 'Male');
```

**5. 학생 정보 조회**

```sql
SELECT * FROM students;
```

**6. 학생 정보 수정**

```sql
UPDATE students
SET age = 23
WHERE id = 2;
```

**7. 학생 정보 삭제**

```sql
DELETE FROM students
WHERE id = 3;
```

---

## 7-2. SQLite 또는 MySQL 사용

### SQLite 예제

SQLite는 별도의 서버가 필요없는 경량 데이터베이스로, 파이썬에 기본적으로 내장되어 있습니다.

```python
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('school_db.sqlite')

# 커서 생성
cursor = conn.cursor()

# 학생 정보를 담을 테이블 생성
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    gender TEXT
)
''')

# 학생 정보 삽입
students_data = [
    (1, 'Alice', 20, 'Female'),
    (2, 'Bob', 22, 'Male'),
    (3, 'Charlie', 21, 'Male')
]

cursor.executemany('INSERT INTO students (id, name, age, gender) VALUES (?, ?, ?, ?)', students_data)

# 학생 정보 조회
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

# 학생 정보 수정
cursor.execute('UPDATE students SET age = ? WHERE id = ?', (23, 2))

# 학생 정보 삭제
cursor.execute('DELETE FROM students WHERE id = ?', (3,))

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()
```

### MySQL 예제

**1. MySQL Connector 설치**

```bash
pip install mysql-connector-python
```

**2. MySQL 연결 및 사용**

```python
import mysql.connector

# MySQL 서버와 연결
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='school_db'
)

# 커서 생성
cursor = conn.cursor()

# 학생 정보를 담을 테이블 생성
cursor.execute('''
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
)
''')

# 학생 정보 삽입
students_data = [
    (1, 'Alice', 20, 'Female'),
    (2, 'Bob', 22, 'Male'),
    (3, 'Charlie', 21, 'Male')
]

cursor.executemany('INSERT INTO students (id, name, age, gender) VALUES (%s, %s, %s, %s)', students_data)

# 학생 정보 조회
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

# 학생 정보 수정
cursor.execute('UPDATE students SET age = %s WHERE id = %s', (23, 2))

# 학생 정보 삭제
cursor.execute('DELETE FROM students WHERE id = %s', (3,))

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()
```

---

## 7-3. 파이썬과 데이터베이스 연동

파이썬은 다양한 데이터베이스와 연동할 수 있는 라이브러리를 제공합니다.

### SQLite 연동 예제

```python
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# 커서 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# 데이터 삽입
cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")

# 데이터 조회
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()
```

### MySQL 연동 예제

```python
import mysql.connector

# MySQL 서버와 연결
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='example_db'
)

# 커서 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
''')

# 데이터 삽입
cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")

# 데이터 조회
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 변경사항 저장 및 연결 종료
conn.commit()
conn.close()
```

### 데이터베이스 연동 주요 메서드

- **connect()**: 데이터베이스에 연결
- **cursor()**: 커서 객체 생성
- **execute()**: SQL 쿼리 실행
- **executemany()**: 여러 데이터를 한 번에 삽입
- **fetchone()**: 한 행 가져오기
- **fetchall()**: 모든 행 가져오기
- **commit()**: 변경사항 저장
- **rollback()**: 변경사항 취소
- **close()**: 연결 종료

---

## 📝 정리

Section 7에서는 다음 내용을 다루었습니다:
- SQL 기본 문법 (CREATE, INSERT, SELECT, UPDATE, DELETE)
- SQLite 데이터베이스 사용법 (경량, 파일 기반, Python 내장)
- MySQL 데이터베이스 사용법 (서버 기반, mysql-connector-python)
- Python과 데이터베이스 연동 방법
- CRUD 작업 (Create, Read, Update, Delete)
- 커서, 커밋, 연결 종료 등 데이터베이스 작업의 기본 흐름

SQLite는 파일 기반의 경량 데이터베이스로 별도의 서버 설치가 필요하지 않으며, MySQL은 별도의 서버가 필요하지만 더 강력한 기능을 제공합니다. 데이터베이스를 활용하여 다양한 데이터 관리 및 처리를 수행할 수 있습니다.

