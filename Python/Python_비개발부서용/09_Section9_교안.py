# ========================================
# Section 9: 프로젝트 실습
# ========================================
# 학습 내용:
# - 타이핑 게임 제작 (기본)
# - 타이핑 게임 제작 (사운드 & DB 연동)
# - 주소록 프로그램 제작
# ========================================

# ========================================
# 9-1. 타이핑 게임 제작 및 기본완성
# ========================================

import random
import time

words = []

n = 1
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

print(words)

input("Ready? Press Enter Key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

	print()

    print("*Question # {}".format(n))
    print(q)

    x = input()

	print()
    
    if str(q).strip() == str(x).strip():
        print("Pass!")
        cor_cnt += 1
    else:
        print("Wrong!")

    n += 1

end = time.time()
et = end - start

et = format(et, ".3f")

if cor_cnt >= 3:
    print("결과 : 합격")
else:
    print("불합격")
    
print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

if __name__ == '__main__':
    pass


# ========================================
# 9-2. 타이핑 게임 - 사운드 적용 및 DB 연동
# ========================================

import random
import time
import winsound
import sqlite3
import datetime

# DB생성 & Autocommit
conn = sqlite3.connect('본인이 원하는 경로/records.db', isolation_level=None)

# Cursor연결
cursor = conn.cursor()

# 테이블 생성(Datatype : TEXT NUMERIC INTEGER REAL BLOB)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,  cor_cnt INTEGER, record text, regdate text)"
)

words = []

n = 1
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

print(words)

input("Ready? Press Enter Key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

	print()

    print("*Question # {}".format(n))
    print(q)

    x = input()

	print()
    
    if str(q).strip() == str(x).strip():
        winsound.PlaySound(
            './sound/good.wav',
            winsound.SND_FILENAME
        )
        print("Pass!")
        cor_cnt += 1

    else:
        winsound.PlaySound(
            './sound/bad.wav',
            winsound.SND_FILENAME
        )

        print("Wrong!")

    n += 1

end = time.time()
et = end - start

et = format(et, ".3f")

print()
print('--------------')


if cor_cnt >= 3:
    print("결과 : 합격")
else:
    print("불합격")

# 기록 DB 삽입
cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?, ?, ?)",
    (
        cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    )
)

# 접속 해제
conn.close()

print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))


# ========================================
# 9-3. 주소록 제작
# ========================================

import os.path
import pickle


# 연락처 클래스
class Contact:
    def __init__(self, name, phone_num, email):
        self.name = name
        self.phone_num = phone_num
        self.email = email

    def prt_info(self):
        print("Name : {}".format(self.name))
        print("Phone_number : {}".format(self.phone_num))
        print("e_mail : {}".format(self.email))
        print("-" * 20)
        print()


# 연락처 정보 입력
def add_cont(c_list):
    name = input_name()
    phone_num = input_phone()
    email = input_email()
    print()

    for v in c_list:
        if name == v.name:
            print('Name exists.')
            print()
            break
    else:
        cont = Contact(name, phone_num, email)
        print('saved.')
        print()
        c_list.append(cont)


# 메뉴 출력
def prt_menu():
    print("1. Add")
    print("2. Info")
    print("3. Delete")
    print("4. DB Save")
    print("5. DB Drop")
    print("6. Exit")
    print()
    menu = input("Select Menu Number : ")
    print()
    return int(menu)


# 이름으로 조회 된 연락처 삭제
def del_cont(c_list):
    nm = input("Name: ")
    print()

    if len(c_list) > 0:
        for i, cont in enumerate(c_list):
            if str(cont.name).strip() == nm.strip():
                print('"{}" deleted.'.format(cont.name))
                print()
                del c_list[i]
                break
        else:
            print('No files to delete.')
            print()
    else:
        print('No files to delete.')
        print()


# 저장 된 모든 연락처 정보 출력
def prt_cont(c_list):
    if len(c_list) > 0:
        for i in c_list:
            i.prt_info()
    else:
        print('Contact is empty.')
        print()


# 파일로 저장
def store_cont_db(c_list):
    try:
        with open("cont_db.bin", "wb") as f:
            pickle.dump(c_list, f)

            print('db saved')
            print()
    except IOError as log:
        print(log)


# 파일 DB 로드
def load_cont_db():
    p_list = []
    if os.path.isfile('cont_db.bin'):
        try:
            with open("cont_db.bin", "rb") as f:
                p_list = pickle.load(f)
        except IOError as log:
            print(log)
    else:
        print('DB File not found!')
        print()

    return p_list


# 파일 DB 삭제
def drop_cont_db():
    if os.path.isfile('cont_db.bin'):
        try:
            os.remove('cont_db.bin')
            print('DB File dropped.')
        except FileNotFoundError as log:
            print(log)
    else:
        print('DB File not found!')
        print()


# 이름 입력
def input_name():
    while True:
        try:
            name = input("Name: ")
            if len(name) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Name is too short.")
    return name


# 전화번호 입력
def input_phone():
    while True:
        try:
            phone_num = input("Phone number: ")
            if len(phone_num) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Phone number is too short.")
    return phone_num


# 전화번호 입력
def input_email():
    while True:
        try:
            phone_email = input("E-mail: ")
            if len(phone_email) < 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Email is too short.")
    return phone_email


# 프로그램 시작
def main():
    c_list = load_cont_db()

    while True:
        menu = prt_menu()
        if menu == 1:
            add_cont(c_list)
        elif menu == 2:
            prt_cont(c_list)
        elif menu == 3:
            del_cont(c_list)
        elif menu == 4:
            store_cont_db(c_list)
        elif menu == 5:
            drop_cont_db()
        else:
            break


if __name__ == "__main__":
    main()

