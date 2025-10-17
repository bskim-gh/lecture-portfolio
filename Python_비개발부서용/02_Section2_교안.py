# ========================================
# Section 2: 데이터 타입
# ========================================
# 학습 내용:
# - 숫자형 (int, float, complex)
# - 문자열 (str)
# - 리스트와 튜플
# - 딕셔너리와 집합
# - 실습 문제
# ========================================

# ========================================
# 2-1. 데이터타입, 숫자형, 숫자형 연산
# ========================================

'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

bytearray
byte
frozenset
'''

# 데이터 타입(Data Type)
v_str1 = "NiceMan"
v_bool = True
v_str2 = "GoodBoy"
v_float = 10.0
v_int = 7
v_list = [v_str1, v_str2]
v_dict = {
    "name": "niceman",
    "age": 25
}
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

# 데이터 타입 출력
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_tuple))
print(type(v_set))

# Numeric Operation (숫자형 연산자)
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 123456789123456789012345678901234567890
big_int2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939

# +
print("##### + #####")
print("i1 + i2 : ", i1 + i2) 
print("f1 + f2 : ", f1 + f2) 
print("big_int1 + big_int2 : ", big_int1 + big_int2) 
print("i1 + f1 : ", i1 + f1)

# -
print("##### - #####")
print("i1 - i2: ", i1 - i2) 
print("f1 - f2: ", f1 - f2)
print("big_int1 - big_int2: ", big_int1 - big_int2)
print("i1 - f1: ", i1 - f1)

# *
print("##### * #####")
print("i1 * i2: ", i1 * i2)
print("f1 * f2: ", f1 * f2)
print("big_int1 * big_int2: ", big_int1 * big_int2)
print("i1 * f1: ", i1 * f1)

# /
print("##### / #####")
print("i2 / i1: ", i2 / i1)
print("f2 / f1: ", f2 / f1)
print("big_int2 / big_int1: ", big_int2 / big_int1)
print("i1 / f1: ", i1 / f1)
print("f1 / i1: ", f1 / i1)

# //
print("##### // #####")
print("i2 // i1: ", i2 // i1) 
print("f2 // f1: ", f2 // f1)
print("big_int2 // big_int1: ", big_int2 // big_int1)
print("i1 // f1: ", i1 // f1)
print("f1 // i1: ", f1 // i1)

# %
print("##### % #####")
print("i1 % i2 :", i1 % i2)
print("f1 % f2 :", f1 % f2)
print("big_int1 % big_int2 :", big_int1 % big_int2)
print("i1 % f1 :", i1 % f1)
print("f1 % i1 :", f1 % i1)

# **
print("##### ** #####")
print("2 ** 3: ", 2 ** 3)
print("i1 ** i2: ", i1 ** i2) 
print("f1 ** f2: ", f1 ** f2)
print("i1 ** f1: ", i1 ** f1)
print("f1 ** i1: ", f1 ** i1)

# 형 변환 실습
a = 5.
b = 4
c = .4
d = 7.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(True))
print(int(False))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y)
print(pow(5, 3))

# 외부 모듈
import math

# ceil
print(math.ceil(5.1))
print(math.ceil(8.999))

# floor
print(math.floor(3.874))
print(math.floor(-25.5))

# pi
print(math.pi)

# 그 밖에 함수는 아래 URL 참조
# https://docs.python.org/3/library/math.html


# 2진수 변환
print(bin(50))


# ========================================
# 2-2. 문자열, 문자열 연산, 슬라이싱
# ========================================

# 문자열 생성
str1 = "I am Boy."
str2 = 'NiceMan'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 문자열 출력
print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

# 문자열 길이
print(len(str1))
print(len(str2))
print(len(str3))
print(len(str4))

# 빈 문자열
str_t1 = ''
str_t2 = str()

print(type(str_t1), len(str_t1))
print(type(str_t2), len(str_t2))

# 이스케이프 문자 사용

escape_str1 = "Do you have a \"big collection\"?"
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'

# 출력1
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

# 탭, 줄바꿈
t_s1 = "Tab \tClick!"
t_s2 = "New Line\n Start!!"

# 출력2
print(t_s1)
print(t_s2)

# Raw String
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"

# Raw String 출력
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)

multi_str1 = \
    """
    문자열
    멀티라인
    테스트
    """
# 멀티라인 출력
print(multi_str1)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))
print('x' in str_o1)
print('i' in str_o1)
print('e' not in str_o2)
print('O' not in str_o2)

# 문자열 형 변환
print(str(77))
print(str(10.4))
print(str(True))
print(str(complex(12)))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s"))
print("join str: ", str_o1.join(["I'm ", "!"]))
print("replace1: ", str_o1.replace('Nice', 'Good'))
print("replace2: ", str_o3.replace("is", "was", 3))
print("split: ", str_o4.split(' '))
print("sorted: ", sorted(str_o1))
print("reversed1: ", reversed(str_o2))
print("reversed2: ", list(reversed(str_o2)))

# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))
# 출력
for i in im_str:
    print(i)

# 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = 'Niceboy'

# 슬라이싱 연습
print(str_sl[0:3])
print(str_sl[:len(str_sl)])
print(str_sl[:len(str_sl) - 1])
print(str_sl[:])
print(str_sl[1:4:2])
print(str_sl[-3:6])
print(str_sl[1:-2])
print(str_sl[::-1])
print(str_sl[::2])

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a))
print(chr(116))


# ========================================
# 2-3. 리스트, 튜플
# ========================================

# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate']
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 리스트 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 리스트 수정, 삭제
print('#=====#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[3]
print('c - ', c)

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(6)
print('a - ', a)
a.sort()
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)
print('a - ', a)
a.reverse()
a.remove(1)
print('a - ', a)
print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 삭제 remove, pop, del

# 반복문 활용
while a:
    l = a.pop()
    print(2 is l)

# 튜플 자료형(순서O, 중복O, 수정X,삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, 'Pen', 'Cap', 'Plate')
e = (10, 100, ('Pen', 'Cap', 'Plate'))

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', e[-1][1][4])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('#=====#')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 튜플 함수
a = (5, 2, 3, 1, 4)

print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))


# ========================================
# 2-4. 딕셔너리, 집합 자료형
# ========================================

# 딕셔너리 자료형(순서X, 중복X, 수정O, 삭제O)

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)

# 출력
print('a - ', a['name'])
print('a - ', a.get('name'))
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))

print('a - ', 'name' in a)
print('a - ', 'addr' in a)

# 집합(Sets) 자료형(순서X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)

# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환
l = list(c)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('l - ', s1 & s2)
print('l - ', s1.intersection(s2))

print('l - ', s1 | s2)
print('l - ', s1.union(s2))

print('l - ', s1 - s2)
print('l - ', s1.difference(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)


# ========================================
# 2-5. 데이터 타입 관련 퀴즈 (문제)
# ========================================

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon


# 3. 화면에 * 기호 100개를 표시하세요.


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.


# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***


# ========================================
# 2-6. 데이터 타입 관련 퀴즈 (정답)
# ========================================

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print('1. q1길이:\t', len(q1))


# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon

print('2. print:\t', '''apple;orange;banana;lemon''')


# 3. 화면에 * 기호 100개를 표시하세요.

print('3. *100개:\t', star * 100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.

print('4. 정수형:\t', int(string30))
print('   실수형:\t', float(string30))
print('   복소수형:\t', complex(string30))
print('   문자형:\t', string30)


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

str = "Niceman"
manIdx = str.index("man")
print('5. 문자추출:\t', str[manIdx:manIdx + 3])


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"

sb = "Strawberry"
print('6. reverse:\t', sbResult)


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

phoneNumber = "010-7777-9999"
print('7. - 제거:\t', re.sub('[^0-9]', '', phoneNumber))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"

url = "http://daum.net"
urlIdx = url.index('''http://''')
print('8. http제거:\t', url[urlIdx + 7:])


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

str = "NiceMan"
print(str.upper())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

str = "abcdefghijklmn"
print(str[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]

list = ["Banana", "Apple", "Orange"]
list.remove("Apple")
print(list)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

tup = (1, 2, 3, 4)
print([s for s in tup])


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

dict = {}
dict['성인'] = 100000
dict['청소년'] = 70000
dict['아동'] = 30000
print(dict)


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

dict['소아']=0
print(dict)


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print(dict.keys())


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.

print(dict.values())


# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***

