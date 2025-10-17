# MySQL DISTINCT

## MySQL DISTINCT 절 소개

테이블에서 데이터를 조회할 때 중복된 행을 얻을 수 있습니다. 이러한 중복 행을 제거하려면 SELECT 문에서 DISTINCT 절을 사용합니다.

다음은 DISTINCT 절의 구문입니다:

```sql
SELECT DISTINCT
    select_list
FROM
    table_name
WHERE
    search_condition
ORDER BY
    sort_expression;
```

이 구문에서는 SELECT DISTINCT 키워드 다음에 고유한 값을 선택하려는 하나 이상의 컬럼을 지정합니다.

하나의 컬럼을 지정하면 DISTINCT 절은 해당 컬럼의 값을 기반으로 행의 고유성을 평가합니다.

그러나 두 개 이상의 컬럼을 지정하면 DISTINCT 절은 이러한 컬럼의 값을 사용하여 행의 고유성을 평가합니다.

DISTINCT 절이 포함된 SELECT 문을 실행할 때 MySQL은 FROM, WHERE, SELECT 절 다음, ORDER BY 절 이전에 DISTINCT 절을 평가합니다:

<img src="./images/distinct.png" alt="" />

## MySQL DISTINCT 절 예제

샘플 데이터베이스의 employees 테이블을 사용하겠습니다:

<img src="./images/employees.png" alt="" />

먼저, 다음 SELECT 문을 사용하여 employees 테이블에서 성을 선택합니다:

```sql
SELECT
    lastname
FROM
    employees
ORDER BY
    lastname;
```

출력에서 명확히 볼 수 있듯이 일부 직원은 동일한 성을 가지고 있습니다. 예: Bondur, Firrelli.

둘째, 다음과 같이 DISTINCT 절을 추가하여 고유한 성을 선택합니다:

```sql
SELECT
    DISTINCT lastname
FROM
    employees
ORDER BY
    lastname;
```

출력에서 명확히 볼 수 있듯이 DISTINCT 절은 결과 집합에서 중복된 성을 제거합니다.

## MySQL DISTINCT와 NULL 값

DISTINCT 절에 NULL 값이 있는 컬럼을 지정하면 DISTINCT 절은 하나의 NULL 값만 유지합니다. 모든 NULL 값이 동일하다고 간주하기 때문입니다.

예를 들어, customers 테이블의 state 컬럼은 NULL 값을 가지고 있습니다.

<img src="./images/customers.png" alt="customers table" />

DISTINCT 절을 사용하여 주(state)를 조회하면 고유한 주와 NULL이 다음과 같이 표시됩니다:

```sql
SELECT DISTINCT state
FROM customers;
```

## 여러 컬럼과 함께 MySQL DISTINCT 사용

DISTINCT 절에 여러 컬럼을 지정하면 DISTINCT 절은 이러한 컬럼의 값 조합을 사용하여 결과 집합에서 행의 고유성을 결정합니다.

예를 들어, customers 테이블에서 도시와 주의 고유한 조합을 얻으려면 다음 쿼리를 사용합니다:

```sql
SELECT DISTINCT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY
    state,
    city;
```

DISTINCT 절이 없으면 다음과 같이 주와 도시의 중복된 조합을 얻게 됩니다:

```sql
SELECT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY
    state ,
    city;
```

## 요약

- MySQL DISTINCT 절을 사용하여 SELECT 절에서 반환된 결과 집합에서 중복 행을 제거합니다.
