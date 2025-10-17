"""
Ch02 - Python 변수와 자료구조
=============================

주요 내용:
- 변수(Variable) 선언 및 메모리 주소
- 자료형(Data Type): 정수, 실수, 논리형, 문자열
- 자료형 변환
- 연산자: 대입, 산술, 비교, 논리, 복합대입
- 문자열(String) 연산 및 처리: 인덱싱, 슬라이싱, 분리, 포맷
- 표준 입출력: input(), print()
- 자료구조: 리스트(List), 튜플(Tuple), 딕셔너리(Dictionary), 집합(Set)
- 문자열 처리 함수 및 이스케이프 문자
"""

# ====================================
# 1. 변수(Variable)
# ====================================

# 변수: 프로그래밍에서 데이터를 처리하기 위한 메모리 공간
var1 = 1
var2 = 2
result = var1 + var2
print('result:', result)

# 변수와 메모리 주소
var1 = "Hello Python"
print(var1)
print(id(var1))

var1 = 100
print(var1)
print(id(var1))

var2 = 150.25
print(var2)
print(id(var2))

var3 = True
print(var3)
print(id(var3))

# 예약어 확인
import keyword
python_keyword = keyword.kwlist
print(python_keyword)
print(type(python_keyword))
print(len(python_keyword))


# ====================================
# 2. 자료형(Data Type)
# ====================================

# 정수형(int)
var1 = 1
var2 = 2
var3 = -3
print('var1 :', var1)
print('var2 :', var2)
print('var3 :', var3)
print('var1 type:', type(var1))
print('var2 type:', type(var2))
print('var3 type:', type(var3))

# 실수형(float)
var4 = 0.4
var5 = 5.125
print('var4 :', var4)
print('var5 :', var5)
print('var4 type :', type(var4))
print('var5 type :', type(var5))

# 논리형(bool)
var6 = True
var7 = False
print('var6 :', var6)
print('var7 :', var7)
print('var6 type :', type(var6))
print('var7 type :', type(var7))

# 문자열(string)
var8 = 'A'
var9 = 'Apple'
var10 = "Apple"
var11 = '사과'
print('var8 :', var8)
print('var9 :', var9)
print('var10 :', var10)
print('var11 :', var11)
print('var8 type :', type(var8))
print('var9 type :', type(var9))
print('var10 type :', type(var10))
print('var11 type :', type(var11))

# 자료형 변환
# 실수 → 정수
a = int(10.5)
b = int(20.42)
add = a + b
print("add =", add)

# 정수 → 실수
a = float(10)
b = float(20)
add2 = a + b
print("add2 =", add2)

# 논리형 → 정수
print(int(True))
print(int(False))

# 문자형 → 정수
st = "10"
print(int(st)**2)


# ====================================
# 3. 연산자(Operator)
# ====================================

# 대입연산자
a = 1
b = c = d = 0
e, f, g = 7, True, 'Apple'
print('a :', a)
print('c :', c)
print('f :', f)
print('g :', g)

# 변수에 값 할당(=)
i = tot = 10
i += 1
tot += i
print(i, tot)

# 같은 줄에 중복 출력
print("출력1", end=", ")
print("출력2")

# 변수 교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)

# 패킹(packing) 할당
lst = [1, 2, 3, 4, 5, 6]
first, second, *third = lst
print(first, second, third)

*v3, v4, v5 = lst
print(v3, v4, v5)

# 산술연산자
num1 = 1
num2 = 2
num3, num4 = 3, 4

rs1 = num1 + num2
rs2 = num1 - num2
rs3 = num2 * num3
rs4 = num4 / num2
rs5 = 7 % 4  # MOD 함수와 동일(나머지값)
rs6 = num3 ** num2  # 거듭제곱

print('rs1 :', rs1)
print('rs2 :', rs2)
print('rs3 :', rs3)
print('rs4 :', rs4)
print('rs5 :', rs5)
print('rs6 :', rs6)

# 산술연산자 예제
num1 = 100
num2 = 20

add = num1 + num2
print("add :", add)  # 120

sub = num1 - num2
print("sub :", sub)  # 80

mul = num1 * num2
print("mul :", mul)  # 2000

div = num1 / num2
print("div :", div)  # 5
print(type(div))

mod = num1 % num2
print("mod :", mod)  # 0

squ = num1 ** num2
print("squ :", squ)

# 복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8
num5 += 1  # num5 = num5+1
num6 -= 2  # num6 = num6-2
num7 *= 3  # num7 = num7*3
num8 /= 4  # num8 = num8/4

print('num5 : ', num5)
print('num6 : ', num6)
print('num7 : ', num7)
print('num8 : ', num8)

# 비교연산자(관계연산자)
var1 = 1
var2 = 2

r1 = var1 > var2  # var1이 var2보다 크다.
r2 = var1 < var2  # var1이 var2보다 작다.
r3 = var1 >= var2  # var1이 var2보다 크거나 같다.
r4 = var1 <= var2  # var1이 var2보다 작거나 같다.
r5 = var1 == var2  # var1이 var2과 같다.
r6 = var1 != var2  # var1이 var2과 다르다.

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)
print('r5 :', r5)
print('r6 :', r6)

# 관계연산자 예제
num1, num2 = 100, 20

# 동등비교
bool_result = num1 == num2
print(bool_result)
bool_result = num1 != num2
print(bool_result)

# 크기비교
bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)

# 논리연산자
var3, var4 = 3, 4

res1 = var3 > 2 and var4 > 3
res2 = var3 > 2 and var4 > 4
res3 = var3 > 2 or var4 > 4
res4 = var3 > 4 or var4 > 5
res5 = not var3 > var4

print('res1 :', res1)
print('res2 :', res2)
print('res3 :', res3)
print('res4 :', res4)
print('res5 :', res5)

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <= 10
print(log_result)

# 두 관계식 중 하나라도 같은 지 판단
log_result = num1 >= 50 or num2 < 10
print(log_result)

log_result = num1 > 50
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)


# ====================================
# 4. 표준 입출력
# ====================================

# 표준 출력장치 예
# value 인수
print("value =", 10 + 20 + 30 + 40 + 50)

# sep 인수 : 값과 값을 특수문자로 구분
print("010", "1234", "5678", sep="-")

# end 인수
print("value :", 10, end=", ")
print("value :", 20)

# format() 함수 인수
print("원주율 =", format(3.14159, "8.3f"))
print("금액 =", format(10000, "10d"))
print("금액 =", format(125000, "3,d"))

# 양식문자 인수
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f" % (name, age, price))

# 외부 상수 출력
name = "장한결"
age = 29
price = 12.5678
print("이름 : {}, 나이 : {}, data = {}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data = {2}".format(age, name, price))

# format 축약형(f-string)
# uid = input("id input : ")
# query = f"select * from member where uid = {uid}"
# print(query)


# ====================================
# 5. 문자열(String) 처리
# ====================================

# 문자열 더하기
str1 = "Hello"
str2 = "Python"
result = str1 + str2
print("result : ", result)

# 문자열 곱하기
name = "홍길동"
print("name * 3:", name*3)

# 문자열 길이
msg = "Hello World"
print("msg 길이 :", len(msg))

# 문자열 인덱스
print("msg의 1번째 문자 :", msg[0])
print("msg의 7번째 문자 :", msg[6])
print("msg의 마지막 문자 :", msg[-1])

# 문자열 색인 예제
string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

# 문자열 연산
print("Python" + " program")
print("Python-" + str(3.7) + ".exe")
print("-"*30)

# 문자열 슬라이스
str = "hello korea"
print("str[0:6] :",str[0:6])
print("str[6:11] :",str[6:11])
print("str[:5] :",str[:5])
print("str[6:] :",str[6:])

# 슬라이싱 예제
oneLine = "this is one line string"
print("문자열 길이 :",len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])
print(oneLine[-11:])

# 문자열 분리
people = "김유신|김춘추|장보고|강감찬|이순신"
p1, p2, p3, p4, p5 = people.split("|")
print("p1 :",p1)
print("p2 :",p2)
print("p3 :",p3)
print("p4 :",p4)
print("p5 :",p5)

# 문자열 포맷
fstr1 = "%d월 %d일"
fstr2 = "%d월 %d일 %s요일"
print(fstr1 % (2, 16))
print(fstr2 % (2, 16, "화"))

# 문자열 유형
oneLine = "this is one line string"
print(oneLine)

multiLine = """this is
multi line
string"""
print(multiLine)

multiLine2 = "this is \nmulti line\nstring"
print(multiLine2)

# 문자열 처리 함수
oneLine = "this is one line string"
print("t 글자 수 : ", oneLine.count("t"))
print("t 글자 수 : ", oneLine.startswith("this"))
print("t 글자 수 : ", oneLine.startswith("that"))
print("t 글자 수 : ", oneLine.replace("this", "that"))

multiLine = "this is\nmulti line\nstring"
sent = multiLine.split("\n")
print("문장 :", sent)

words = oneLine.split(" ")
print("단어 :", words)

sent2 = ",".join(words)
print(sent2.replace(",", " "))

# 이스케이프 문자 차단
print("escape 문자 차단 ")
print("\n출력 이스케이프 문자 ")
print("\\n출력 이스케이프 문자 ")
print(r"\n출력 이스케이프 문자 ")

print("path =", "C:\Python\test")
print("path =", "C:\Python\\test")
print("path =", r"C:\Python\test")


# ====================================
# 6. 리스트(List)
# ====================================

# 리스트 생성
list1 = [1, 2, 3, 4, 5]
print("list1 type : ", type((list1)))
print("list1[0] : ", list1[0])
print("list1[2] : ", list1[2])
print("list1[4] : ", list1[4])

list2 = [5, 3.14, True, "홍길동"]
print("list2 type : ", type((list2)))
print("list2[0] : ", list2[1])
print("list2[2] : ", list2[2])
print("list2[4] : ", list2[3])

list3 = [[1, 2, 3],
         [True, False, True],
         ["김유신", "김춘추", "장보고"]]

print("list3[0][2] : ", list3[0][2])
print("list3[1][1] : ", list3[1][1])
print("list3[2][0] : ", list3[2][0])

# 리스트 덧셈
animal1 = ["사자", "호랑이", "코끼리"]
animal2 = ["기린", "곰"]
result = animal1 + animal2
print("result :", result)

# 리스트 수정, 삭제
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [7, 8]
print("numbers :", numbers)

numbers[2:3] = [8, 9]
print("numbers :", numbers)

numbers[1:3] = []
print("numbers :", numbers)

numbers.append(3)
print("numbers :", numbers)

del numbers[0:3]
print("numbers :", numbers)


# ====================================
# 7. 튜플(Tuple)
# ====================================

# Tuple 생성
tuple1 = (1, 2, 3, 4, 5)
tuple2 = 1, 2, 3, 4, 5
tuple3 = ("한국", "미국", "일본", "중국", "호주")

print("tuple1 type :", type(tuple1))
print("tuple2 type :", type(tuple2))
print("tuple3 type :", type(tuple3))

print("tuple1[0] :", tuple1[0])
print("tuple2[2] : %d" % tuple2[2])
print("tuple3[0] : %s" % tuple3[0])
print("tuple3[0] : %s" % tuple3[1])

# 튜플은 원소 수정, 삭제 안됨
# tuple1[0] = 1
# del tuple2[1]


# ====================================
# 8. 딕셔너리(Dictionary)
# ====================================

# 딕셔너리 생성
dic1 = {1: "C++", 2: "Java", 3: "Python"}
dic2 = {
    "KOR": "한국",
    "USA": "미국",
    "JPN": "일본",
    "CHN": "중국"
}
dic3 = {
    101: [1, 2, 3, 4, 5],
    102: ("한국", "미국", "일본", "중국", "호주"),
    103: {"p1": "김유신", "p2": "김춘추", "p3": "장보고" }
}

# 딕셔너리 데이터 출력
print("dic1 :", dic1)
print("dic1[1] :", dic1[1])
print("dic1[3] :", dic1[3])

print("dic2 :", dic2)
print('dic2["KOR"] :', dic2["KOR"])
print('dic2["USA"] :', dic2["USA"])

print("dic3 :", dic3)
print("dic3[101][2] :", dic3[101][2])
print("dic3[102][1] :", dic3[102][1])
print('dic3[103]["p%d"] :' % dic3[101][2], dic3[103]["p%d" % dic3[101][2]])

# 딕셔너리 응용
dic_list = [dic1, dic2, dic3]

r1 = dic_list[0][3]
r2 = dic_list[1]["KOR"]
r3 = dic_list[2][103]["p1"]

print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)


# ====================================
# 9. 집합(Set)
# ====================================

# 집합 생성
set1 = set([1, 2, 3, 4, 5])
set2 = set("Hello Korea")

print("set1 :", set1)
print("set2 :", set2)

# 집합 출력(리스트로 변환)
set1_list = list(set1)
set2_list = list(set2)

print("set1_list[0] :", set1_list[0])
print("set1_list[1] :", set1_list[1])
print("set1_list[2] :", set1_list[2])

print("set2_list[0] :", set2_list[0])
print("set2_list[1] :", set2_list[1])
print("set2_list[2] :", set2_list[2])

