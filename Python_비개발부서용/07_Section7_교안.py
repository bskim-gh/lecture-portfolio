# ========================================
# Section 7: 예외처리 및 데이터 파일
# ========================================
# 학습 내용:
# - 예외처리 (try, except, else, finally)
# - CSV 파일 읽기/쓰기
# - Excel 파일 처리 (pandas)
# ========================================

# ========================================
# 7-1. 예외처리의 이해
# ========================================

# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError..
# 문법적으로 에러가 없지만 코드 실행 프로세스에서 발생하는 예외 처리 중요

# SyntaxError : 잘못된 문법

# print('test)
# print('Hello'))
# if True
#    pass
# a = 20; b = 30; a+ = b
# x => y


# NameError : 참조 변수 없음

a = 10
b = 15

# print(c)


# ZeroDivisionError : 0 나누기 에러

# print(10 / 0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]

# print(x[1])
# print(x[3])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop(50))


# KeyError

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

# print(dic['hobby'])
# print(dic.get('hobby'))


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장(EAFP 코딩 스타일)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# print(time.time())
# print(time.month())

x = [1, 2, 3]
# print(x.append(4))
# print(x.add(10))


# ValueError : 참조 값이 없을 때 예외

x = [1, 5, 9]

# x.remove(5)
# print(x)

# x.remove(100)
# print(x)

t = (10, 100, 1000)

print(t.index(100))
# print(t.index(7))


# FileNotFoundError

# f = open('test.txt')


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)
# print(sum([1,2,3],10,1))

# print(x + list(y))
# print(x + list(z)


# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행


# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제2

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제3

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:
    print(e)
else:
    print('ok! else!')
finally:
    print('ok! finally!')

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try:
    print('try')
finally:
    print('finally')

print()

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise ValueError
except ValueError:
    print('Raise! Occurred ValueError')
except Exception:
    print('Occurred Exception')
else:
    print('ok! else!')


# ========================================
# 7-2. Excel, CSV 파일 읽기 및 쓰기
# ========================================

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

# 예제3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-----')

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

with open('./resource/sample3.csv', 'w') as f:
    wt = csv.writer(f)
    print(dir(wt))
    print(type(wt))
    for v in w:
        wt.writerow(v)

# 예제5
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    print(dir(wt))
    print(type(wt))

    wt.writerows(w)


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())
print()

# 데이터 구조
print(xlsx.shape)


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)

