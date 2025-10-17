# Section 4: 고급 클래스 기능
# 특수 메서드, 연산자 오버로딩, 클래스 메서드, 정적 메서드

print("=" * 50)
print("Section 4: 고급 클래스 기능")
print("=" * 50)

# =============================================================================
# 1. 생성자와 소멸자, 참조 카운트
# =============================================================================
print("\n1. 생성자와 소멸자, 참조 카운트")
print("-" * 30)

class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
d_copy = d
del d_copy 
del d

# =============================================================================
# 2. 연산자 오버로딩
# =============================================================================
print("\n2. 연산자 오버로딩")
print("-" * 30)

#연산자 오버라이드 
class NumBox:
    def __init__(self, num):
        self.Num = num
    
    def __add__(self, num):
        self.Num += num
    
    def __sub__(self, num):
        self.Num -= num

#인스턴스 생성
n = NumBox(40)
n + 100 
print("덧셈 후:", n.Num)
n - 110 
print("뺄셈 후:", n.Num)

# =============================================================================
# 3. 클래스 메서드
# =============================================================================
print("\n3. 클래스 메서드")
print("-" * 30)

class CoeffVar(object):
    coefficient = 1 
    
    @classmethod
    def mul(cls, fact):
        return cls.coefficient * fact 

#파생형식을 정의
class MulFive(CoeffVar):
    coefficient = 5 

x = MulFive.mul(4)
print("클래스 메서드 결과:", x)

# =============================================================================
# 4. 정적 메서드
# =============================================================================
print("\n4. 정적 메서드")
print("-" * 30)

class MyCalc(object):
    @staticmethod
    def my_add(x, y):
        return x + y

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5, 7)
print("정적 메서드 결과:", a)

# =============================================================================
# 5. 메모리 관리
# =============================================================================
print("\n5. 메모리 관리")
print("-" * 30)

class MyClass:
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    
    def __del__(self):
        print("Instance is deleted!")

d = MyClass(5)
#del d 

print("코드 실행 종료")

# =============================================================================
# 6. 메모리 구조 분석
# =============================================================================
print("\n6. 메모리 구조 분석")
print("-" * 30)

class SuperClass:
    def __init__(self):
        self.x = 10 
    
    def printX(self):
        print(self.x)

class SubClass(SuperClass):
    def __init__(self):
        self.y = 20
    
    def printY(self):
        print(self.y)

s = SubClass()
s.a = 30 
print("SuperClass:", SuperClass.__dict__)
print("SubClass:", SubClass.__dict__)
print("s:", s.__dict__)

print("\n" + "=" * 50)
print("Section 4 완료!")
print("=" * 50)
