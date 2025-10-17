# MySQL AND 연산자

## MySQL AND 연산자 소개

MySQL에는 기본 제공 부울 타입이 없습니다. 대신 숫자 0을 FALSE로, 0이 아닌 값을 TRUE로 사용합니다.

AND 연산자는 두 개 이상의 부울 표현식을 결합하여 1, 0 또는 NULL을 반환하는 논리 연산자입니다:

```sql
A AND B
```

이 표현식에서 A와 B를 피연산자라고 합니다. 이들은 리터럴 값이거나 표현식일 수 있습니다.

논리 AND 연산자는 A와 B가 모두 0이 아니고 NULL이 아닌 경우 1을 반환합니다. 피연산자 중 하나가 0이면 0을 반환하고, 그렇지 않으면 NULL을 반환합니다.

논리 AND 연산자는 A와 B가 모두 0이 아니고 NULL이 아닌 경우 1을 반환합니다. 예를 들어:

```sql
SELECT 1 AND 1;
```

논리 AND 연산자는 A 또는 B가 0이거나 A와 B가 모두 0인 경우 0을 반환합니다:

```sql
SELECT 1 AND 0, 0 AND 1, 0 AND 0, 0 AND NULL;
```

논리 AND 연산자는 피연산자 중 하나가 0이 아니거나 두 피연산자가 모두 NULL인 경우 NULL을 반환합니다.

```sql
SELECT 1 AND NULL, NULL AND NULL;
```

다음 표는 참(true), 거짓(false), null을 결합할 때 AND 연산자의 결과를 보여줍니다.

|       | TRUE  | FALSE | NULL  |
| ----- | ----- | ----- | ----- |
| TRUE  | TRUE  | FALSE | NULL  |
| FALSE | FALSE | FALSE | FALSE |
| NULL  | NULL  | FALSE | NULL  |

실제로는 SELECT, UPDATE, DELETE 문의 WHERE 절에서 AND 연산자를 사용하여 조건을 형성합니다. 또한 INNER JOIN 및 LEFT JOIN 절의 조건에서도 AND 연산자를 사용할 수 있습니다.

AND 연산자를 포함하는 표현식을 평가할 때 MySQL은 결과를 결정할 수 있는 즉시 표현식의 나머지 부분 평가를 중단합니다.

이를 단락 평가(short-circuit evaluation)라고 합니다. 다시 말해, AND 연산자는 단락 평가됩니다. 예를 들어:

```sql
SELECT 1 = 0 AND 1 / 0 ;
```

이 예제에서 MySQL은 표현식 1 = 0 AND 1 / 0의 첫 번째 부분 1 = 0만 평가합니다.

표현식 1 = 0이 0을 반환하므로 MySQL은 전체 표현식의 결과를 결정할 수 있으며, 이는 0입니다.

따라서 MySQL은 표현식의 나머지 부분인 1/0을 평가할 필요가 없습니다. 평가했다면 0으로 나누기 오류가 발생했을 것입니다.

## MySQL AND 연산자 예제

데모를 위해 샘플 데이터베이스의 customers 테이블을 사용하겠습니다.

<img src="./images/customers.png" alt="" />

다음 문은 AND 연산자를 사용하여 미국 캘리포니아(CA)에 위치한 고객을 찾습니다:

```sql
SELECT
    customername,
    country,
    state
FROM
    customers
WHERE
    country = 'USA' AND
    state = 'CA';
```

AND 연산자를 사용하여 두 개 이상의 부울 표현식을 결합할 수 있습니다. 예를 들어, 다음 쿼리는 미국 캘리포니아에 위치하고 신용 한도가 100K보다 큰 고객을 반환합니다.

```sql
SELECT
    customername,
    country,
    state,
    creditlimit
FROM
    customers
WHERE
    country = 'USA' AND
    state = 'CA' AND
    creditlimit > 100000;
```

## 요약

- AND 연산자를 사용하여 두 개의 부울 표현식을 결합합니다. AND 연산자는 두 표현식이 모두 참일 때 true를 반환하고, 그렇지 않으면 false를 반환합니다.
- SELECT 문의 WHERE 절에서 조건을 형성하기 위해 AND 연산자를 사용합니다.
