"""
Ch04 - Python 자료구조 심화
===========================

주요 내용:
- 문자열(str) 클래스 객체
- 리스트(list) 객체: 생성, 인덱싱, 슬라이싱
- 단일 리스트와 중첩 리스트
- 리스트 메서드: append(), remove(), insert(), extend()
- 리스트 정렬: sort(), reverse
- 리스트 내포(List Comprehension)
- 튜플(tuple) 객체 및 관련 함수
- 집합(set) 객체 및 집합 연산
- 중복 제거 활용
- 딕셔너리(dict) 객체 및 메서드
- 단어 빈도수 구하기
- 얕은 복사(shallow copy)와 깊은 복사(deep copy)
"""

# ====================================
# 1. 문자열(str) 클래스 객체
# ====================================

str_var = str(object="string")
print(str_var)
print(type(str_var))
print(str_var[0])
print(str_var[-1])

str_var2 = "string"
print(str_var2)
print(type(str_var2))
print(str_var2[0])
print(str_var2[-1])


# ====================================
# 2. 리스트(list) 객체
# ====================================

# 단일 리스트 객체
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))

for i in lst:
    print(lst[:i])

# 리스트 색인
x = list(range(1, 11))

print(x)
print(x[:5])
print(x[-5:])
print("index 2씩 증가")
print(x[::2])
print(x[1::2])

# 중첩 리스트 객체
a = ["a", "b", "c"]
print(a)

b = [10, 20, a, 5, True, "문자열"]
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])


# ====================================
# 3. 리스트 메서드: 추가, 삭제, 수정, 삽입
# ====================================

# append, remove, 수정, insert
num = ["one", "two", "three", "four"]
print(num)
print(len(num))

num.append("five")
print(num)

num.remove("five")
print(num)

num[3] = "4"
print(num)

num.insert(0, "zero")
print(num)

# extend와 append의 차이
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y
print(z)

x.extend(y)
print(x)
print("len(x) :", len(x))

x.append(y)
print(x)
print("len(x) :", len(x))

# 리스트 곱하기
lst = [1, 2, 3, 4]
result = lst * 2
print(result)


# ====================================
# 4. 리스트 정렬과 요소 검사
# ====================================

lst = [1, 2, 3, 4]
result = lst * 2
print(result)
result.sort()
print(result)
result.sort(reverse=True)
print(result)

import random
r = []
for i in range(5):
    r.append(random.randint(1, 5))

print(r)
if 4 in r:
    print("있음")
else:
    print("없음")


# ====================================
# 5. 리스트 내포(List Comprehension)
# ====================================

x = [2, 4, 1, 5, 7]

lst = [i ** 2 for i in x]
print(lst)

num = list(range(1, 11))
print(num)

lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)


# ====================================
# 6. 튜플(tuple) 객체
# ====================================

# 튜플 생성
t = (10, )
print(t)

t2 = (1, 2, 3, 4, 5, 3)
print(t2)

print(t2[0], t2[1:4], t2[-1])

for i in t2:
    print(i, end=" ")

print()

if 6 in t2:
    print("6 있음")
else:
    print("6 없음")

# 튜플 관련 함수
lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)

print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))


# ====================================
# 7. 집합(set) 객체
# ====================================

# 집합 생성 (중복 자동 제거)
s = {1, 3, 5, 3, 1}
print(len(s))

for d in s:
    print(d, end=" ")

print()

# 집합 연산
s2 = {3, 6}
print(s.union(s2))  # 합집합
print(s.difference(s2))  # 차집합
print(s.intersection(s2))  # 교집합

# 집합 메서드
s3 = {1, 3, 5}
print(s3)

s3.add(7)
print(s3)

s3.discard(3)
print(s3)


# ====================================
# 8. 중복 제거 활용
# ====================================

gender = ["남", "여", "남", "여"]

print(gender)

sgender = set(gender)
lgender = list(sgender)
print(lgender)

print(lgender[1])


# ====================================
# 9. 딕셔너리(dict) 객체
# ====================================

# 딕셔너리 생성
dic = dict(key1=100, key2=200, key3=300)
print(dic)

person = {"name": "홍길동", "age": 35, "address": "서울시"}
print(person)
print(person["name"])
print(type(dic), type(person))

# 딕셔너리 수정
person["age"] = 45
print(person)

# 딕셔너리 삭제
del person["address"]
print(person)

# 딕셔너리 추가
person["pay"] = 350
print(person)

# 요소 검사와 반복
print(person["age"])
print("age" in person)

for key in person.keys():
    print(key)
for v in person.values():
    print(v)

for i in person.items():
    print(i)


# ====================================
# 10. 단어 빈도수 구하기
# ====================================

charset = ["abc", "code", "band", "band", "abc"]
wc = {}

for key in charset:
    wc[key] = wc.get(key, 0) + 1
print(wc)


# ====================================
# 11. 얕은 복사(shallow copy)와 깊은 복사(deep copy)
# ====================================

name = ["홍길동", "이순신", "강감찬"]
print("name address =", id(name))

# 얕은 복사 (주소만 복사)
name2 = name
print("name2 address =", id(name2))

print(name)
print(name2)

name2[0] = "김길동"
print(name)
print(name2)

# 깊은 복사 (값을 복사)
import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)

print("name address =", id(name))
print("name3 address =", id(name3))

name[1] = "이순신장군"
print(name)
print(name3)

