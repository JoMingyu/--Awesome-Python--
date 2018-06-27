# https://docs.python.org/3/library/sqlite3.html
from sqlite3 import *
# https://github.com/python/cpython/tree/3.6/Lib/sqlite3/
# SQLite는 별도의 서버 모델이 없는 disk-base의 경량 데이터베이스를 제공하는 C 라이브러리
# SQL의 비표준 변형을 통해 데이터베이스에 접근하도록 허용

connection = connect('test.db')
# test.db에 대한 Connection 객체 생성

cursor = connection.cursor()
# Cursor 객체 생성

cursor.execute('CREATE TABLE users(id text, pw text, name text, birthday text)')
# create table

cursor.execute("INSERT INTO users VALUES('planb', 'pw', 'JoMingyu', '2001-02-05')")
# row insert

connection.commit()
# save(commit)

id = 'planb'

cursor.execute("SELECT * FROM users WHERE id='{}'".format(id))
# Python 내장 string formatting
print(cursor.fetchone())

cursor.execute('SELECT * FROM users WHERE id=?', (id,))
# 자체 지원 placeholder, ?로 placeholder를 표기하고, 튜플로 값을 전달
print(cursor.fetchone())

cursor.execute('DELETE FROM users')
connection.commit()

values = [
    ('planb', 'pw', 'JoMingyu', '2001-02-05'),
    ('geni429', 'pw', 'JeongGeunCheol', '2000-04-29'),
]

cursor.executemany('INSERT INTO users VALUES(?, ?, ?, ?)', values)
# placeholder에 들어가는 튜플을 list로 감싸고, placeholder가 포함된 SQL에 전달하면 쿼리를 연속적으로 수행
connection.commit()

cursor.execute('SELECT * FROM users')
print(cursor.fetchall())

for row in cursor.execute('SELECT * FROM users ORDER BY birthday'):
    # cursor 객체를 iterator처럼 사용
    print(row)