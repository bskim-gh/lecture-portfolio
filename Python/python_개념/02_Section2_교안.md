# Section 2: Python 자료구조와 파일 처리

## 📚 학습 목표
- 리스트, 튜플, 딕셔너리, 집합 등 Python의 핵심 자료구조 이해
- 리스트와 딕셔너리 컴프리헨션을 활용한 효율적인 코드 작성
- 파일 입출력과 다양한 인코딩 처리 방법 학습
- 대용량 파일 처리 기법 습득

---

## 2-1. 리스트, 튜플, 딕셔너리, 집합 등 파이썬의 자료 구조

파이썬은 다양한 자료 구조를 제공하여 데이터를 효율적으로 저장하고 처리할 수 있습니다.

### 1. 리스트 (Lists)

리스트는 여러 개의 항목을 순서대로 저장하는 자료 구조로, 대괄호 []로 묶어 표현됩니다. 리스트는 수정 가능하며, 다양한 타입의 데이터를 포함할 수 있습니다.

**예제 코드:**
```python
# 리스트 생성
fruits = ['apple', 'banana', 'orange', 'grape']

# 리스트의 요소에 접근
print(fruits[0])  # 'apple'
print(fruits[-1])  # 'grape'

# 리스트 슬라이싱
print(fruits[1:3])  # ['banana', 'orange']

# 리스트 요소 수정
fruits[0] = 'kiwi'
print(fruits)  # ['kiwi', 'banana', 'orange', 'grape']

# 리스트에 요소 추가
fruits.append('watermelon')
print(fruits)  # ['kiwi', 'banana', 'orange', 'grape', 'watermelon']

# 리스트 길이 확인
print(len(fruits))  # 5
```

> ❓**Quiz**   
> fruits 에서 orange가 None 이 되는 경우 None 을 제거 하는 방법은?

### 2. 튜플 (Tuples)

튜플은 리스트와 비슷하지만 수정이 불가능한 자료 구조입니다. 소괄호 ()로 묶어 표현되며, 읽기 전용 데이터를 저장하는 데 유용합니다.

**예제 코드:**
```python
# 튜플 생성
coordinates = (3, 5)

# 튜플 요소에 접근
print(coordinates[0])  # 3
print(coordinates[1])  # 5

# 튜플은 수정 불가능
coordinates[0] = 2  # TypeError: 'tuple' object does not support item assignment
```

### 3. 딕셔너리 (Dictionaries)

딕셔너리는 키-값 쌍으로 데이터를 저장하는 자료 구조입니다. 중괄호 {}로 묶어 표현되며, 키를 통해 값을 검색하는 데 사용됩니다.

**예제 코드:**
```python
# 딕셔너리 생성
person = {'name': 'John', 'age': 30, 'is_student': True}

# 딕셔너리 요소에 접근
print(person['name'])  # 'John'
print(person['age'])   # 30

# 딕셔너리 값 수정
person['age'] = 35
print(person)  # {'name': 'John', 'age': 35, 'is_student': True}

# 새로운 키-값 쌍 추가
person['occupation'] = 'engineer'
print(person)  # {'name': 'John', 'age': 35, 'is_student': True, 'occupation': 'engineer'}
```

### 4. 집합 (Sets)

집합은 중복을 허용하지 않는 요소들의 모음입니다. 중괄호 {}로 묶어 표현되며, 순서가 없는 자료 구조입니다.

**예제 코드:**
```python
# 집합 생성
unique_numbers = {1, 2, 3, 4, 5}

# 집합에 요소 추가
unique_numbers.add(6)
print(unique_numbers)  # {1, 2, 3, 4, 5, 6}

# 집합에 이미 존재하는 요소 추가 (중복은 허용되지 않음)
unique_numbers.add(3)
print(unique_numbers)  # {1, 2, 3, 4, 5, 6}

# 집합에서 요소 제거
unique_numbers.remove(2)
print(unique_numbers)  # {1, 3, 4, 5, 6}
```

---

## 2-2. 리스트와 딕셔너리 컴프리헨션

파이썬의 리스트 컴프리헨션과 딕셔너리 컴프리헨션은 간결하고 효율적인 방법으로 리스트와 딕셔너리를 생성하는 기법입니다.

### 1. 리스트 컴프리헨션

리스트 컴프리헨션은 기존 리스트를 이용하여 새로운 리스트를 생성하는 방법입니다.

**기본 예제:**
```python
# 리스트 컴프리헨션을 사용한 예제
numbers = [1, 2, 3, 4, 5]

# 원본 리스트의 제곱 값을 갖는 새로운 리스트 생성
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # [1, 4, 9, 16, 25]

# 원본 리스트에서 짝수만 필터링하여 새로운 리스트 생성
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4]
```

**조건부 리스트 컴프리헨션:**
```python
# 1부터 10까지의 숫자 중에서 홀수만 제곱한 새로운 리스트 생성
numbers = range(1, 11)
squared_odd_numbers = [x**2 for x in numbers if x % 2 != 0]
print(squared_odd_numbers)  # [1, 9, 25, 49, 81]

# 짝수는 제곱하고 홀수는 그대로 남기는 새로운 리스트 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x**2 if x % 2 == 0 else x for x in numbers]
print(result)  # [1, 4, 3, 16, 5, 36, 7, 64, 9]
```

### 2. 딕셔너리 컴프리헨션

딕셔너리 컴프리헨션은 for문을 사용하여 새로운 딕셔너리를 생성하는 방법입니다.

**예제 코드:**
```python
# 딕셔너리 컴프리헨션을 사용한 예제
fruits = ['apple', 'banana', 'orange']
prices = [1.0, 1.5, 2.0]

# 과일과 가격을 묶어 딕셔너리 생성
fruit_prices = {fruit: price for fruit, price in zip(fruits, prices)}
print(fruit_prices)  # {'apple': 1.0, 'banana': 1.5, 'orange': 2.0}
```

---

## 2-3. 파일 입출력

파이썬의 파일 입출력은 데이터를 파일에 쓰거나 파일에서 읽어오는 작업을 말합니다.

### 1. 파일 입출력 원리

파일 입출력은 크게 두 가지 방식으로 이루어집니다.

- **쓰기 (Writing):** 데이터를 파일에 기록하여 저장하는 것입니다.
- **읽기 (Reading):** 파일에 저장된 데이터를 읽어와서 프로그램에서 사용하는 것입니다.

### 2. 관련 함수와 메서드

- **open 함수:** 파일을 열고 파일 객체를 반환합니다.
- **close 메서드:** 파일 객체의 작업이 끝나면 파일을 닫아 리소스를 해제합니다.
- **read, readline, readlines 메서드:** 파일에서 데이터를 읽어올 때 사용합니다.
- **write 메서드:** 파일에 데이터를 쓸 때 사용합니다.

### 3. 파일 입출력 예제

```python
# 파일 쓰기 (Writing)
with open('example.txt', 'w') as file:
    file.write("Hello, world!\n")
    file.write("Python File I/O Example")

# 파일 읽기 (Reading)
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 파일 읽기 (줄 단위로)
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # 개행 문자(\n) 제거하여 출력
```

### 4. 인코딩 처리

```python
# euc-kr 로 인코딩 설정을 해서 파일 읽기
file_path = 'data.txt'

try:
    with open(file_path, 'r', encoding='euc-kr') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"파일 '{file_path}'이(가) 존재하지 않습니다.")
except UnicodeDecodeError:
    print(f"파일 '{file_path}'을(를) euc-kr로 읽을 수 없습니다.")
```

### 🚀 대용량 파일 읽기

2GB 이상의 큰 파일을 읽을 때는 `chunk` 단위로 파일을 분할하여 읽는 방법을 사용합니다.

**방법 1: read 메서드 사용**
```python
file_path = 'large_file.txt'
chunk_size = 1024  # 원하는 chunk 크기 (바이트 단위)

try:
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            # chunk 처리 작업 수행
except FileNotFoundError:
    print(f"파일 '{file_path}'이(가) 존재하지 않습니다.")
```

**방법 2: iter 함수 사용 (더 효율적)**
```python
file_path = 'large_file.txt'
chunk_size = 1024

try:
    with open(file_path, 'r') as file:
        for chunk in iter(lambda: file.read(chunk_size), ''):
            # chunk 처리 작업 수행
            pass
except FileNotFoundError:
    print(f"파일 '{file_path}'이(가) 존재하지 않습니다.")
```

---

## 📝 정리

Section 2에서는 다음 내용을 다루었습니다:
- 리스트, 튜플, 딕셔너리, 집합 등 Python의 핵심 자료구조
- 리스트와 딕셔너리 컴프리헨션을 활용한 효율적인 코드 작성
- 파일 입출력의 기본 (읽기, 쓰기, with 구문)
- 인코딩 처리 (UTF-8, EUC-KR)
- 대용량 파일을 chunk 단위로 처리하는 방법

이러한 자료구조와 파일 처리 기법을 잘 활용하면 다양한 데이터를 효율적으로 다룰 수 있습니다.

