# ========================================
# Section 6: 모듈과 파일
# ========================================
# 학습 내용:
# - 모듈과 패키지
# - 파일 읽기, 쓰기
# - with 구문 활용
# ========================================

# ========================================
# 6-1. 모듈과 패키지
# ========================================

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)
from pkg.fibonacci import Fibonacci

Fibonacci.fib(100)

print("ex1 : ", Fibonacci.fib2(200))
print("ex1 : ", Fibonacci().title)


# 사용2(클래스)
from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)


# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(500)

print("ex3 : ", fb.fib2(600))
print("ex3 : ", fb().title)


# 사용4(함수) : 파일 Alias
import pkg.calculations as c

print("ex4 : ", c.add(10,10))
print("ex4 : ", c.mul(10,4))


# 사용5(함수)
from pkg.calculations import div as d

print("ex5 : ", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))


# ========================================
# 6-2. 파일 읽기, 쓰기
# ========================================

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
f.close()

print()

# 예제2
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))
    print(list(c))
    print(c)

print()

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print()

# 예제4
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)
    contents = f.read()
    print('>', contents)
    f.seek(0, 0)
    contents = f.read()
    print('>', contents)

# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기

print()

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end='')
        line = f.readline()

# readlines : 전체 읽은 후 라인 단위 리스트 저장

print()
print()

# 예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    print()
    for c in contents:
        print(c, end='')

print()
print()

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))

# 파일 쓰기

# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('niceman!!')

# 예제3
from random import randint

with open('./resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)
    print('Test Contents!!', file=f)

