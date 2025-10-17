# ========================================
# Section 3: 흐름 제어
# ========================================
# 학습 내용:
# - 조건문 (if, elif, else)
# - 관계 연산자, 논리 연산자
# - 반복문 (while, for)
# - break, continue, else
# - 실습 문제
# ========================================

# ========================================
# 3-1. 조건문 실습
# ========================================


print(type(True))
print(type(False))

# 기본 형식

# 예1
if True:
    print("Yes")

if False:
    print("No")

# 예2
if False:
    print("You can't reach here")
else:
    print("Oh, you are here")

# 관계연산자
# >, >=, <, <=, ==, !=


a = 10
b = 0

# == 양 변이 같을 때 참.
print(a == b)

# != 양 변이 다를 때 참.
print(a != b)

# > 왼쪽이 클때 참.
print(a > b)

# >= 왼쪽이 크거나 같을 때 참.
print(a >= b)

# < 오른쪽이 클 때 참.
print(a < b)

# <= 오른쪽이 크거나 같을 때 참.
print(a <= b)

# 참 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1
# 거짓 : "", [], (), {}, 0, None

city = ""
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

city = "Seoul"
if city:
    print("You are in:", city)
else:
    print("Please enter your city")

# 논리연산자
# and, or, not

a = 100
b = 60
c = 15

print('and : ', a > b and b > c)
print('or : ', a > b or b > c)
print('not : ', not a > b)
print('not : ', not b > c)
print(not True)
print(not False)

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리 순서로 적용

print('ex1 : ', 3 + 12 > 7 + 3)
print('ex2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('ex3 : ', 5 + 10 > 3 and 7 + 3 == 10)
print('ex4 : ', 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행.
if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("불합격입니다.")

id1 = "gold"
id2 = "admin"
grade = 'super'

if id1 == "gold" or id2 == "admin":
    print("관리자 로그인 성공")

if id2 == "admin" and grade == "super":
    print("최고 관리자 로그인 성공")

is_work = False

if not is_work:
    print("is work!")

# 다중 조건문
num = 90

if num >= 70:
    print("num ? ", num)
elif num >= 60:
    print("num ? ", num)
else:
    print("default num")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원가능")

# in, not in

q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e)
print("seoul" in e.values())


# ========================================
# 3-2. 반복문 실습
# ========================================

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 사용(while, for)
v1 = 1

while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2)

for v3 in range(1, 11):
    print("v3 is :", v3)

for v4 in range(1, 11, 2):
    print("v4 is :", v4)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1 ~ 100 합 : ', sum1)
print('1 ~ 100 합 : ', sum(range(1, 101)))
print('1 ~ 100 안에 3의 배수의 합 : ', sum(range(1, 101, 3)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]

for name in names:
    print("You are", name)

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for number in lotto_numbers:
    print("Your number", number)

# 예제3
word = 'dreams'

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

for key in my_info:
    print(key, ":", my_info[key])

for val in my_info.values():
    print(val)

# 예제5
name = 'KennRY'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break
for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : ", num)

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue

    print("type:", type(v))
    print("multiply by 2:", v * 3)

# for-else 실습
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : ", num)
else:
    print("Not Found 39...")

# flag 사용

f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:
            print("found : 33!")
            f = False
        print("not found : ", v)

# else 구문 정리(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
# 예제1

i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1
else:
    print('else block run!')

# 예제2
j = 1
while j <= 10:
    print('j : ', j)
    if j == 11:
        break
    j += 1
else:
    print('else block run!')

# 중첩 for 문 구구단 출력

for i in range(1, 11):
    for j in range(1, 11):
        print('{:4d}'.format(i * j), end='')
    print()

# 자료 구조 변환 예제
name = 'Niceman'
print('reversed : ', reversed(name))
print('list : ', list(reversed(name)))
print('list : ', tuple(reversed(name)))
print('list : ', set(reversed(name)))


# ========================================
# 3-3. 제어문 관련 퀴즈 (문제)
# ========================================

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]


# ========================================
# 3-4. 제어문 관련 퀴즈 (정답)
# ========================================

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print(''.join([q1[s] for s in q1 if s == '가을']))


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.

q2 = fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

hasApple = ['사과다!' for key, val in q2.items() if key == '사과' or val == '사과']

if len(hasApple) > 0:
    print('사과있음')
else:
    print('사과없음 ㅡㅡ')


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 100
grade = ''
if 0 < score > 100:
    grade = '나가'
elif score > 80:
    grade = 'A'
elif score > 60:
    grade = 'B'
elif score > 40:
    grade = 'C'
elif score > 20:
    grade = 'D'
elif score >= 0:
    grade = 'E'

print(grade)


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18
best = 0

best = a
if b > a:
    best = b
if c > b:
    best = c

print(best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

s = '891022-2473837'
if int(s[7]) % 2 == 0:
    print('여자')
else:
    print('남자')


# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

print(''.join([s for s in q3 if s != '정']))


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

print(' '.join([str(s) for s in range(1, 100) if int(s) % 2 == 1]))


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

print([s for s in q4 if len(s) >= 5])


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print([s for s in q5 if s.islower()])


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

print([s.upper() if s.islower() else s.lower() for s in q5])

