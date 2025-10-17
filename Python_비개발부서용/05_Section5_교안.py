# ========================================
# Section 5: 클래스
# ========================================
# 학습 내용:
# - 클래스와 인스턴스 개념
# - self 이해
# - 클래스 변수 vs 인스턴스 변수
# - 상속 (Inheritance)
# - 다중 상속
# ========================================

# ========================================
# 5-1. Self, 클래스, 인스턴스 변수
# ========================================

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 예제1

class UserInfo:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Name: " + self.name)

    def __del__(self):
        print("Instance removed!")


user1 = UserInfo("Kim")
user2 = UserInfo("Park")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__)
print('user2 : ', user2.__dict__)

print(user1.name)


# 예제2
# self의 이해

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()
print(id(f))
f.function2()
print(SelfTest.function1())


# 예제3
# 클래스 변수 , 인스턴스 변수

class Warehouse:
    stock_num = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__)

print(user1.stock_num)
print(user2.stock_num)


# ========================================
# 5-2. 상속, 다중상속
# ========================================

# 예제1
# 상속 기본
# 슈퍼클래스 및 서브클래스 -> 모든 속성, 메소드 사용 가능


class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show" Method!'


class BmwCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


class BenzCar(Car):
    """Sub Class"""

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show(self):
        super().show()
        return 'Car Info : %s %s %s' % (self.car_name, self.color,self.type)

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)
print(model1.type)
print(model1.car_name)
print(model1.show())
print(model1.show_model())

# Method Overriding
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())

# Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance Info
print('Inheritance Info : ', BmwCar.mro())
print('Inheritance Info : ', BenzCar.mro())


# 예제2
# 다중 상속
class X():
    pass


class Y():
    pass


class Z():
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print(A.mro())

