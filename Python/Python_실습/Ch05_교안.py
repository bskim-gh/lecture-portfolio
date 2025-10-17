"""
Ch05 - Python 함수와 모듈
=========================

주요 내용:
- 함수(Function) 정의 및 호출
- 함수 4가지 유형: 매개변수/리턴값 조합
- 디폴트 매개변수(default parameter)
- 가변 매개변수(*args)
- 다중 리턴값
- 람다 함수(lambda function)
- 함수를 변수에 저장
- 모듈(Module) 임포트
- 내장 함수(Built-in functions)
- time, math, random 모듈
- statistics 모듈
- 분산과 표준편차 계산
- 피타고라스 정리 함수
- 몬테카를로 시뮬레이션
- 함수 스코프(global, local, nonlocal)
- 일급 함수와 클로저(Closure)
- 획득자(getter)와 지정자(setter)
- 함수 장식자(Decorator)
- 재귀 함수(Recursive function)
"""

# ====================================
# 1. 함수 기본
# ====================================

# 함수: 일련의 코드로직을 모듈화한 코드블럭
def ft(x):
    y = 2 * x + 3
    return y


def f(x):
    y = x ** 2 + 2 * x + 3
    return y


# 함수 실행(호출)
rs1 = ft(1)
rs2 = ft(2)
rs3 = ft(3)
print("rs1 :", rs1)
print("rs2 :", rs2)
print("rs3 :", rs3)

print("f(1) :", f(1))
print("f(2) :", f(2))
print("f(3) :", f(3))


# ====================================
# 2. 함수 4가지 유형
# ====================================

# 함수유형(1) : 매개변수 O, 리턴값 O
def type1(x, y):
    z = x + y
    return z

r1 = type1(1, 2)
r2 = type1(2, 3)
print("r1 :", r1)
print("r2 :", r2)

# 함수유형(2) : 매개변수 O, 리턴값 X
def type2(items):
    tot = 0
    for item in items:
        tot += item

    print("items 합 :", tot)

type2([1, 2, 3, 4, 5])
type2((1, 3, 5, 7, 9))
type2((2, 4, 6, 8, 10))

# 함수유형(3) : 매개변수 X, 리턴값 O
def type3():
    tot = 0
    for i in range(11):
        tot += i

    return tot

result = type3()
print("result :", result)

# 함수유형(4) : 매개변수 X, 리턴값 X
def type4():
    result = type3()
    print("type4 result :", result)

type4()

# 사용자 정의함수 예
def s():
    print('인수가 없는 함수')
    print('userFunc1')

s()

def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z =', z)

userFunc2(2, 3)

def userFunc3(x, y):
    print('userFunc3')
    tot = x+y
    sub = x-y
    mul = x*y
    div = x/y

    return tot, sub, mul, div

t, s, m, d = userFunc3(10, 20)
print(t)
print(s)
print(m)
print(d)


# ====================================
# 3. 디폴트 매개변수
# ====================================

def hello(name="홍길동", age=21):
    print("이름 :", name)
    print("나이 :", age)

hello()
hello("김유신")
hello("김춘추", 25)


# ====================================
# 4. 가변 매개변수
# ====================================

def total(*scores):
    tot = 0
    for score in scores:
        tot += score

    return tot

r1 = total(1)
r2 = total(1, 2)
r3 = total(1, 2, 3)

print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)


# ====================================
# 5. 하나 이상의 리턴값
# ====================================

def sum_and_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2

    return y1, y2

rs1, rs2 = sum_and_multi(2, 3)
print("rs1 :", rs1)
print("rs2 :", rs2)


# ====================================
# 6. 변수에 저장하는 함수
# ====================================

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

var1 = plus
var2 = minus

res1 = var1(2, 3)
res2 = var2(2, 3)

print("res1 :", res1)
print("res2 :", res2)

cal_list = [plus, minus]
res3 = cal_list[0](3, 4)
res4 = cal_list[1](4, 6)

print("res3 :", res3)
print("res4 :", res4)


# ====================================
# 7. 람다 함수
# ====================================

adder = lambda x, y, z: x + y + z

result = adder(1, 2, 3)
print("result :", adder(1, 2, 3))

# 람다 함수 예
def Adder(x, y):
    add = x + y
    return add

print('add =', Adder(10, 20))
print('add =', (lambda x, y: x + y)(10, 20))


# ====================================
# 8. 내장 함수
# ====================================

import time
import math
import random

# time 함수
t1 = time.time()
print("t1 :", t1)

t2 = time.ctime()
print("t2 :", t2)

now = time.localtime(time.time())
year = time.strftime("%Y", now)
month = time.strftime("%m", now)
date = time.strftime("%d", now)
hour = time.strftime("%H", now)
min = time.strftime("%M", now)
sec = time.strftime("%S", now)

print("%s년 %s월 %s일" % (year, month, date))
print("%s시 %s분 %s초" % (hour, min, sec))

# abs 함수
r1 = abs(-2.5)
print("r1 :", r1)

# ceil 함수
r2 = math.ceil(1.2)
r3 = math.ceil(1.8)
print("r2 :", r2)
print("r3 :", r3)

# floor 함수
r4 = math.floor(1.2)
r5 = math.floor(1.8)
print("r4 :", r4)
print("r5 :", r5)

# round 함수
r6 = round(1.2)
r7 = round(1.8)
print("r6 :", r6)
print("r7 :", r7)

# random 함수
num1 = random.random()
print("num1 :", num1)

num2 = num1 * 10
print("num2 :", num2)

num3 = math.ceil(num2)
print("num3 :", num3)  # 1 ~ 10 사이의 정수

# 한번에 실행
result = math.ceil(random.random() * 45)
print("result :", result)


# ====================================
# 9. builtins 함수와 statistics 모듈
# ====================================

dataset = list(range(1, 6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

import statistics
from statistics import variance, stdev

print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))
print('표본 분산=', statistics.variance(dataset))
print('표본 표준편차=', statistics.stdev(dataset))


# ====================================
# 10. 분산과 표준편차 함수
# ====================================

from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

def Avg(data):
    avg = mean(data)
    return avg

print('산술평균 =', Avg(dataset))

def var_sd(data):
    avg = Avg(data)
    diff = [(d-avg)**2 for d in data]

    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)

    return var, sd

v, s = var_sd(dataset)
print(v)
print(s)


# ====================================
# 11. 피타고라스 정리 함수
# ====================================

def pytha(s, t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print('3변의 길이 :', a, b, c)

pytha(2, 1)


# ====================================
# 12. 몬테카를로 시뮬레이션
# ====================================

def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0, 1)
        if (r == 1):
            result.append(1)
        else:
            result.append(0)

    return result

print(coin(10))

def montaCoin(n):
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0]

    result = cnt / n

    return result

print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))


# ====================================
# 13. 함수 스코프
# ====================================

x = 50
def local_func(x):
    x += 50
local_func(x)
print('x =', x)

def global_func():
    global x
    x += 50

global_func()
print('x =', x)


# ====================================
# 14. 일급 함수와 클로저
# ====================================

def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b

b = a()
b()

data = list(range(1, 101))
def outer_func(data):
    dataSet = data
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)


# ====================================
# 15. 획득자(getter)와 지정자(setter)
# ====================================

def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value
    return getter, setter

getter, setter = main_func(100)

print('num =', getter())

setter(200)
print('num =', getter())


# ====================================
# 16. 함수 장식자(Decorator)
# ====================================

def wrap(a):
    def decorated():
        print('반가워요!')
        a()
        print('잘가요!')
    return decorated

@wrap
def hello():
    print('hi ~', "홍길동")

hello()


# ====================================
# 17. 재귀 함수
# ====================================

# 숫자 카운트
def Counter(n):
    if n == 0:
        return 0
    else:
        Counter(n-1)

print('n = 0 :', Counter(0))
Counter(5)

# 1~n 정수 누적합
def Adder(n):
    if n == 1:
        return 1
    else:
        result = n + Adder(n-1)

        print(n, end=' ')
        return result

print('n=1 :', Adder(1))
print('\nn=5 :', Adder(10))


# ====================================
# 18. 최대공약수 함수
# ====================================

def gcd(n1, n2):
    temp = 0

    if n1 < n2:
        temp = n1
    else:
        temp = n2

    while True:
        if n1 % temp == 0 and n2 % temp == 0:
            break

        temp -= 1

    return temp

print("1과 5의 최대공약수 :", gcd(1, 5))
print("2과 6의 최대공약수 :", gcd(2, 6))
print("6과 9의 최대공약수 :", gcd(6, 9))
print("18과 12의 최대공약수 :", gcd(18, 12))
print("60과 24의 최대공약수 :", gcd(60, 24))


# ====================================
# 19. 구구단 함수
# ====================================

def gugudan(x):
    print("\n---- %d단 ----" % x)
    for a in range(1, 10):
        print("%d * %d = %d" % (x, a, x * a))


for i in range(2, 10):
    gugudan(i)

