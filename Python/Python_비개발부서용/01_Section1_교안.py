# ========================================
# Section 1: Python 소개 및 기본 문법
# ========================================
# 학습 내용:
# - Python 기본 출력 (print)
# - 변수, 조건문, 반복문, 함수, 클래스 기초
# - 가상환경 및 패키지 관리
# ========================================

# ========================================
# 1-1. Python 소개 및 기본 출력
# ========================================

print('Hello Python!')


# ========================================
# 1-2. Print 구문의 이해
# ========================================
# 참조 : https://www.python-course.eu/python3_formatted_output.php

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
# 기본 출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()

# separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

print()

# end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# file 옵션 사용
import sys

print('GeeksForGeeks', file=sys.stdout)

print()

print("%s's favorite number is %d" % ('Eunki', int(45)))

# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))

# %d, %f, %s
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0:5d}, Price:{1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))


# ========================================
# 1-3. 기본 코딩 실습
# ========================================

import this
import sys


# 파이썬 2.x vs 3.x 기본 캐릭터 셋 설명
# Python 3.x 입력 인코딩
print(sys.stdin.encoding)

# Python 3.x 출력 인코딩
print(sys.stdout.encoding)

# 출력문
print("My name is Goodboy!")

# 변수선언
myName = "Goodboy"

# 조건문
if myName == "Goodboy":
    print("OK!")

# 반복문(구구단)
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i * j)

# 변수선언(한글)
이름 = "좋은사람"

# 출력
print(이름)


# 함수선언(한글명)
def 인사():
    print("안녕하세요. 반갑습니다.")


# 함수 실행
인사()


# 클래스 선언
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

# 정보 값 출력
print(id(cookie))
print(dir(cookie))
print(cookie.__class__)
print(cookie.__hash__)


# ========================================
# 1-4. 가상환경 개념 및 pip 사용법
# ========================================

# 외부 설치 패키지 테스트
import simplejson as json

test_dict = {'1': 95, '4': 77, '3': 65, '5': 100, '2': 88}

# simplejson 실행
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))


'''
python -m venv 가상환경명
	Script\activate.bat
	Script\deactivate.bat
	pip 명령어 : search , install, uninstall, list, freeze, show
	pip install search simplejson , simple*
	pip install install simplejson
	pip install install simplejson==버전
	pip install --upgrade simplejson
	pip show simplejson
	pip show -f simplejson
	pip freeze > packages.txt
	pip freeze --all > packages.txt
	pip install -r packages.txt


	python -m venv /path/to/venv : 윈도우, 맥, 리눅스 동일

	윈도우 : Script
	맥 : bin

	윈도우 

	activate.bat : 가상환경 진입
	deactivate.bat : 가상환경 해제

	맥
	source ./activate : 가상환경 진입
	source ./deactivate : 가상환경 해제

	command : code 실행
'''

