# Section 1: Python 기초 문법
# 조건문, 반복문, 함수, 예외처리

print("=" * 50)
print("Section 1: Python 기초 문법")
print("=" * 50)

# =============================================================================
# 1. 조건문
# =============================================================================
print("\n1. 조건문 (if-elif-else)")
print("-" * 30)

score = int(input("점수를 입력 : "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"

print("등급은 ", grade)

# =============================================================================
# 2. 반복문 기초
# =============================================================================
print("\n2. 반복문 기초")
print("-" * 30)

# while 루프
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---for in루프---")
lst = [100, "apple", 3.14]
for item in lst:
    print(item, type(item))

# 딕셔너리로 값을 초기화 
d = {"apple":100, "kiwi":200}
for item in d.items():
    print(item)

print("---키만 출력---")
for k in d.keys():
    print(k)

print("---값만 출력---")
for v in d.values():
    print(v)

# 구구단 출력
print("---구구단 출력---")
for x in [2,3,4,5,6]:
    print("---{0}단 출력".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

# =============================================================================
# 3. break와 continue
# =============================================================================
print("\n3. break와 continue")
print("-" * 30)

# break 구문
print("---break구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for item in lst:
    if item > 5:
        break
    print("Item:{0}".format(item))

# continue 구문
print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

# range 함수와 리스트 컴프리헨션
print("---수열함수---")
result = list(range(10))
print(result)

result = list(range(1,11))
print(result)

years = list(range(2000,2022))
print(years)

# 수동으로 루프를 돌리는 경우
for i in range(5):
    print(i)

# 리스트 컴프리헨션
lst = list(range(1,11))
result2 = [i**2 for i in lst if i>5]
print("리스트 컴프리헨션:", result2)

tp = ("apple", "kiwi", "orange")
print([len(i) for i in tp])

# 딕셔너리 컴프리헨션
d = {100:"apple", 200:"orange", 300 : "kiwi"}
print([v.upper() for v in d.values()])

# =============================================================================
# 4. 함수 기본
# =============================================================================
print("\n4. 함수 기본")
print("-" * 30)

# 함수를 정의
def setValue(newValue):
    #함수 내부에서 초기화 하면 지역변수
    x = newValue
    print("함수 내부:", x)

# 함수를 호출
result = setValue(5)
print(result)

# 다중의 값을 리턴
def swap(x,y):
    return y,x

# 호출
result = swap(5,6)
print(result)
print(result[0], result[1])

# 교집합 문자를 리턴하는 함수
def union(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print("교집합:", union("HAM", "SPAM"))

# =============================================================================
# 5. 지역변수와 전역변수
# =============================================================================
print("\n5. 지역변수와 전역변수")
print("-" * 30)

def change(x):
    # 복사본을 지역변수로 만들기
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부 : ", x1)

# 함수를 호출
wordlist = ["j", "A", "M"]
#pass by reference
change(wordlist)
print("함수 호출 후 :", wordlist)

# 지역변수와 전역 변수 (이름 충돌)
x = 1
def func(a):
    return x+a

# 호출
print("전역변수 사용:", func(1))

def func2(a):
    x=2
    return x+a

#호출
print("지역변수 사용:", func2(1))
print("전역변수 x:", x)

# 전역변수를 읽기 + 쓰기 할 경우 불변형식이면 global 키워드 사용
g=1
print("전역변수 g ID:", id(g))
def testScope(a):
    global g
    g=2
    print("지역변수 g ID:", id(g))
    return g+a

#호출
print("testScope 결과:", testScope(1))
print("함수 호출 후 전역변수 g:", g)
print("전역변수 g ID:", id(g))

# =============================================================================
# 6. 가변인자와 람다 함수
# =============================================================================
print("\n6. 가변인자와 람다 함수")
print("-" * 30)

# 함수의 기본값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print("기본값 사용:", times())
print("첫 번째 인자만:", times(5))
print("두 인자 모두:", times(5,6))

#키워드 인자 방식으로 전달한다. 
def userURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL 

#호출
print("순서대로:", userURI("credu.com", "80"))
print("키워드 인자:", userURI(port="8080", server="credu.com"))

#가변인자는 입력되는 인자의 갯수가 가변적인 경우
#인자에 *를 붙이면 가변인자(내부에서 Tuple)
def union(*ar):
    #지역변수로 결과를 담을 리스트를 초기화 
    result = []
    #HAM(0) | EGG(1) ==> ar이라는 가변인자 
    for item in ar:
        #H(0) | A(1) | M(2)
        #E(0) | G(1) | G(2)
        for x in item:
            #x라는 글자가 포함되어 있지 않다면 추가 
            if x not in result:
                result.append(x)
    return result 

#호출
print("가변인자 2개:", union("HAM","EGG"))
print("가변인자 3개:", union("HAM","EGG","SPAM"))

#정의되지 않은 인자 처리(필수, 옵션도 섞여 있는 경우)
#내부에서 딕셔너리(dict)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL

#호출
print("키워드 가변인자:", userURIBuilder("naver.com", "80", id="kim", password="1234"))
print("키워드 가변인자 여러개:", userURIBuilder("naver.com", "80", id="kim", password="1234", 
    name="mike", age="30"))

#람다 함수(간단하게 함수를 정의, 익명함수) 
g = lambda x,y:x*y 
print("람다 함수:", g(3,4))
print("람다 함수:", g(5,6))

#메모리에 있는 변수, 함수를 딕셔너리 
print("전역 네임스페이스:", globals())

# =============================================================================
# 7. 예외처리
# =============================================================================
print("\n7. 예외처리")
print("-" * 30)

#함수를 정의
def divide(a,b):
    return a/b 

#에러 처리
try:
    #함수를 호출
    result = divide(5,0)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 합니다.")
except:
    print("다른 에러~~")
else:
    print("결과:{0}".format(result))
finally:
    print("무조건 실행(한번 더 체크)")

print("전체 코드 실행 종료")

print("\n" + "=" * 50)
print("Section 1 완료!")
print("=" * 50)
