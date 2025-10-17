# MySQL LIMIT

## MySQL LIMIT 절 소개

LIMIT 절은 SELECT 문에서 반환할 행 수를 제한하는 데 사용됩니다. LIMIT 절은 하나 또는 두 개의 인수를 허용합니다. 두 인수의 값은 모두 0 또는 양의 정수여야 합니다.

다음은 두 개의 인수가 있는 LIMIT 절 구문을 보여줍니다:

```sql
SELECT
    select_list
FROM
    table_name
LIMIT [offset,] row_count;
```

이 구문에서:

- offset은 반환할 첫 번째 행의 오프셋을 지정합니다. 첫 번째 행의 오프셋은 1이 아니라 0입니다.
- row_count는 반환할 최대 행 수를 지정합니다.

다음 그림은 LIMIT 절을 보여줍니다:
<img
  src="./images/limit.png"
  alt=""
/>

하나의 인수와 함께 LIMIT 절을 사용하면 MySQL은 이 인수를 사용하여 결과 집합의 첫 번째 행부터 반환할 최대 행 수를 결정합니다.

따라서 다음 두 절은 동일합니다:

```sql
LIMIT row_count;
```

그리고

```sql
LIMIT 0 , row_count;
```

위의 구문 외에도 MySQL은 다음 대체 LIMIT 절 구문을 제공합니다:

```sql
LIMIT row_count OFFSET offset
```

## LIMIT 및 ORDER BY 절

기본적으로 SELECT 문은 지정되지 않은 순서로 행을 반환합니다. LIMIT 절을 SELECT 문에 추가하면 반환되는 행을 예측할 수 없습니다.

따라서 LIMIT 절이 예상 출력을 반환하도록 하려면 항상 다음과 같이 ORDER BY 절과 함께 사용해야 합니다:

```sql
SELECT
    select_list
FROM
    table_name
ORDER BY
    sort_expression
LIMIT offset, row_count;
```

## MySQL LIMIT 절 예제

데모를 위해 샘플 데이터베이스의 customers 테이블을 사용하겠습니다.

<img
  src="./images/customers.png"
  alt=""
/>

### 1) 최고 또는 최저 행을 가져오기 위해 MySQL LIMIT 사용

이 문은 LIMIT 절을 사용하여 신용이 가장 높은 상위 5명의 고객을 가져옵니다:

```sql
SELECT
    customerNumber,
    customerName,
    creditLimit
FROM
    customers
ORDER BY creditLimit DESC
LIMIT 5;
```

이 예제에서:

- 먼저, ORDER BY 절은 고객을 신용이 높은 순에서 낮은 순으로 정렬합니다.
- 그런 다음, LIMIT 절은 처음 5개의 행을 반환합니다.

마찬가지로 이 예제는 LIMIT 절을 사용하여 신용이 가장 낮은 5명의 고객을 찾습니다:

```sql
SELECT
    customerNumber,
    customerName,
    creditLimit
FROM
    customers
ORDER BY creditLimit
LIMIT 5;
```

이 예제에서:

- 먼저, ORDER BY 절은 고객을 신용이 낮은 순에서 높은 순으로 정렬합니다.
- 그런 다음, LIMIT 절은 처음 5개의 행을 반환합니다.

신용이 0인 고객이 5명 이상 있으므로 위 쿼리의 결과는 일관되지 않은 결과로 이어질 수 있습니다.

이 문제를 해결하려면 ORDER BY 절에 더 많은 컬럼을 추가하여 행을 고유한 순서로 제한해야 합니다:

```sql
SELECT
    customerNumber,
    customerName,
    creditLimit
FROM
    customers
ORDER BY
    creditLimit,
    customerNumber
LIMIT 5;
```

### 2) 페이지네이션을 위해 MySQL LIMIT 절 사용

화면에 데이터를 표시할 때 행을 페이지로 나누는 경우가 많습니다. 각 페이지에는 10개 또는 20개와 같이 제한된 수의 행이 포함됩니다.

페이지 수를 계산하려면 전체 행을 페이지당 행 수로 나눕니다. 특정 페이지의 행을 가져오려면 LIMIT 절을 사용할 수 있습니다.

이 쿼리는 COUNT(\*) 집계 함수를 사용하여 customers 테이블에서 전체 행을 가져옵니다:

```sql
SELECT
    COUNT(*)
FROM
    customers;
```

각 페이지에 10개의 행이 있다고 가정하면 122명의 고객을 표시하려면 13개의 페이지가 필요합니다. 마지막 13번째 페이지에는 2개의 행만 포함됩니다.

이 쿼리는 LIMIT 절을 사용하여 고객 이름으로 정렬된 처음 10명의 고객이 포함된 페이지 1의 행을 가져옵니다:

```sql
SELECT
    customerNumber,
    customerName
FROM
    customers
ORDER BY customerName
LIMIT 10;
```

이 쿼리는 LIMIT 절을 사용하여 11 – 20행을 포함하는 두 번째 페이지의 행을 가져옵니다:

```sql
SELECT
    customerNumber,
    customerName
FROM
    customers
ORDER BY customerName
LIMIT 10, 10;
```

### 3) n번째로 높거나 낮은 값을 가져오기 위해 MySQL LIMIT 사용

n번째로 높거나 낮은 값을 가져오려면 다음 LIMIT 절을 사용합니다:

```sql
SELECT select_list
FROM table_name
ORDER BY sort_expression
LIMIT n-1, 1;
```

LIMIT n-1, 1 절은 n번째 행부터 시작하여 1개의 행을 반환합니다.

예를 들어, 다음은 두 번째로 높은 신용을 가진 고객을 찾습니다:

```sql
    SELECT
        customerName,
        creditLimit
    FROM
        customers
    ORDER BY
        creditLimit DESC
    LIMIT 1,1;
```

결과를 다시 확인해 보겠습니다. 이 쿼리는 신용이 높은 순에서 낮은 순으로 정렬된 모든 고객을 반환합니다:

```sql
SELECT
    customerName,
    creditLimit
FROM
    customers
ORDER BY
    creditLimit DESC;
```

출력에서 명확히 볼 수 있듯이 결과는 예상대로 정확했습니다.

## MySQL LIMIT & DISTINCT 절

DISTINCT 절과 함께 LIMIT 절을 사용하면 MySQL은 LIMIT 절에 지정된 고유 행 수를 찾는 즉시 검색을 중단합니다.

이 예제는 DISTINCT 절과 함께 LIMIT 절을 사용하여 customers 테이블의 처음 5개의 고유한 주를 반환합니다:

```sql
SELECT DISTINCT
    state
FROM
    customers
WHERE
    state IS NOT NULL
LIMIT 5;
```

## 요약

- MySQL LIMIT 절을 사용하여 SELECT 문에서 반환되는 행 수를 제한합니다.
