# Section 2: 클래스와 객체 기초
# 클래스 정의, 객체 생성, 클래스 변수와 인스턴스 변수

print("=" * 50)
print("Section 2: 클래스와 객체 기초")
print("=" * 50)

# =============================================================================
# 1. 클래스 기본 구조
# =============================================================================
print("\n1. 클래스 기본 구조")
print("-" * 30)

class Person:
    #생성자 (초기화) 메서드
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
    
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p1.print()
p2 = Person()
p2.name = "현성환"
p2.print()

# 런타임(코드가 실행될 때) 변수를 추가할 수 있는 동적 형식의 언어
Person.title = "new title"
print("p1.title:", p1.title)
print("p2.title:", p2.title)
print("Person.title:", Person.title)

# =============================================================================
# 2. 클래스 변수와 인스턴스 변수
# =============================================================================
print("\n2. 클래스 변수와 인스턴스 변수")
print("-" * 30)

class Person:
    # 클래스에 소속된 데이터 공유하는 멤버변수
    num_person = 0
    
    #생성자 (초기화) 메서드
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
        Person.num_person += 1
    
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()

print("인스턴스 갯수: {0}".format(Person.num_person))

#특정 인스턴스에 변수를 추가
p1.age = 30
print("p1.age:", p1.age)
# print(p2.age)  # 에러: p2에는 age 속성이 없음

# =============================================================================
# 3. 계산기 클래스
# =============================================================================
print("\n3. 계산기 클래스")
print("-" * 30)

# 계산기 클래스 정의 
class Calc:
    def __init__(self):
        self.result = 0 
    
    def add(self, a, b):
        self.result = a + b
    
    def remove(self, a, b):
        self.result = a - b
    
    def multiple(self, a, b):
        self.result = a * b
    
    def divide(self, a, b):
        self.result = a / b 

#인스턴스 생성
calc = Calc()
calc.add(5, 3)
print("덧셈 결과:", calc.result)
calc.remove(5, 2)
print("뺄셈 결과:", calc.result)
calc.multiple(3, 4)
print("곱셈 결과:", calc.result)
calc.divide(5, 2)
print("나눗셈 결과:", calc.result)

# =============================================================================
# 4. 은행 계좌 클래스
# =============================================================================
print("\n4. 은행 계좌 클래스")
print("-" * 30)

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    
    def deposit(self, amount):
        self.__balance += amount 
    
    def withdraw(self, amount):
        self.__balance -= amount
    
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print("계좌 정보:", account1) 

# 동적으로 속성 추가 (권장하지 않음)
account1.__balance1 = 150000
print("동적 속성 추가:", account1.__balance1)
print("원래 계좌 정보:", account1)

# =============================================================================
# 5. self 키워드 중요성
# =============================================================================
print("\n5. self 키워드 중요성")
print("-" * 30)

#전역변수
str = "Not Class Member"

class GString:
    def __init__(self):
        # 인스턴스 멤버변수 초기화
        self.str = "" 
    
    def set(self, msg):
        self.str = msg
    
    def print(self):
        print(self.str)

# 인스턴스 생성
g = GString()
g.set("First Message")
g.print()

print("\n" + "=" * 50)
print("Section 2 완료!")
print("=" * 50)
