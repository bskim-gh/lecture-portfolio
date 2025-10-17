"""
Ch06 - Python 객체지향 프로그래밍
=================================

주요 내용:
- 클래스(Class) 정의 및 객체 생성
- 속성(Attribute)과 메서드(Method)
- 생성자(__init__)
- self 키워드
- 클래스 멤버와 인스턴스 멤버
- 클래스 메서드(@classmethod)
- 캡슐화(Encapsulation) 및 정보은닉
- private 변수(__변수명)
- getter/setter 메서드
- 상속(Inheritance)
- super() 함수
- 메서드 재정의(Method Overriding)
- 다형성(Polymorphism)
- 클래스 활용 예제: 은행계좌, 계산기, 사람, 학생
"""

# ====================================
# 1. 함수와 클래스 비교
# ====================================

# 함수 방식
def calc_func(a, b):
    x = a
    y = b

    def plus():
        p = x + y
        return p

    def minus():
        m = x - y
        return m
    return plus, minus

p, m = calc_func(10, 20)
print(p())
print(m())

# 클래스 방식
class calc_class:
    x = y = 0
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10, 20)

print(obj.plus())
print(obj.minus())


# ====================================
# 2. 클래스 기본 구조
# ====================================

class Car:
    cc = 0
    door = 0
    carType = None

    def __init__(self, cc, door, carType):
        self.cc = cc
        self.door = door
        self.carType = carType

    def display(self):
        print("자동차는 %dcc이고, 문짝은 %d개, 타입은 %s"
              % (self.cc, self.door, self.carType))

car1 = Car(2000, 4, '승용차')
car2 = Car(3000, 5, 'SUV')

car1.display()
car2.display()


# ====================================
# 3. 생성자
# ====================================

# 생성자를 통한 초기화
class multiply:
    x = y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = multiply(10, 20)
print('곱셈 =', obj.mul())

# 빈 생성자와 별도 초기화 메서드
class multiply2:
    x = y = 0

    def __init__(self):
        pass

    def data(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = multiply2()
obj.data(10, 20)
print('곱셈 =', obj.mul())


# ====================================
# 4. self 키워드
# ====================================

class multiply3:

    def data(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        result = self.x * self.y
        self.display(result)

    def display(self, result):
        print('곱셈 = %d' % (result))

obj = multiply3()
obj.data(10, 20)
obj.mul()


# ====================================
# 5. 클래스 멤버
# ====================================

class DatePro:
    content = "날짜 처리 클래스"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        print("%d.%d.%d" % (self.year, self.month, self.day))

    @classmethod
    def date_string(cls, dateStr):
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]

        print(f"{year}년 {month}월 {day}일")

date = DatePro(2021, 2, 25)
print(date.content)
print(date.year)
date.display()

print(DatePro.content)
DatePro.date_string('20210225')


# ====================================
# 6. 캡슐화(Encapsulation)
# ====================================

class Account:
    __balance = 0
    __accName = None
    __accNo = None

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    def deposit(self, money):
        if money < 0:
            print('금액확인')
            return
        self.__balance += money

    def withdraw(self, money):
        if self.__balance < money:
            print('잔액부족')
            return
        self.__balance -= money

acc = Account(1000, '홍길동', '125-152-4125-41')

bal = acc.getBalance()
print(bal)

acc.deposit(10000)
bal = acc.getBalance()
print(bal)


# ====================================
# 7. 계산기 클래스
# ====================================

class Calc:
    def plus(self, var1, var2):
        return var1 + var2

    def minus(self, var1, var2):
        return var1 - var2

    def multi(self, var1, var2):
        return var1 * var2

    def div(self, var1, var2):
        return var1 / var2

cal = Calc()

r1 = cal.plus(1, 2)
r2 = cal.minus(1, 2)
r3 = cal.multi(2, 3)
r4 = cal.div(4, 2)

print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)
print("r4 :", r4)


# ====================================
# 8. 사람 클래스
# ====================================

class Person:
    __name: None
    __age: 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def hello(self):
        print("-----------------")
        print("이름 :", self.__name)
        print("나이 :", self.__age)

kim = Person("김유신", 25)
kim.hello()

lee = Person("이순신", 35)
lee.hello()


# ====================================
# 9. 학생 클래스 (상속)
# ====================================

class Student(Person):

    __school = None
    __major = None

    def __init__(self, name, age, school, major):
        super().__init__(name, age)
        self.__school = school
        self.__major = major

    def hello(self):
        super().hello()
        print("학교 :", self.__school)
        print("전공 :", self.__major)

kim_student = Student("김유신", 25, "해강고등학교", "인문계")
kim_student.hello()


# ====================================
# 10. 직장인 학생 클래스 (다중 상속)
# ====================================

class SalaryStudent(Student):

    __company = None

    def __init__(self, name, age, school, major, company):
        super().__init__(name, age, school, major)
        self.__company = company

    def hello(self):
        super().hello()
        print("회사 :", self.__company)

lee_salary = SalaryStudent("이순신", 31, "부경대", "경영학", "삼성전자")
lee_salary.hello()


# ====================================
# 11. 은행 계좌 클래스
# ====================================

class BankAccount:
    __bank = None
    __id = None
    __name = None
    __balance = 0

    def __init__(self, bank, id, name, balance):
        self.__bank = bank
        self.__id = id
        self.__name = name
        self.__balance = balance

    def deposit(self, cash):
        self.__balance += cash

    def withdraw(self, cash):
        self.__balance -= cash

    def show(self):
        print("------------------------------")
        print("은행명 :", self.__bank)
        print("계좌번호 :", self.__id)
        print("입금주 :", self.__name)
        print("잔액 :", self.__balance)

kb = BankAccount("국민은행", "664121-04-454507", "장한결", 10000)

kb.deposit(20000)
kb.withdraw(3000)
kb.show()

wr = BankAccount("우리은행", "110-364-457545", "지대선", 20000)

wr.deposit(30000)
wr.withdraw(5000)
wr.show()


# ====================================
# 12. 증권 계좌 클래스 (상속)
# ====================================

class StockAccount(BankAccount):

    __stock = None
    __amount = 0
    __price = 0

    def __init__(self, bank, id, name, balance, stock, amount, price):
        super().__init__(bank, id, name, balance)
        self.__stock = stock
        self.__amount = amount
        self.__price = price

    def buy(self, stock, amount, price):
        self.__stock = stock
        self.__amount += amount
        self.__price = price

    def sell(self, stock, amount, price):
        self.__stock = stock
        self.__amount -= amount
        self.__price = price

    def show(self):
        super().show()
        print("주식종목 :", self.__stock)
        print("수량 :", self.__amount)
        print("가격 :", self.__price)

kb_stock = StockAccount("KB증권", "101-451-454521", "장한결", 50000, "삼성전자", 10, 40000)
kb_stock.deposit(50000)
kb_stock.withdraw(4000)
kb_stock.buy("삼성전자", 5, 45000)
kb_stock.sell("삼성전자", 5, 50000)
kb_stock.show()

