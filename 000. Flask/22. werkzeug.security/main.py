# -- 알아볼 부분
# werkzeug.security - https://github.com/pallets/werkzeug/blob/master/werkzeug/security.py

# Flask는 WSGI 툴킷으로 Werkzeug를 사용하고 있는데, werkzeug.security에 좋은 헬퍼 함수들이 많다
# http://werkzeug.pocoo.org/docs/0.14/utils/

from werkzeug.security import safe_str_cmp
# 버전 0.7에서 새롭게 만들어진 문자열 비교 함수
# werkzeug.security.safe_str_cmp(a, b)
# 문자열을 일정한 시간 간격으로 비교한다고 한다

if safe_str_cmp('abc', 'abc'):
    print('equal')


from werkzeug.security import generate_password_hash as pw_hash_gen
# 버전 0.6.1에서 새롭게 만들어진 비밀번호 hashing 헬퍼 함수
# werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
hashed_pw = pw_hash_gen('plaintext')
# 아래처럼 method$salt$hash 형태의 문자열이 리턴됨
# 'pbkdf2:sha256:50000$LJv1AtJ1$5093598a1ca66765b1432c6604a7d64f1503e8a62e6029b40fae4195b5054fe3'

from werkzeug.security import check_password_hash as pw_hash_check
# werkzeug.security.check_password_hash(pwhash, password)
print(pw_hash_check(hashed_pw, 'plaintext'))
