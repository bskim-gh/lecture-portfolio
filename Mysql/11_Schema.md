# MySQL 스키마 및 테이블 구조

## 🎯 학습 목표

이 섹션을 마치면 다음을 할 수 있게 됩니다:
- 데이터베이스 스키마의 개념과 중요성 이해
- 적절한 데이터 타입 선택하기
- PRIMARY KEY와 FOREIGN KEY의 차이와 역할 이해
- 테이블 간의 관계 설계하기
- CASCADE 옵션을 활용한 데이터 무결성 유지

---

## 💡 스키마란 무엇인가?

### 스키마의 정의

**스키마(Schema)**는 데이터베이스의 **설계도**입니다. 건물을 짓기 전에 설계도를 그리듯이, 데이터베이스를 만들기 전에 스키마를 설계합니다.

스키마는 다음과 같은 것들을 정의합니다:
- 📊 **테이블 구조**: 어떤 테이블들이 있는가?
- 📝 **컬럼 정의**: 각 테이블에 어떤 데이터를 저장하는가?
- 🔢 **데이터 타입**: 각 컬럼은 어떤 형식의 데이터를 저장하는가?
- 🔑 **키(Key)**: 어떤 컬럼이 고유 식별자인가?
- 🔗 **관계(Relationship)**: 테이블들은 서로 어떻게 연결되는가?
- ⚠️ **제약조건(Constraints)**: 어떤 규칙을 지켜야 하는가?

---

## 🏗️ 왜 스키마 설계가 중요한가?

### 1. 데이터 무결성 보장
스키마를 잘 설계하면 잘못된 데이터가 들어가는 것을 방지할 수 있습니다.

**예시:**
- 나이 컬럼을 음수로 저장하는 것을 방지
- 존재하지 않는 고객의 주문을 생성하는 것을 방지
- 필수 정보(이메일, 전화번호 등)가 누락되는 것을 방지

### 2. 데이터 중복 최소화
같은 데이터를 여러 곳에 저장하지 않고, 필요할 때 관계를 통해 가져옵니다.

**잘못된 설계 예시:**
```
주문 테이블에 고객의 이름, 주소, 전화번호를 모두 저장
→ 고객 정보가 변경되면 모든 주문 데이터를 수정해야 함
```

**올바른 설계 예시:**
```
고객 테이블에 고객 정보 저장
주문 테이블에는 고객 ID만 저장
→ 고객 정보가 변경되어도 고객 테이블만 수정
```

### 3. 검색 성능 향상
적절한 인덱스와 데이터 타입을 선택하면 쿼리 속도가 빨라집니다.

### 4. 유지보수 용이성
명확한 구조는 나중에 수정하거나 확장하기 쉽습니다.

---

## 📚 스키마 설계의 핵심 개념

### 1. 테이블 (Table)
엑셀의 시트와 비슷합니다. 관련된 데이터를 모아놓은 구조입니다.

**예시:**
- `customers` 테이블: 고객 정보
- `orders` 테이블: 주문 정보
- `products` 테이블: 제품 정보

### 2. 컬럼 (Column)
테이블의 각 항목입니다. 엑셀의 열(세로)과 같습니다.

**예시 (customers 테이블):**
- `customerNumber`: 고객 번호
- `customerName`: 고객 이름
- `email`: 이메일 주소
- `phone`: 전화번호

### 3. 행 (Row)
실제 데이터 한 건입니다. 엑셀의 행(가로)과 같습니다.

**예시:**
```
customerNumber: 103
customerName: 'Atelier graphique'
email: 'contact@atelier.fr'
phone: '40.32.2555'
```

### 4. 데이터 타입 (Data Type)
각 컬럼에 저장할 수 있는 데이터의 종류입니다.

**실생활 비유:**
- 나이는 숫자 → `INT`
- 이름은 문자 → `VARCHAR`
- 생일은 날짜 → `DATE`
- 가격은 금액 → `DECIMAL`

### 5. 키 (Key)
데이터를 식별하고 연결하는 특별한 컬럼입니다.

**실생활 비유:**
- **PRIMARY KEY (기본 키)**: 주민등록번호처럼 한 사람을 고유하게 식별
- **FOREIGN KEY (외래 키)**: 가족관계증명서의 부모 주민번호처럼 다른 사람을 참조

### 6. 관계 (Relationship)
테이블들이 서로 어떻게 연결되는지를 정의합니다.

**실생활 비유:**
- **일대다**: 한 명의 부모가 여러 자녀를 가질 수 있음 (부모 ↔ 자녀)
- **다대다**: 한 학생이 여러 과목을 수강하고, 한 과목에 여러 학생이 등록 (학생 ↔ 과목)
- **일대일**: 한 사람이 하나의 주민등록번호를 가짐 (사람 ↔ 주민번호)

---

## 🎓 스키마 학습 순서

이 문서는 다음 순서로 구성되어 있습니다:

```
1. 테이블 생성 방법 (CREATE TABLE)
   ↓
2. 데이터 타입 선택하기
   - 숫자형 (정수, 실수, 금액)
   - 문자형 (짧은 문자, 긴 문자)
   - 날짜/시간형
   ↓
3. 키(Key) 이해하기
   - PRIMARY KEY: 고유 식별자
   - FOREIGN KEY: 테이블 간 연결
   - UNIQUE KEY: 중복 방지
   - INDEX: 검색 속도 향상
   ↓
4. 테이블 관계 설계하기
   - 일대다 관계
   - 다대다 관계
   - 일대일 관계
   ↓
5. CASCADE 옵션 활용하기
   - 데이터 삭제/수정 시 자동 처리
   ↓
6. 실전 예제
   - 온라인 쇼핑몰 스키마 설계
```

---

## 🔍 시작하기 전에 알아두면 좋은 것들

### 용어 정리

| 용어 | 의미 | 실생활 비유 |
|------|------|-------------|
| **Schema** | 데이터베이스 구조 설계 | 건물 설계도 |
| **Table** | 데이터를 담는 그릇 | 엑셀 시트 |
| **Column** | 데이터 항목 | 엑셀 열(세로) |
| **Row** | 실제 데이터 | 엑셀 행(가로) |
| **Primary Key** | 고유 식별자 | 주민등록번호 |
| **Foreign Key** | 다른 테이블 참조 | 가족관계 참조번호 |
| **Constraint** | 데이터 규칙 | 교통 규칙 |
| **Index** | 검색 최적화 | 책의 색인 |

### 실무에서 자주 사용하는 명령어

```sql
-- 테이블 구조 확인
DESC table_name;

-- 테이블 목록 보기
SHOW TABLES;

-- 테이블 생성 구문 확인
SHOW CREATE TABLE table_name;
```

---

## 📋 테이블 생성 (CREATE TABLE)

### 기본 구문

```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    column3 datatype constraints,
    ...
    PRIMARY KEY (column_name),
    FOREIGN KEY (column_name) REFERENCES other_table(column_name)
);
```

### 실제 예제

```sql
CREATE TABLE employees (
    employeeNumber INT(11) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    extension VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    officeCode VARCHAR(10) NOT NULL,
    reportsTo INT(11) NULL,
    jobTitle VARCHAR(50) NOT NULL,
    PRIMARY KEY (employeeNumber),
    INDEX idx_reportsTo (reportsTo),
    FOREIGN KEY (reportsTo) REFERENCES employees(employeeNumber),
    FOREIGN KEY (officeCode) REFERENCES offices(officeCode)
) ENGINE = InnoDB;
```

---

## 🔤 컬럼 데이터 타입

### 1. 숫자형 (Numeric Types)

| 타입 | 설명 | 범위 | 사용 예시 |
|------|------|------|-----------|
| **TINYINT** | 매우 작은 정수 | -128 ~ 127 | 나이, 상태 코드 |
| **SMALLINT** | 작은 정수 | -32,768 ~ 32,767 | 소규모 카운트 |
| **INT** | 일반 정수 | -2,147,483,648 ~ 2,147,483,647 | ID, 수량 |
| **BIGINT** | 큰 정수 | 매우 큰 범위 | 대용량 ID |
| **DECIMAL(M,D)** | 고정 소수점 | M: 전체 자릿수, D: 소수 자릿수 | 가격, 금액 |
| **FLOAT** | 부동 소수점 (단정밀도) | 7자리 정밀도 | 과학 계산 |
| **DOUBLE** | 부동 소수점 (배정밀도) | 15자리 정밀도 | 정밀 계산 |

**예제:**
```sql
CREATE TABLE products (
    productId INT NOT NULL,
    quantity SMALLINT DEFAULT 0,
    price DECIMAL(10, 2),  -- 999,999,999.99까지 저장 가능
    weight DOUBLE,
    PRIMARY KEY (productId)
);
```

---

### 2. 문자형 (String Types)

| 타입 | 설명 | 최대 길이 | 사용 예시 |
|------|------|-----------|-----------|
| **CHAR(N)** | 고정 길이 문자열 | 255 | 국가 코드 (KR, US) |
| **VARCHAR(N)** | 가변 길이 문자열 | 65,535 | 이름, 주소, 이메일 |
| **TEXT** | 긴 텍스트 | 65,535 | 상품 설명 |
| **MEDIUMTEXT** | 더 긴 텍스트 | 16MB | 블로그 글 |
| **LONGTEXT** | 매우 긴 텍스트 | 4GB | 대용량 문서 |

**예제:**
```sql
CREATE TABLE users (
    userId INT NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    bio TEXT,
    countryCode CHAR(2),  -- 'KR', 'US' 등
    PRIMARY KEY (userId)
);
```

---

### 3. 날짜/시간형 (Date and Time Types)

| 타입 | 설명 | 형식 | 사용 예시 |
|------|------|------|-----------|
| **DATE** | 날짜만 | YYYY-MM-DD | 생일, 등록일 |
| **TIME** | 시간만 | HH:MM:SS | 근무 시작 시간 |
| **DATETIME** | 날짜 + 시간 | YYYY-MM-DD HH:MM:SS | 주문 시간 |
| **TIMESTAMP** | 타임스탬프 | YYYY-MM-DD HH:MM:SS | 수정 시간 (자동) |
| **YEAR** | 연도 | YYYY | 생산 연도 |

**예제:**
```sql
CREATE TABLE orders (
    orderId INT NOT NULL,
    orderDate DATE NOT NULL,
    orderTime TIME,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    updatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (orderId)
);
```

---

### 4. 기타 타입

| 타입 | 설명 | 사용 예시 |
|------|------|-----------|
| **ENUM** | 열거형 (선택 가능한 값 제한) | 'small', 'medium', 'large' |
| **SET** | 집합 (여러 값 선택 가능) | 'read', 'write', 'delete' |
| **BOOLEAN** | 참/거짓 (TINYINT(1)과 동일) | 활성화 여부 |
| **BLOB** | 바이너리 데이터 | 이미지, 파일 |
| **JSON** | JSON 형식 데이터 | 설정 데이터 |

**예제:**
```sql
CREATE TABLE products (
    productId INT NOT NULL,
    size ENUM('small', 'medium', 'large', 'x-large'),
    colors SET('red', 'blue', 'green', 'yellow'),
    isActive BOOLEAN DEFAULT TRUE,
    metadata JSON,
    PRIMARY KEY (productId)
);
```

---

## 🔑 키(Key) 유형

### 1. PRIMARY KEY (기본 키)

- **정의**: 테이블에서 각 행을 고유하게 식별하는 컬럼
- **특징**:
  - 테이블당 하나만 존재
  - NULL 값 불가
  - 중복 값 불가
  - 자동으로 인덱스 생성

**예제:**
```sql
CREATE TABLE customers (
    customerNumber INT NOT NULL,
    customerName VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    PRIMARY KEY (customerNumber)
);

-- 복합 기본 키 (여러 컬럼 조합)
CREATE TABLE orderDetails (
    orderNumber INT NOT NULL,
    productCode VARCHAR(15) NOT NULL,
    quantity INT,
    PRIMARY KEY (orderNumber, productCode)
);
```

---

### 2. FOREIGN KEY (외래 키)

- **정의**: 다른 테이블의 PRIMARY KEY를 참조하는 컬럼
- **목적**: 테이블 간의 관계를 정의하고 참조 무결성 유지
- **특징**:
  - 참조하는 테이블에 해당 값이 존재해야 함
  - NULL 허용 가능

**예제:**
```sql
CREATE TABLE orders (
    orderNumber INT NOT NULL,
    orderDate DATE NOT NULL,
    customerNumber INT NOT NULL,
    PRIMARY KEY (orderNumber),
    FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
);
```

---

### 3. UNIQUE KEY (고유 키)

- **정의**: 중복을 허용하지 않는 컬럼
- **특징**:
  - PRIMARY KEY와 유사하지만 NULL 허용 가능
  - 테이블에 여러 개 존재 가능

**예제:**
```sql
CREATE TABLE users (
    userId INT NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    PRIMARY KEY (userId),
    UNIQUE KEY (username),
    UNIQUE KEY (email)
);
```

---

### 4. INDEX (인덱스)

- **정의**: 데이터 검색 속도를 향상시키기 위한 구조
- **목적**: 쿼리 성능 최적화
- **특징**:
  - 검색은 빠르지만 삽입/수정/삭제는 느려질 수 있음
  - WHERE, JOIN, ORDER BY 절에서 자주 사용되는 컬럼에 생성

**예제:**
```sql
CREATE TABLE employees (
    employeeNumber INT NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    departmentId INT,
    PRIMARY KEY (employeeNumber),
    INDEX idx_name (lastName, firstName),  -- 복합 인덱스
    INDEX idx_department (departmentId),
    INDEX idx_email (email)
);
```

---

## 🔗 테이블 관계 (Relationships)

### 1. 일대다 (One-to-Many) 관계

가장 일반적인 관계. 한 테이블의 한 행이 다른 테이블의 여러 행과 연결됩니다.

**예제: 고객(customers) ↔ 주문(orders)**

```sql
-- 부모 테이블 (One)
CREATE TABLE customers (
    customerNumber INT NOT NULL,
    customerName VARCHAR(50) NOT NULL,
    PRIMARY KEY (customerNumber)
);

-- 자식 테이블 (Many)
CREATE TABLE orders (
    orderNumber INT NOT NULL,
    orderDate DATE NOT NULL,
    customerNumber INT NOT NULL,
    PRIMARY KEY (orderNumber),
    FOREIGN KEY (customerNumber) REFERENCES customers(customerNumber)
);
```

**설명**: 한 고객(customer)은 여러 개의 주문(orders)을 가질 수 있습니다.

---

### 2. 다대다 (Many-to-Many) 관계

중간 테이블(연결 테이블)을 사용하여 구현합니다.

**예제: 주문(orders) ↔ 제품(products)**

```sql
-- 테이블 1
CREATE TABLE orders (
    orderNumber INT NOT NULL,
    orderDate DATE NOT NULL,
    PRIMARY KEY (orderNumber)
);

-- 테이블 2
CREATE TABLE products (
    productCode VARCHAR(15) NOT NULL,
    productName VARCHAR(70) NOT NULL,
    PRIMARY KEY (productCode)
);

-- 중간 테이블 (Junction Table)
CREATE TABLE orderDetails (
    orderNumber INT NOT NULL,
    productCode VARCHAR(15) NOT NULL,
    quantity INT NOT NULL,
    priceEach DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (orderNumber, productCode),
    FOREIGN KEY (orderNumber) REFERENCES orders(orderNumber),
    FOREIGN KEY (productCode) REFERENCES products(productCode)
);
```

**설명**: 
- 한 주문(order)에는 여러 제품(products)이 포함될 수 있습니다.
- 한 제품(product)은 여러 주문(orders)에 포함될 수 있습니다.

---

### 3. 일대일 (One-to-One) 관계

한 테이블의 한 행이 다른 테이블의 정확히 한 행과 연결됩니다.

**예제: 사용자(users) ↔ 프로필(profiles)**

```sql
CREATE TABLE users (
    userId INT NOT NULL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (userId)
);

CREATE TABLE profiles (
    userId INT NOT NULL,
    bio TEXT,
    avatar VARCHAR(255),
    phone VARCHAR(20),
    PRIMARY KEY (userId),
    FOREIGN KEY (userId) REFERENCES users(userId)
);
```

**설명**: 한 사용자(user)는 하나의 프로필(profile)만 가집니다.

---

## ⚙️ CASCADE 옵션 (참조 동작)

FOREIGN KEY 제약조건에서 부모 테이블의 데이터가 변경되거나 삭제될 때 자식 테이블에서 어떻게 처리할지 정의합니다.

### CASCADE 옵션 종류

| 옵션 | 설명 |
|------|------|
| **ON DELETE CASCADE** | 부모 행 삭제 시 자식 행도 함께 삭제 |
| **ON DELETE SET NULL** | 부모 행 삭제 시 자식의 외래 키를 NULL로 설정 |
| **ON DELETE RESTRICT** | 자식 행이 존재하면 부모 행 삭제 불가 (기본값) |
| **ON DELETE NO ACTION** | RESTRICT와 유사 |
| **ON UPDATE CASCADE** | 부모 행의 키 값 변경 시 자식 행도 함께 변경 |
| **ON UPDATE SET NULL** | 부모 행의 키 값 변경 시 자식의 외래 키를 NULL로 설정 |
| **ON UPDATE RESTRICT** | 자식 행이 존재하면 부모 행 키 값 변경 불가 |

---

### CASCADE 예제

#### 1. ON DELETE CASCADE

```sql
CREATE TABLE departments (
    departmentId INT NOT NULL,
    departmentName VARCHAR(50) NOT NULL,
    PRIMARY KEY (departmentId)
);

CREATE TABLE employees (
    employeeId INT NOT NULL,
    employeeName VARCHAR(50) NOT NULL,
    departmentId INT,
    PRIMARY KEY (employeeId),
    FOREIGN KEY (departmentId) 
        REFERENCES departments(departmentId)
        ON DELETE CASCADE  -- 부서 삭제 시 해당 부서의 직원도 함께 삭제
);
```

**동작:**
```sql
-- 부서 삭제
DELETE FROM departments WHERE departmentId = 10;

-- 자동으로 해당 부서의 모든 직원도 삭제됨
```

---

#### 2. ON DELETE SET NULL

```sql
CREATE TABLE employees (
    employeeId INT NOT NULL,
    employeeName VARCHAR(50) NOT NULL,
    managerId INT,
    PRIMARY KEY (employeeId),
    FOREIGN KEY (managerId) 
        REFERENCES employees(employeeId)
        ON DELETE SET NULL  -- 상사 삭제 시 부하직원의 managerId를 NULL로 설정
);
```

**동작:**
```sql
-- 상사 직원 삭제
DELETE FROM employees WHERE employeeId = 100;

-- 해당 직원을 상사로 둔 직원들의 managerId가 NULL로 변경됨
```

---

#### 3. ON DELETE RESTRICT (기본값)

```sql
CREATE TABLE customers (
    customerNumber INT NOT NULL,
    customerName VARCHAR(50) NOT NULL,
    PRIMARY KEY (customerNumber)
);

CREATE TABLE orders (
    orderNumber INT NOT NULL,
    customerNumber INT NOT NULL,
    PRIMARY KEY (orderNumber),
    FOREIGN KEY (customerNumber) 
        REFERENCES customers(customerNumber)
        ON DELETE RESTRICT  -- 주문이 있는 고객은 삭제 불가
);
```

**동작:**
```sql
-- 주문이 있는 고객 삭제 시도
DELETE FROM customers WHERE customerNumber = 103;

-- 에러 발생: Cannot delete or update a parent row
-- 먼저 해당 고객의 주문을 삭제해야 함
```

---

#### 4. ON UPDATE CASCADE

```sql
CREATE TABLE customers (
    customerNumber INT NOT NULL,
    customerName VARCHAR(50) NOT NULL,
    PRIMARY KEY (customerNumber)
);

CREATE TABLE orders (
    orderNumber INT NOT NULL,
    customerNumber INT NOT NULL,
    PRIMARY KEY (orderNumber),
    FOREIGN KEY (customerNumber) 
        REFERENCES customers(customerNumber)
        ON UPDATE CASCADE  -- 고객 번호 변경 시 주문의 고객 번호도 함께 변경
);
```

**동작:**
```sql
-- 고객 번호 변경
UPDATE customers SET customerNumber = 999 WHERE customerNumber = 103;

-- 해당 고객의 모든 주문의 customerNumber도 999로 자동 변경됨
```

---

## 🏗️ 테이블 관계 설계 예제

### 실전 예제: 온라인 쇼핑몰 데이터베이스

```sql
-- 1. 고객 테이블
CREATE TABLE customers (
    customerNumber INT NOT NULL AUTO_INCREMENT,
    customerName VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    PRIMARY KEY (customerNumber)
) ENGINE = InnoDB;

-- 2. 제품 라인 테이블
CREATE TABLE productLines (
    productLine VARCHAR(50) NOT NULL,
    textDescription TEXT,
    PRIMARY KEY (productLine)
) ENGINE = InnoDB;

-- 3. 제품 테이블
CREATE TABLE products (
    productCode VARCHAR(15) NOT NULL,
    productName VARCHAR(70) NOT NULL,
    productLine VARCHAR(50) NOT NULL,
    quantityInStock SMALLINT NOT NULL,
    buyPrice DECIMAL(10, 2) NOT NULL,
    MSRP DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (productCode),
    INDEX idx_productLine (productLine),
    FOREIGN KEY (productLine) 
        REFERENCES productLines(productLine)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = InnoDB;

-- 4. 주문 테이블
CREATE TABLE orders (
    orderNumber INT NOT NULL AUTO_INCREMENT,
    orderDate DATE NOT NULL,
    requiredDate DATE NOT NULL,
    shippedDate DATE,
    status VARCHAR(15) NOT NULL,
    customerNumber INT NOT NULL,
    PRIMARY KEY (orderNumber),
    INDEX idx_customer (customerNumber),
    FOREIGN KEY (customerNumber) 
        REFERENCES customers(customerNumber)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = InnoDB;

-- 5. 주문 상세 테이블 (다대다 관계를 위한 중간 테이블)
CREATE TABLE orderDetails (
    orderNumber INT NOT NULL,
    productCode VARCHAR(15) NOT NULL,
    quantityOrdered INT NOT NULL,
    priceEach DECIMAL(10, 2) NOT NULL,
    orderLineNumber SMALLINT NOT NULL,
    PRIMARY KEY (orderNumber, productCode),
    INDEX idx_product (productCode),
    FOREIGN KEY (orderNumber) 
        REFERENCES orders(orderNumber)
        ON DELETE CASCADE      -- 주문 삭제 시 주문 상세도 함께 삭제
        ON UPDATE CASCADE,
    FOREIGN KEY (productCode) 
        REFERENCES products(productCode)
        ON DELETE RESTRICT     -- 제품이 주문에 포함되어 있으면 삭제 불가
        ON UPDATE CASCADE
) ENGINE = InnoDB;

-- 6. 결제 테이블
CREATE TABLE payments (
    customerNumber INT NOT NULL,
    checkNumber VARCHAR(50) NOT NULL,
    paymentDate DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (customerNumber, checkNumber),
    FOREIGN KEY (customerNumber) 
        REFERENCES customers(customerNumber)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE = InnoDB;
```

---

## 📊 테이블 관계도 (ERD)

```
customers (고객)
    ├─ 1:N → orders (주문)
    │           ├─ 1:N → orderDetails (주문 상세)
    │           │              └─ N:1 → products (제품)
    │           │                           └─ N:1 → productLines (제품 라인)
    │           │
    └─ 1:N → payments (결제)

관계 설명:
- customers ↔ orders: 일대다 (한 고객이 여러 주문)
- customers ↔ payments: 일대다 (한 고객이 여러 결제)
- orders ↔ orderDetails: 일대다 (한 주문에 여러 상품)
- orders ↔ products: 다대다 (orderDetails를 통한 연결)
- products ↔ productLines: 다대일 (여러 제품이 하나의 제품 라인)
```

---

## 🔍 스키마 조회 명령어

### 데이터베이스 목록 조회
```sql
SHOW DATABASES;
```

### 테이블 목록 조회
```sql
SHOW TABLES;
```

### 테이블 구조 조회
```sql
DESC table_name;
-- 또는
DESCRIBE table_name;
-- 또는
SHOW COLUMNS FROM table_name;
```

### 테이블 생성 구문 조회
```sql
SHOW CREATE TABLE table_name;
```

### 인덱스 조회
```sql
SHOW INDEX FROM table_name;
```

### 외래 키 조회
```sql
SELECT 
    CONSTRAINT_NAME,
    TABLE_NAME,
    COLUMN_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM 
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE
WHERE 
    TABLE_SCHEMA = 'database_name'
    AND REFERENCED_TABLE_NAME IS NOT NULL;
```

---

## 💡 스키마 설계 모범 사례

### 1. 명명 규칙
- **테이블명**: 복수형 사용 (`users`, `products`, `orders`)
- **컬럼명**: 명확하고 설명적인 이름 사용
- **PRIMARY KEY**: 보통 `id` 또는 `테이블명 + Number/Id`
- **FOREIGN KEY**: 참조 테이블명 + Id (`customerId`, `productId`)

### 2. 데이터 타입 선택
- 적절한 크기의 데이터 타입 선택 (저장 공간 최적화)
- 금액은 `DECIMAL` 사용 (부동소수점 오차 방지)
- 날짜/시간은 적절한 타입 선택

### 3. 제약 조건
- `NOT NULL`: 필수 컬럼에 지정
- `DEFAULT`: 기본값 설정
- `UNIQUE`: 중복 방지가 필요한 컬럼
- `CHECK`: 값의 범위 제한 (MySQL 8.0.16+)

### 4. 인덱스 전략
- PRIMARY KEY는 자동 인덱스
- WHERE 절에 자주 사용되는 컬럼에 인덱스 추가
- JOIN에 사용되는 FOREIGN KEY에 인덱스 추가
- 과도한 인덱스는 INSERT/UPDATE 성능 저하

### 5. CASCADE 사용 주의
- `ON DELETE CASCADE`: 신중하게 사용 (데이터 손실 가능)
- `ON DELETE RESTRICT`: 안전한 기본 옵션
- 비즈니스 로직에 맞는 옵션 선택

---

## 📝 실습 예제

### 예제 1: 학생 관리 시스템

```sql
-- 학과 테이블
CREATE TABLE departments (
    deptId INT NOT NULL AUTO_INCREMENT,
    deptName VARCHAR(50) NOT NULL,
    PRIMARY KEY (deptId)
);

-- 학생 테이블
CREATE TABLE students (
    studentId INT NOT NULL AUTO_INCREMENT,
    studentName VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    deptId INT,
    enrollmentDate DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (studentId),
    FOREIGN KEY (deptId) 
        REFERENCES departments(deptId)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- 과목 테이블
CREATE TABLE courses (
    courseId INT NOT NULL AUTO_INCREMENT,
    courseName VARCHAR(100) NOT NULL,
    credits INT NOT NULL,
    PRIMARY KEY (courseId)
);

-- 수강 신청 테이블 (다대다 관계)
CREATE TABLE enrollments (
    studentId INT NOT NULL,
    courseId INT NOT NULL,
    enrollmentDate DATE DEFAULT (CURRENT_DATE),
    grade VARCHAR(2),
    PRIMARY KEY (studentId, courseId),
    FOREIGN KEY (studentId) 
        REFERENCES students(studentId)
        ON DELETE CASCADE,
    FOREIGN KEY (courseId) 
        REFERENCES courses(courseId)
        ON DELETE CASCADE
);
```

---

## 요약

### 핵심 개념
1. **데이터 타입**: 숫자형, 문자형, 날짜/시간형 등 적절한 타입 선택
2. **PRIMARY KEY**: 테이블의 각 행을 고유하게 식별
3. **FOREIGN KEY**: 테이블 간의 관계를 정의하고 참조 무결성 유지
4. **INDEX**: 검색 성능 향상
5. **CASCADE**: 부모-자식 관계에서 데이터 변경 시 자동 처리 방식 정의

### 테이블 관계
- **일대다 (1:N)**: 가장 일반적, FOREIGN KEY로 구현
- **다대다 (N:M)**: 중간 테이블(Junction Table) 필요
- **일대일 (1:1)**: 데이터 분리가 필요한 경우

### CASCADE 옵션
- **DELETE CASCADE**: 부모 삭제 시 자식도 삭제
- **DELETE SET NULL**: 부모 삭제 시 자식의 FK를 NULL로
- **DELETE RESTRICT**: 자식이 있으면 부모 삭제 불가
- **UPDATE CASCADE**: 부모의 키 변경 시 자식도 변경

