# Section 1: Python 기초 - 환경 설정 및 기본 문법

## 📚 학습 목표
- Python의 특징과 활용 분야 이해
- Anaconda를 통한 Python 개발 환경 설정
- 변수, 자료형, 연산자의 기본 개념 숙지
- 조건문과 반복문을 활용한 흐름 제어
- 함수와 모듈을 통한 코드 재사용

---

## 1-1. 파이썬 소개와 설치

### 파이썬의 특징

파이썬은 배우기 쉽고 간결한 문법으로 인기 있는 프로그래밍 언어입니다. 파이썬은 광범위한 분야에서 활용되며, 데이터 분석, 웹 개발, 인공지능, 자동화 등 다양한 용도로 사용됩니다.

**1. 쉽고 배우기 쉬운 문법:**
- 파이썬은 직관적이고 간결한 문법으로 쉽게 읽고 쓸 수 있습니다. 이로 인해 프로그래밍을 처음 접하는 사람들도 빠르게 배울 수 있습니다.

**2. 다양한 용도로 활용:**
- 파이썬은 다양한 분야에서 활용됩니다. 데이터 과학, 머신 러닝, 웹 개발, 자동화, 게임 개발, 네트워크 프로그래밍 등 다양한 작업을 지원합니다.

**3. 큰 커뮤니티와 라이브러리 지원:**
- 파이썬은 커뮤니티가 활발하며, 많은 개발자들이 사용하고 있습니다. 이로 인해 다양한 라이브러리와 모듈을 활용할 수 있어 높은 생산성을 얻을 수 있습니다.

**4. 플랫폼 독립성:**
- 파이썬은 여러 플랫폼(Windows, macOS, Linux 등)에서 동일한 코드를 실행할 수 있습니다.

**5. 인공지능과 빅데이터 분야에서 강력한 지원:**
- 머신 러닝, 딥 러닝, 데이터 분석 등의 분야에서 파이썬은 풍부한 라이브러리와 프레임워크를 제공하여 최신 기술을 쉽게 활용할 수 있습니다.

**6. Jupyter Notebook 지원:**
- Jupyter Notebook을 사용하여 코드와 문서, 시각화, 수식 등을 통합하여 인터랙티브한 환경에서 개발하고 공유할 수 있습니다.

### 아나콘다(Anaconda) 설치

아나콘다는 데이터 과학과 머신 러닝을 위한 파이썬 배포판으로, 다양한 라이브러리와 툴을 포함하고 있어 데이터 분석 및 개발을 더욱 편리하게 할 수 있습니다.

**1. 아나콘다 소개**
- 아나콘다는 파이썬 데이터 과학 생태계를 위한 배포판으로, 다양한 라이브러리와 패키지를 포함하여 편리한 개발 환경을 제공합니다.
- 데이터 분석, 머신 러닝, 인공지능 등 다양한 분야에서 활용됩니다.
- 주요 특징으로는 가상 환경 관리, 패키지 관리, Jupyter Notebook 등이 있습니다.

**2. 아나콘다 설치 방법**

**2-1. 다운로드**
- 아나콘다 공식 웹사이트(https://www.anaconda.com/products/individual)에서 운영 체제(Windows, macOS, Linux)에 맞는 아나콘다 설치 파일을 다운로드합니다.

**2-2. 설치**
- 다운로드한 설치 파일을 실행합니다.
- 설치 창에서 언어, 설치 경로 등을 설정할 수 있습니다. 기본 설정을 따르는 것을 권장합니다.
- "Next"를 클릭하고 라이선스 동의에 동의한 후 "Next"를 클릭합니다.
- 설치 옵션 창에서 "Register Anaconda as the system Python 3.x"와 "Add Anaconda to my PATH environment variable" 옵션을 선택하고 "Install" 버튼을 클릭하여 설치를 진행합니다.

**2-3. 설치 완료**
- 설치가 완료되면 "Next"와 "Finish" 버튼을 차례로 클릭하여 마무리합니다.

**3. 아나콘다 실행**
- 아나콘다를 설치하면 Anaconda Navigator라는 툴이 설치됩니다. 이를 통해 아나콘다 환경을 관리하고 Jupyter Notebook 등을 실행할 수 있습니다.
- 시작 메뉴나 런처에서 Anaconda Navigator를 찾아 실행합니다.

**4. 가상 환경 생성과 사용 (옵션)**
- 아나콘다는 가상 환경을 지원하여 여러 프로젝트를 분리하여 관리할 수 있습니다.
- 가상 환경을 생성하려면 Anaconda Navigator의 "Environments" 탭에서 "Create" 버튼을 클릭합니다. 이름을 입력하고 원하는 파이썬 버전을 선택하여 가상 환경을 생성합니다.
- 생성한 가상 환경에서 필요한 라이브러리를 설치하고 사용할 수 있습니다.

---

## 1-2. 변수, 자료형, 연산자

### 1. 변수 (Variables)

변수는 값을 저장하는 데 사용되는 이름표입니다. 변수에는 숫자, 문자열, 객체 등 다양한 데이터를 저장할 수 있습니다. 파이썬은 동적 타이핑 언어로, 변수의 타입을 명시적으로 선언하지 않고 사용할 때 자동으로 결정됩니다.

**예제 코드:**
```python
# 변수에 값 할당
age = 30
name = "John Doe"
is_student = True

# 변수 출력
print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)
```

> ❓**Quiz**   
> 결과값이 `Name: John Doe` 가 출력되려면?

### 2. 자료형 (Data Types)

파이썬은 여러 가지 기본적인 자료형을 제공합니다. 주요 자료형으로는 숫자, 문자열, 리스트, 튜플, 딕셔너리, 집합 등이 있습니다.

**예제 코드:**
```python
# 숫자 (Numbers)
num_integer = 10
num_float = 3.14

# 문자열 (Strings)
name = "Alice"
message = 'Hello, how are you?'

# 리스트 (Lists)
fruits = ['apple', 'banana', 'orange']

# 튜플 (Tuples)
coordinates = (3, 5)

# 딕셔너리 (Dictionaries)
person = {'name': 'John', 'age': 25, 'is_student': True}

# 집합 (Sets)
unique_numbers = {1, 2, 3, 4, 5}
```

> ❓**Quiz**   
> 리스트에서 가장 마지막 값을 가져오려면?

### 3. 연산자 (Operators)

연산자는 값을 가지고 다른 값을 만들거나 연산하는 데 사용됩니다. 파이썬은 다양한 연산자를 지원합니다. 산술, 비교, 논리, 할당, 멤버십 연산자 등이 있습니다.

**예제 코드:**
```python
# 산술 연산자 (Arithmetic Operators)
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
remainder = a % b
exponentiation = a ** b

# 비교 연산자 (Comparison Operators)
is_equal = a == b
is_not_equal = a != b
is_greater_than = a > b
is_less_than = a < b
is_greater_than_or_equal = a >= b
is_less_than_or_equal = a <= b

# 논리 연산자 (Logical Operators)
logical_and = (a > 0) and (b < 5)
logical_or = (a > 0) or (b > 10)
logical_not = not (a == b)

# 할당 연산자 (Assignment Operators)
x = 5
x += 2  # x = x + 2와 같음
x *= 3  # x = x * 3과 같음

# 멤버십 연산자 (Membership Operators)
numbers = [1, 2, 3, 4, 5]
is_in_list = 3 in numbers
is_not_in_list = 6 not in numbers
```

---

## 1-3. 조건문과 반복문

### 1. 조건문 (Conditional Statements)

조건문은 주어진 조건의 참과 거짓에 따라 다른 코드 블록을 실행합니다. 파이썬에서는 if, elif(else if), else 키워드를 사용하여 조건문을 작성합니다.

**예제 코드:**
```python
# 예제 1: if 문
x = 10

if x > 5:
    print("x is greater than 5")

# 예제 2: if-else 문
num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 예제 3: if-elif-else 문
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```

### 2. 반복문 (Loops)

반복문은 동일한 코드를 여러 번 반복하여 실행하는 데 사용됩니다. 파이썬에서는 while과 for 두 가지 종류의 반복문이 있습니다.

**예제 코드:**
```python
# 예제 1: while 루프
count = 0

while count < 5:
    print("Count:", count)
    count += 1

# 예제 2: for 루프 (리스트 순회)
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)

# 예제 3: for 루프 (범위 순회)
for i in range(5):  # 0부터 4까지 반복
    print(i)

# 예제 4: for 루프 (딕셔너리 순회)
person = {'name': 'John', 'age': 30, 'occupation': 'engineer'}

for key, value in person.items():
    print(key, ":", value)
```

---

## 1-4. 함수와 모듈

### 1. 함수 (Functions)

함수는 특정 작업을 수행하는 코드 블록을 정의하는 것으로, 필요할 때마다 호출하여 사용할 수 있습니다. 함수를 사용하면 코드를 구조화하고 중복을 제거하여 코드의 가독성과 재사용성을 높일 수 있습니다.

**예제 코드:**
```python
# 예제 1: 함수 정의와 호출
def greet(name):
    """인사를 출력하는 함수"""
    print("Hello, " + name + "!")

greet("Alice")
greet("Bob")

# 예제 2: 함수 리턴 값
def add(a, b):
    """두 수를 더하여 결과를 반환하는 함수"""
    return a + b

result = add(5, 3)
print("결과:", result)

# 예제 3: 기본 인자 값
def greet_with_default(name="Guest"):
    """기본값을 가진 함수"""
    print("Hello, " + name + "!")

greet_with_default()
greet_with_default("John")
```

### 2. 모듈 (Modules)

모듈은 파이썬 코드를 구성하는 함수, 변수, 클래스 등을 모아놓은 파일입니다. 다른 파이썬 파일에서 이 모듈을 임포트하여 사용할 수 있습니다. 모듈을 사용하면 코드를 논리적으로 구분하여 관리하고 재사용성을 높일 수 있습니다.

**예제 코드:**

**greetings.py (모듈 파일)**
```python
def greet(name):
    """인사를 출력하는 함수"""
    print("Hello, " + name + "!")
```

**main.py (메인 파일)**
```python
# greetings.py 모듈 임포트
import greetings

greetings.greet("Alice")
greetings.greet("Bob")
```

### 🚀 문자열 처리 예제

**1. 문자열 붙이기와 포맷팅:**

```python
# 문자열 붙이기
str1 = "Hello"
str2 = "World"
result1 = str1 + " " + str2
print(result1)  # 출력: Hello World

# 문자열 포맷팅
name = "Alice"
age = 30
result2 = "My name is {} and I am {} years old.".format(name, age)
print(result2)  # 출력: My name is Alice and I am 30 years old.

# f-string을 사용한 문자열 포맷팅 (Python 3.6 이상)
result3 = f"My name is {name} and I am {age} years old."
print(result3)  # 출력: My name is Alice and I am 30 years old.
```

**2. 문자열 분리와 결합:**

```python
# 문자열 분리
text = "apple, banana, orange"
fruits = text.split(", ")
print(fruits)  # 출력: ['apple', 'banana', 'orange']

# 문자열 결합
fruits_str = ", ".join(fruits)
print(fruits_str)  # 출력: apple, banana, orange
```

**3. 문자열 대소문자 변경:**

```python
text = "Hello, World!"
lower_case = text.lower()
upper_case = text.upper()
print(lower_case)  # 출력: hello, world!
print(upper_case)  # 출력: HELLO, WORLD!
```

**4. 문자열 검색과 대체:**

```python
text = "I love Python programming."
substring = "Python"
if substring in text:
    print("Found 'Python' in the text.")
else:
    print("Not found.")

new_text = text.replace("Python", "Java")
print(new_text)  # 출력: I love Java programming.
```

**5. 공백 제거:**

```python
text = "   Hello, World!   "
trimmed_text = text.strip()
print(trimmed_text)  # 출력: Hello, World!
```

**6. 문자열 검증:**

```python
text1 = "12345"
text2 = "Hello"
text3 = "3.14"

is_digit1 = text1.isdigit()
is_digit2 = text2.isdigit()
is_float = text3.replace(".", "").isdigit()

print(is_digit1)  # 출력: True
print(is_digit2)  # 출력: False
print(is_float)   # 출력: True
```

> ❓**Quiz**   
> 변수값이 비어 있는지 확인 하는 함수를 만들려면?

### 🚀 수학 함수 예제

```python
import math

# 절대값 구하기
abs_result = abs(-10)
print("Absolute Value:", abs_result)  # 출력: 10

# 반올림하기
round_result = round(3.14159, 2)
print("Rounded Value:", round_result)  # 출력: 3.14

# 최댓값, 최솟값 구하기
max_value = max(1, 2, 3, 4, 5)
min_value = min(1, 2, 3, 4, 5)
print("Maximum Value:", max_value)  # 출력: 5
print("Minimum Value:", min_value)  # 출력: 1

# 거듭제곱 구하기
power_result = pow(2, 3)  # 2의 3제곱
print("Power:", power_result)  # 출력: 8

# 제곱근 구하기
sqrt_result = math.sqrt(25)
print("Square Root:", sqrt_result)  # 출력: 5.0

# 로그 구하기
log_result = math.log(100, 10)  # 밑이 10인 100의 로그
print("Logarithm:", log_result)  # 출력: 2.0

# 삼각함수
angle_in_radians = math.radians(45)  # 각도를 라디안으로 변환
sin_result = math.sin(angle_in_radians)
cos_result = math.cos(angle_in_radians)
tan_result = math.tan(angle_in_radians)
print("Sine:", sin_result)  # 출력: 0.7071067811865475
print("Cosine:", cos_result)  # 출력: 0.7071067811865476
print("Tangent:", tan_result)  # 출력: 0.9999999999999999
```

> ❓**Quiz**   
> `nums = [1,2,3,4]` 가 있을때 nums 의 평균값을 구하는 방법은?

### 🚀 다양한 함수 예제

**1. 함수 정의와 호출:**

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # 출력: Hello, Alice!
```

**2. 기본값을 갖는 함수:**

```python
def greet(name="Guest"):
    return f"Hello, {name}!"

message1 = greet("Alice")
message2 = greet()
print(message1)  # 출력: Hello, Alice!
print(message2)  # 출력: Hello, Guest!
```

**3. 가변 인자를 받는 함수:**

```python
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result1 = sum_numbers(1, 2, 3)
result2 = sum_numbers(10, 20, 30, 40)
print(result1)  # 출력: 6
print(result2)  # 출력: 100
```

**4. 딕셔너리 인자를 받는 함수:**

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# 출력:
# name: Alice
# age: 30
# city: New York
```

**5. 함수 내부 함수 (중첩 함수):**

```python
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

add_5 = outer_func(5)
result = add_5(3)
print(result)  # 출력: 8
```

**6. 람다 함수 (익명 함수):**

```python
double = lambda x: x * 2
result = double(5)
print(result)  # 출력: 10
```

**7. 재귀 함수 (팩토리얼 계산):**

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # 출력: 120
```

> ❓**Quiz**   
> 평균값을 구할수 있는 함수를 작성하려면?

---

## 📝 정리

Section 1에서는 Python의 기초적인 내용을 다루었습니다:
- Python의 특징과 Anaconda 설치 방법
- 변수, 자료형, 연산자의 기본 개념
- 조건문과 반복문을 활용한 흐름 제어
- 함수와 모듈을 통한 코드 재사용
- 문자열 처리 및 수학 함수 활용

이러한 기초를 바탕으로 다음 섹션에서는 더 복잡한 자료구조와 활용법을 배우게 됩니다.

