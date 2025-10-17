"""
Test - Python 종합 연습문제
===========================

주요 내용:
- 연산자 활용
- 다이아몬드 별 출력
- 피보나치 수열
- 리스트에서 최댓값 찾기
- 선택정렬(Selection Sort)
- 로또 번호 생성
- 최대공약수 함수
- 팩토리얼 재귀 함수
- 클래스 활용
- 예외처리를 활용한 숫자 맞추기 게임
"""

# ====================================
# 1. 연산자
# ====================================

x = 4
y = -2

z = x + y
print('연산1 : x + y =', z)

z = x - y
print('연산2 : x - y =', z)

z = x * y
print('연산3 : x * y =', z)

z = x / y
print('연산4 : x / y =', z)

z = (x + y) * (x - y)
print('연산5 : (x + y) * (x - y) =', z)

z = (x * y) + (x / y)
print('연산6 : (x * y) + (x / y) =', z)

z = x * y ** 2
print('연산7 : %d x %d = %d' % (x, y ** 2, z))

z = x * y ** 3
print('연산8 : %d x %d = %d' % (x, y ** 3, z))

z = x * y ** 4
print('연산9 : %d x %d = %d' % (x, y ** 4, z))

z = x * y ** 5
print('연산10 : %d x %d = %d' % (x, y ** 5, z))


# ====================================
# 2. 다이아몬드 출력
# ====================================

count = 0

for i in range(1, 10):
    if i <= 5:
        count += 1
    else:
        count -= 1

    for j in range(5-count):
        print(" ", end="")

    for k in range(2 * count - 1):
        print('*', end="")

    print()


# ====================================
# 3. 피보나치 수열
# ====================================

n1 = 1
n2 = 2

print(n1, end='\n')
print(n2, end='\n')

for i in range(1, 10):
    n3 = n1 + n2
    print(n3, end='\n')

    n1 = n2
    n2 = n3


# ====================================
# 4. 리스트에서 최댓값 찾기
# ====================================

numbers = [17, 92, 18, 33, 58, 7, 26, 42]
maxNum = numbers[0]

for num in numbers:

    if maxNum < num:
        maxNum = num

print('numbers에서 가장 큰 수 :', maxNum)


# ====================================
# 5. 리스트 선택정렬
# ====================================

nums = [4, 2, 1, 5, 3]

for i in range(4):

    for j in range(i+1, 5):

        if nums[i] > nums[j]:

            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

# 정렬 후 출력
for n in nums:
    print(n, end=', ')


# ====================================
# 6. 로또 번호 생성
# ====================================

import math
import random


def lotto():

    lotto_set = set()

    while True:
        num = math.ceil(random.random() * 45)

        lotto_set.add(num)

        if len(lotto_set) == 6:
            break

    return list(lotto_set)


if __name__ == '__main__':
    for i in range(5):
        # 로또 번호 생성
        lotto_nums = lotto()

        # 번호 정렬
        lotto_nums.sort()

        # 번호 출력
        print(lotto_nums)


# ====================================
# 7. 최대공약수 함수
# ====================================

def gcd(a, b):
    temp = 0

    if a < b:
        temp = a
    else:
        temp = b

    while True:

        if a % temp == 0 and b % temp == 0:
            break

        temp -= 1

    return temp


if __name__ == '__main__':
    print('1과 5의 최대공약수 :', gcd(1, 5))
    print('2과 6의 최대공약수 :', gcd(2, 6))
    print('3과 9의 최대공약수 :', gcd(3, 9))
    print('18과 12의 최대공약수 :', gcd(18, 12))
    print('60과 24의 최대공약수 :', gcd(60, 24))


# ====================================
# 8. 팩토리얼 재귀 함수
# ====================================

def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n-1)


if __name__ == '__main__':
    print('3! =', factorial(3))
    print('4! =', factorial(4))
    print('5! =', factorial(5))


# ====================================
# 9. 클래스
# ====================================

class King:

    def __init__(self, name='태종', year=1392):
        self.name = name
        self.year = year

    def show(self):
        print('-----------------')
        print('name :', self.name)
        print('year :', self.year)


if __name__ == '__main__':

    king1 = King()
    king2 = King('태종')
    king3 = King('세종대왕', 1418)

    king1.show()
    king2.show()
    king3.show()


# ====================================
# 10. 예외처리를 활용한 숫자 맞추기 게임
# ====================================

# answer = math.ceil(random.random() * 45)
# number = 0
# count = 0
#
# while True:
#     count += 1
#     print('----------------------------')
#     print('answer를 맞춰보세요.')
#     number = input('1 ~ 45 사이의 값 입력 : ')
#
#     try:
#         # 문자를 숫자로 변환
#         number = int(number)
#     except:
#         print('숫자를 입력하십시요!')
#         continue
#
#     if number < 0:
#         print('음수를 입력할 수 없습니다.')
#         continue
#
#     if answer > number:
#         print('더 큰 수를 입력하세요.')
#
#     elif answer < number:
#         print('더 작은 수를 입력하세요.')
#
#     else:
#         print('정답 :', answer)
#         print('시도횟수 : %d회' % count)
#         break
#
# print('프로그램 정상종료...')

print('Test 종합 연습문제 학습 완료')

