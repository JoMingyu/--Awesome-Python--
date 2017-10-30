# 파이썬에서 mysql server에 접근해 보자
# pip install pymysql

import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='abcd',
    db='test_db',
    charset='utf8'
)

# select문과 update, insert, delete문은 쿼리 수행에 차이가 있다

# 1. select문을 다룬 쿼리가 있다고 치면
selectQuery = ''
cursor = connection.cursor()
cursor.execute(selectQuery)
result = cursor.fetchall()

# 2. update or insert or delete문을 다룬 쿼리가 있다고 치면
updateQuery = ''
cursor = connection.cursor()
cursor.execute(updateQuery)
connection.commit()

# 기본적으로 커넥션에서 커서를 만들고 execute 함수를 이용해 쿼리문을 날리는 건 똑같고
# cursor.fetch를 쓰느냐 connection.commit을 쓰느냐의 차이
