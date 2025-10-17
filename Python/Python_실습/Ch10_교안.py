"""
Ch10 - Python 데이터베이스 프로그래밍
=====================================

주요 내용:
- 데이터베이스 연결
- pymysql 모듈을 이용한 MySQL 연동
- sqlite3 모듈을 이용한 SQLite 연동
- CRUD 작업: INSERT, SELECT, UPDATE, DELETE
- cursor 객체를 이용한 SQL 실행
- fetchall()을 이용한 결과 조회
- commit()을 이용한 변경사항 확정
- 사용자 등록 및 조회 프로그램
- SQLite 데이터베이스 생성
- SQLite CRUD 프로그래밍
"""

import pymysql
import sqlite3

# ====================================
# 1. MySQL INSERT
# ====================================

def mysql_insert():
    conn = pymysql.connect(host='공용DB localhost',
                           user='bskim02',
                           password='1234',
                           db='bskim02_db',
                           charset='utf8')

    # SQL 실행 객체 생성
    cur = conn.cursor()

    # SQL 실행
    sql = "INSERT INTO `USER1` VALUES ('test', '홍길동', '010-1234-1001', 25);"
    cur.execute(sql)

    # 실행 확정
    conn.commit()

    # 데이터베이스 접속 종료
    conn.close()

    print('- INSERT 완료 -')


# ====================================
# 2. MySQL UPDATE
# ====================================

def mysql_update():
    conn = pymysql.connect(host='공용DB localhost',
                           user='bskim02',
                           password='1234',
                           db='bskim02_db',
                           charset='utf8')

    # SQL 실행 객체 생성
    cur = conn.cursor()

    # SQL 실행
    sql = "UPDATE `USER1` SET `hp`='010-1234-1101' WHERE `uid`='p101';"
    cur.execute(sql)

    # 실행 확정
    conn.commit()

    # 데이터베이스 접속 종료
    conn.close()

    print('- UPDATE 완료 -')


# ====================================
# 3. MySQL DELETE
# ====================================

def mysql_delete():
    conn = pymysql.connect(host='공용DB localhost',
                           user='bskim02',
                           password='1234',
                           db='bskim02_db',
                           charset='utf8')

    # SQL 실행 객체 생성
    cur = conn.cursor()

    # SQL 실행
    sql = "DELETE FROM `USER1` WHERE `uid`='p101';"
    cur.execute(sql)

    # 실행 확정
    conn.commit()

    # 데이터베이스 접속 종료
    conn.close()

    print('- DELETE 완료 -')


# ====================================
# 4. MySQL SELECT
# ====================================

def mysql_select():
    conn = pymysql.connect(host='공용DB localhost',
                           user='bskim02',
                           password='1234',
                           db='bskim02_db',
                           charset='utf8')

    # SQL 실행 객체 생성
    cur = conn.cursor()

    # SQL 실행
    cur.execute("SELECT * FROM `USER1`;")

    # 결과 출력
    for row in cur.fetchall():
        print('----------------')
        print('아이디 :', row[0])
        print('이름 :', row[1])
        print('휴대폰 :', row[2])
        print('나이 :', row[3])
        print('----------------')

    # 데이터베이스 종료
    conn.close()


# ====================================
# 5. 사용자 등록 및 조회 프로그램
# ====================================

def user_register_program():
    conn = pymysql.connect(host='공용DB localhost',
                           user='bskim02',
                           password='1234',
                           db='bskim02_db',
                           charset='utf8')

    while True:

        print('0:종료, 1:등록, 2:조회')

        result = input('입력 : ')
        if result == '0':
            print('- 프로그램이 종료되었습니다 -')
            break

        elif result == '1':
            # 사용자 등록
            uid = input('아이디 입력 : ')
            name = input('이름 입력 : ')
            hp = input('휴대폰 입력 : ')
            age = input('나이 입력 : ')

            # SQL 실행 객체 생성
            cur = conn.cursor()

            # SQL 실행
            sql = "INSERT INTO `USER1` VALUES ('%s', '%s', '%s', '%s');" % (uid, name, hp, age)
            cur.execute(sql)

            # 실행 확정
            conn.commit()

            print('- 사용자 등록 완료 -')

        elif result == '2':
            # 사용자 조회
            uid = input('조회하고 싶은 아이디 입력 : ')

            # SQL 실행 객체 생성
            cur = conn.cursor()

            # SQL 실행
            cur.execute("SELECT * FROM `USER1` WHERE `uid`= '%s';" % uid)

            # 결과 출력
            for row in cur.fetchall():
                print('----------------')
                print('아이디 :', row[0])
                print('이름 :', row[1])
                print('휴대폰 :', row[2])
                print('나이 :', row[3])
                print('----------------')

            print('- 사용자 조회 완료 -')

        else:
            print('오류: 입력값을 다시 한 번 확인해주십시오.')

    conn.close()


# ====================================
# 6. SQLite 데이터베이스 생성
# ====================================

def sqlite_create():
    conn = sqlite3.connect('./data/sqlite_db')
    print('DB파일 생성')

    cur = conn.cursor()

    sql = 'CREATE TABLE IF NOT EXISTS `test_table` ('
    sql += '`name` text(10), '
    sql += '`phone` text(15), '
    sql += '`addr` text(50)'
    sql += ');'

    cur.execute(sql)

    cur.execute("INSERT INTO `test_table` VALUES ('홍길동', '010-1111-1001', '서울시')")
    cur.execute("INSERT INTO `test_table` VALUES ('이순신', '010-1111-1002', '해남시')")
    cur.execute("INSERT INTO `test_table` VALUES ('강감찬', '010-1111-1003', '평양시')")

    conn.commit()

    conn.close()


# ====================================
# 7. SQLite CRUD 프로그래밍
# ====================================

def sqlite_crud():
    print(sqlite3.sqlite_version_info)

    conn = sqlite3.connect('./data/sqlite_db')

    cur = conn.cursor()

    sql = """CREATE TABLE IF NOT EXISTS `goods`(
            `code`  INTEGER     PRIMARY KEY,
            `name`  TEXT(30)    UNIQUE NOT NULL,
            `su`    INTEGER     DEFAULT 0,
            `dan`   REAL        DEFAULT 0.0
            );
            """
    cur.execute(sql)

    cur.execute("INSERT INTO `goods` VALUES (1, '냉장고', 2, 8500000)")
    cur.execute("INSERT INTO `goods` VALUES (2, '세탁기', 3, 5500000)")
    cur.execute("INSERT INTO `goods` (`code`, `name`) VALUES (3, '전자레인지')")
    cur.execute("INSERT INTO `goods`(`code`, `name`, `dan`) VALUES (4, 'HDTV', 15000000)")

    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))

    sql = f"INSERT INTO `goods` VALUES({code},'{name}', {su}, {dan})"
    cur.execute(sql)
    conn.commit()

    code = int(input('수정 code 입력 : '))
    su = int(input('수정 su 입력 : '))
    dan = int(input('수정 dan 입력 : '))

    sql = f"UPDATE `goods` SET `su` = {su}, `dan` = {dan} WHERE `code` = {code}"
    cur.execute(sql)
    conn.commit()

    code = int(input('삭제 code 입력 : '))
    sql = f"DELETE FROM `goods` WHERE `code` = {code}"
    cur.execute(sql)
    conn.commit()

    sql = "SELECT * FROM `goods`"
    cur.execute(sql)
    rows = cur.fetchall()

    for row in rows:
        print(row[0], row[1], row[2], row[3])

    print('검색된 레코드 수 :', len(rows))

    name = input("상품명 입력 : ")
    sql = f"SELECT * FROM `goods` WHERE `name` LIKE '{name}'"
    cur.execute(sql)
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print('검색된 레코드 없음')

    conn.commit()


if __name__ == '__main__':
    print('Ch10 데이터베이스 프로그래밍 학습 완료')
    # 실행 예제: mysql_select(), sqlite_create(), sqlite_crud() 등

