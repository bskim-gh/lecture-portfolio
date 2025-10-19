# ========================================
# Section 8: 데이터베이스
# ========================================
# 학습 내용:
# - SQLite 데이터베이스
# - 테이블 생성 및 데이터 삽입
# - 데이터 조회
# - 데이터 수정 및 삭제
# ========================================

# ========================================
# 8-1. 테이블 생성 및 삽입
# ========================================

import datetime
import sqlite3

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime', nowDatetime)

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version', sqlite3.sqlite_version)

# DB생성 & Autocommit
# 본인 DB 파일 경로
conn = sqlite3.connect('본인이 원하는 경로/database.db', isolation_level=None)

# DB생성(메모리)
# conn = sqlite3.connect(":memory:")

# Cursor연결
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Datatype : TEXT NUMERIC INTEGER REAL BLOB)
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES (1 ,'Kim','Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDatetime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
          (2, 'Park', 'Park@naver.com', '010-1111-1111', 'Park.com', nowDatetime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-3333-3333', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-4444-4444', 'Yoo.com', nowDatetime)
)
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)


# 테이블 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 커밋 : isolation_level=None 일 경우 자동 반영(Auto Commit)
conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()


# ========================================
# 8-2. 테이블 조회
# ========================================

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect('본인이 원하는 경로/database.db')

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 된다.
# 1개 로우 선택
print('One -> \n', c.fetchone())

# 지정 로우 선택
print('Three -> \n', c.fetchmany(size=3))

# 전체 로우 선택
print('All -> \n', c.fetchall())

print()

# 순회1
rows = c.fetchall()
for row in rows:
    print('retrieve1  >', row)

# 순회2
for row in c.fetchall():
    print('retrieve2 >', row)

# 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print('retrieve3 > ', row)

print()

# WHERE Retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall())

# WHERE Retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)
print('param2', c.fetchone())
print('param2', c.fetchall())

# WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

# WHERE Retrieve4
param4 = (1, 4)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('param4', c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id In('%d','%d')" % (1, 4))
print('param5', c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

with conn:
    # Dump 출력(데이터베이스 백업 시 중요)
    with open('본인이 원하는 경로/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete.')


# ========================================
# 8-3. 테이블 수정 및 삭제
# ========================================

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('본인이 원하는 경로/database.db/database.db')

# Cursor연결
c = conn.cursor()

# 데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 1))

# 데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'niceman', 'id': 3})

# 데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 5))

# 중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (7,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {'id': 8})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 9)

# 중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 관계형 데이터 베이스

# 커밋
conn.commit()

# 접속 해제
conn.close()

