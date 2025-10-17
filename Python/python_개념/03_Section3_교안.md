# Section 3: 객체지향 프로그래밍 (OOP)

## 📚 학습 목표
- 클래스와 객체의 개념 이해
- 상속과 다형성을 통한 코드 재사용
- OOP를 활용한 실전 프로젝트 구현

---

## 3-1. 클래스와 객체 개념

객체 지향 프로그래밍(Object-Oriented Programming, OOP)은 현실 세계의 개념을 프로그래밍에 반영하는 개념입니다.

### 클래스 (Class)

- 클래스는 물체를 정의하는 설계도와 같습니다
- 어떤 물체(객체)가 가져야 할 속성(변수)과 행동(메서드)을 정의합니다
- `class` 키워드를 사용하여 정의하며, 클래스 이름은 관례적으로 대문자로 시작합니다
- 객체를 생성하기 위한 템플릿으로, 실체화되지 않은 추상적인 개념입니다

### 객체 (Object)

- 객체는 클래스의 인스턴스로, 실제로 생성된 것입니다
- 클래스를 기반으로 생성되어 클래스에서 정의한 속성과 메서드를 가집니다
- 객체는 각각 독립적인 상태를 가지며, 서로 다른 속성을 가질 수 있습니다

### 예제: 사람 클래스

```python
# 클래스 정의
class Person:
    # 생성자 (인스턴스 변수 초기화)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 메서드
    def greet(self):
        return f"Hello, my name is {self.name}."

    def show_age(self):
        return f"I am {self.age} years old."

# 객체 생성 (인스턴스화)
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 객체 사용 (메서드 호출)
print(person1.greet())  # Hello, my name is Alice.
print(person2.show_age())  # I am 25 years old.
```

> ❓**Quiz**   
> person.py 에 본문의 클래스가 있다고 했을때 main.py 에서 person.py 의 Person 클래스를 호출하려면?

---

## 3-2. 상속과 다형성

### 상속 (Inheritance)

상속은 객체 지향 프로그래밍(OOP)의 중요한 개념 중 하나로, 이미 존재하는 클래스를 기반으로 새로운 클래스를 만드는 것을 말합니다.

- 상속을 통해 기존 클래스의 속성과 메서드를 새로운 클래스에서 그대로 사용하거나 확장
- 하위 클래스(subclass)가 상위 클래스(superclass)의 특성을 물려받는 개념
- 이러한 관계를 "IS-A" 관계라고도 합니다

### 다형성 (Polymorphism)

다형성은 OOP에서 객체가 여러 가지 형태를 가질 수 있는 능력을 말합니다.

- 동일한 메서드를 호출하더라도 객체의 타입에 따라 다른 동작을 할 수 있도록 하는 특성
- **오버라이딩(Overriding):** 하위 클래스에서 상위 클래스의 메서드를 재정의
- **오버로딩(Overloading):** 하나의 메서드 이름으로 여러 형태의 인자를 받아 처리

### 예제: 동물 클래스 상속

```python
# 상위 클래스 (부모 클래스)
class Animal:
    def speak(self):
        return "Animal speaks."

# 하위 클래스 (자식 클래스)
class Dog(Animal):
    def speak(self):
        return "Dog barks."

class Cat(Animal):
    def speak(self):
        return "Cat meows."

# 다형성을 통한 메서드 호출
def animal_speak(animal):
    return animal.speak()

# 객체 생성
dog = Dog()
cat = Cat()

# 다형성을 활용하여 각 동물이 다르게 말하도록 함
print(animal_speak(dog))  # "Dog barks."
print(animal_speak(cat))  # "Cat meows."
```

---

## 3-3. OOP를 활용한 간단한 프로젝트

객체 지향 프로그래밍(OOP)를 활용한 '직원 관리 시스템'을 만들어보겠습니다.

### 프로젝트 설명

1. `Employee` 클래스를 정의 - 직원의 이름, 나이, 직급을 속성으로 가짐
2. `Employee` 클래스에 직원 정보를 출력하는 `display_info` 메서드 정의
3. `Company` 클래스를 정의 - 여러 직원 객체를 관리
4. `Company` 클래스에 직원 추가 및 전체 직원 정보 출력 메서드 정의

### 예제 코드

```python
# 직원 클래스
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Position: {self.position}")

# 회사 클래스
class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        print("Company Employees:")
        for employee in self.employees:
            employee.display_info()

# 직원 객체 생성
emp1 = Employee("Alice", 30, "Manager")
emp2 = Employee("Bob", 25, "Engineer")
emp3 = Employee("Charlie", 28, "Designer")

# 회사 객체 생성
company = Company()

# 직원 객체를 회사에 추가
company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(emp3)

# 회사에 있는 모든 직원 정보 출력
company.display_all_employees()
```

---

## 📝 정리

Section 3에서는 다음 내용을 다루었습니다:
- 클래스와 객체의 기본 개념
- `__init__` 생성자와 self 키워드
- 상속(Inheritance)과 IS-A 관계
- 다형성(Polymorphism)과 메서드 오버라이딩
- OOP를 활용한 직원 관리 시스템 구현

OOP를 사용하면 데이터와 관련 기능을 모듈화하여 코드를 더 유지보수하기 쉽고 재사용성이 높게 만들 수 있습니다.

