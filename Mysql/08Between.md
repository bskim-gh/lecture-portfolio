# MySQL BETWEEN

## BETWEEN 소개

BETWEEN 연산자는 값이 범위 내에 있는지 여부를 지정하는 논리 연산자입니다. 다음은 BETWEEN 연산자의 구문입니다:

```sql
value BETWEEN low AND high;
```

BETWEEN 연산자는 다음 조건에서 1을 반환합니다:

```sql
value >= low AND value <= high
```

그렇지 않으면 0을 반환합니다.

value, low 또는 high가 NULL이면 BETWEEN 연산자는 NULL을 반환합니다.

예를 들어, 다음 문은 15가 10과 20 사이에 있으므로 1을 반환합니다:

```sql
SELECT 15 BETWEEN 10 AND 20;
```

다음 예제는 15가 20과 30 사이에 없으므로 0을 반환합니다:

```sql
SELECT 15 BETWEEN 20 AND 30;
```

---

**_참고:_** MySQL은 1을 참으로, 0을 거짓으로 처리합니다.

---

### NOT BETWEEN

BETWEEN 연산자를 부정하려면 NOT 연산자를 사용합니다:

```sql
value NOT BETWEEN low AND high
```

NOT BETWEEN 연산자는 다음 조건에서 1을 반환합니다:

```sql
value < low OR value > high
```

그렇지 않으면 0을 반환합니다.

예를 들어, 다음 문은 15가 10과 20 사이에 있지 않다는 것이 참이 아니므로 0을 반환합니다:

```sql
SELECT 15 NOT BETWEEN 10 AND 20;
```

실제로는 SELECT, UPDATE, DELETE 문의 WHERE 절에서 BETWEEN 연산자를 사용합니다.

## MySQL BETWEEN 연산자 예제

BETWEEN 연산자 사용 예제를 연습해 보겠습니다.

### 1) 숫자와 함께 MySQL BETWEEN 사용 예제

샘플 데이터베이스의 다음 products 테이블을 참조하세요:

<img
  src="./images/products.png"
  alt=""
/>

다음 예제는 BETWEEN 연산자를 사용하여 구매 가격이 90에서 100 사이인 제품을 찾습니다:

```sql
SELECT
    productCode,
    productName,
    buyPrice
FROM
    products
WHERE
    buyPrice BETWEEN 90 AND 100;
```

이 쿼리는 BETWEEN 연산자 대신 크거나 같음(>=)과 작거나 같음(<=) 연산자를 사용하여 동일한 결과를 얻습니다:

```sql
SELECT
    productCode,
    productName,
    buyPrice
FROM
    products
WHERE
    buyPrice >= 90 AND buyPrice <= 100;
```

구매 가격이 $20에서 $100 사이가 아닌 제품을 찾으려면 다음과 같이 NOT BETWEEN 연산자를 사용합니다:

```sql
SELECT
    productCode,
    productName,
    buyPrice
FROM
    products
WHERE
    buyPrice NOT BETWEEN 20 AND 100;
```

다음과 같이 작음(<), 큼(>) 및 논리 연산자(AND)를 사용하여 위 쿼리를 다시 작성할 수 있습니다:

```sql
SELECT
    productCode,
    productName,
    buyPrice
FROM
    products
WHERE
    buyPrice < 20 OR buyPrice > 100;
```

### 2) 날짜와 함께 MySQL BETWEEN 연산자 사용 예제

다음 orders 테이블을 참조하세요:

<img
  src="./images/orders.png"
  alt=""
/>

값이 날짜 범위 내에 있는지 확인하려면 값을 명시적으로 DATE 타입으로 캐스팅해야 합니다.

예를 들어, 다음 문은 요청 날짜가 2003년 1월 1일부터 2003년 1월 31일 사이인 주문을 반환합니다:

```sql
SELECT
   orderNumber,
   requiredDate,
   status
FROM
   orders
WHERE
   requireddate BETWEEN
     CAST('2003-01-01' AS DATE) AND
     CAST('2003-01-31' AS DATE);
```

이 예제에서는 CAST()를 사용하여 리터럴 문자열 '2003-01-01'을 DATE 값으로 캐스팅합니다:

```sql
CAST('2003-01-01' AS DATE)
```

## 요약

- MySQL BETWEEN 연산자를 사용하여 값이 값 범위 내에 있는지 테스트합니다.
