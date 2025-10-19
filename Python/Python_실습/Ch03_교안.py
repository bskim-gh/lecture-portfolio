"""
Ch03 - Python 제어문
===================

주요 내용:
- 조건문(if, if-else, if-elif-else)
- 단일 조건문 및 중첩 조건문
- 삼항 조건문(조건부 표현식)
- while 반복문
- 무한 루프(infinite loop)
- break와 continue
- for 반복문
- range() 함수
- 이중 for문 및 구구단
- 별 삼각형 출력
- 리스트와 튜플을 이용한 반복
- random 모듈 활용
"""

# ====================================
# 1. 조건문(if)
# ====================================

# if
num1, num2 = 1, 2

if num1 > 0:
    print("num1은 0보다 크다")

if num1 > num2:
    print("num1은 num2보다 크다")

if num1 > 0:
    if num2 > 1:
        print("num1은 0보다 크고 num2는 1보다 크다.")

if num1 > 0 and num2 > 1:
    print("num1은 0보다 크고 num2는 1보다 크다.")

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    # 조건이 참일 때
    print("num3는 num4보다 크다.")
else:
    # 조건이 거짓일 때
    print("num3는 num4보다 작다.")

# if ~ elif ~ else
if num1 > num2:
    print("num1은 num2보다 크다.")
elif num2 > num3:
    print("num2는 num3보다 크다.")
elif num3 > num4:
    print("num3는 num4보다 크다.")
else:
    print("num4가 가장 크다.")

# 단일 조건문 형식 1
var = 10
if var >= 5:
    print("var =", var)
    print("var는 5보다 크다.")
    print("조건이 참인 경우 실행")

print("항상 실행")

# 중첩 조건문 예
# score = int(input("점수 입력 : "))
score = 85
grade = ""

if score >= 85 and score <= 100:
    grade = "우수"
elif score >= 70:
    grade = "보통"
else:
    grade = "저조"

print(f"당신의 점수는 {score}점이며 등급은 '{grade}'입니다.")


# ====================================
# 2. 삼항 조건문
# ====================================

# 일반 조건문
num = 9
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2
print("result =", result)

# 삼항 연산자
# 형식) 변수 = 참 if (조건문) else 거짓
result2 = num * 2 if num >= 5 else num + 2
print("result2 =", result2)

result2 = "True" if num <= 8 else "False"
print(result2)

# score = int(input("점수 입력: "))
score = 80
grade = ""

if 85 <= score <= 100:
    grade = "우수"
elif 70 <= score < 85:
    grade = "보통"
else:
    grade = "저조"

print("당신의 점수는 %d점이고, 당신의 등급은 '%s'입니다" % (score, grade))


# ====================================
# 3. while 반복문
# ====================================

# While문
num1, num5 = 1, 5

while num1 < num5:
    print("num1 :", num1)
    num1 += 1

# 1부터 10까지 합
k, sum = 1, 0

while k <= 10:
    sum += k
    k += 1

print("1부터 10까지의 합:", sum)

# 1부터 10까지 짝수 합
i, tot = 1, 0

while i <= 10:
    if i % 2 == 0:
        tot += i
    i += 1

print("1부터 10까지 짝수 합 :", tot)

# while 반복문 예
cnt = tot = 0

while cnt < 5:
    cnt += 1
    tot += cnt
    print(cnt, tot)

cnt = tot = 0
dataset = []

while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        dataset.append(cnt)

print(tot)
print(dataset)

# break
num = 1

while True:
    if num % 5 == 0 and num % 7 == 0:
        break  # 반복문 종료
    num += 1

print("5와 7의 최소공배수 :", num)

# continue
j, total = 1, 0

while j <= 10:
    j += 1
    if j % 2 == 1:
        continue
    total += j

print("1부터 10까지 짝수 합 :", total)


# ====================================
# 4. break와 continue
# ====================================

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end=" ")


# ====================================
# 5. for 반복문
# ====================================

# for문
for i in range(10):
    print("i :", i)

for i in range(10, 20):
    print("i :", i)

for i in range(10, 0, -2):
    print("i :", i)

# 1부터 10까지 합
sum1 = 0

for k in range(11):
    sum1 += k

print("1부터 10까지 합: %d" % sum1)

# 1부터 10까지 짝수 합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k

print("1부터 10까지 짝수 합: %d" % sum2)

# 문자열 반복
string = "홍길동"
print(len(string))
for s in string:
    print(s)

# 리스트 반복
lstset = [1, 2, 3, 4, 5]

for e in lstset:
    print("원소 :", e)


# ====================================
# 6. range 클래스
# ====================================

num1 = range(10)
print("num1 :", num1)

num2 = range(1, 10)
print("num2 :", num2)

num3 = range(1, 10, 2)
print("num3 :", num3)

for n in num1:
    print(n, end=" ")
print()
for n in num2:
    print(n, end=" ")
print()
for n in num3:
    print(n, end=" ")


# ====================================
# 7. 이중 for문
# ====================================

# 이중 for문
for a in range(3):
    print("a :", a)
    for b in range(5):
        print("b :", b)

# 구구단
for k in range(2, 10):
    print("구구단 %d단" % k)
    for i in range(1, 10):
        print("%d X %d = %d" % (k, i, k*i))

# 구구단 예제
print("★구구단(2~9단)★")

for i in range(2, 10):
    print("---%d단---" % i)
    for a in range(1, 10):
        print("%d * %d =" % (i, a), i*a)

# 별삼각형
for a in range(10, 0, -1):
    for b in range(a):
        print("★", end="")
    print("")

for i in range(10):
    print("☆"*i)

# 크리스마스 트리
print(" "*10+"@"+" "*11)
for k in range(10, 0, -1):
    print(" "*k+"*"*(11-k)+"*"*(10-k))
print(" "*9+"|||")
print(" "*9+"|||")


# ====================================
# 8. 리스트와 튜플을 이용한 for문
# ====================================

# 리스트를 이용한 for문
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print("num :", num)

for person in ["김유신", "김춘추", "장보고"]:
    print("person :", person)

scores = [62, 86, 72, 74, 96]
total = 0

for score in scores:
    total += score

print("점수 합 :", total)

# 튜플을 이용한 for문
nums = (10, 20, 30, 40, 50)

for n in nums:
    print("nums :", n)

for animal in ("사자", "호랑이", "독수리"):
    print("animal :", animal)


# ====================================
# 9. random 모듈
# ====================================

import random

# random() 함수
r = random.random()
rr = int(float(format(r, "2.2f"))*100)
print(type(rr))
print(rr)

cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.001:
        break
    else:
        cnt += 1

print("난수 개수 =", cnt)

# randint() 함수
names = ["홍길동", "이순신", "유관순"]
print(names)
print(names[2])

if "유관순" in names:
    print("유관순 있음")
else:
    print("유관순 없음")

idx = random.randint(0, 2)
print(names[idx])

# 리스트에 난수 추가
lst = []
for i in range(10):
    r = random.randint(1, 10)
    lst.append(r)

print("lst =", lst)

for i in range(10):
    print(lst[i] * 0.25)


# ====================================
# 10. 문장과 단어 추출
# ====================================

string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []

for sen in string.split(sep="\n"):
    sents.append(sen)
    for word in sen.split():
        words.append(word)

print("문장 :", sents)
print("문장 수 :", len(sents))
print("단어 :", words)
print("단어 수 :", len(words))

print(string.split(sep="\n"))

