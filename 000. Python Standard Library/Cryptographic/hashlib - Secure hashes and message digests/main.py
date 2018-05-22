# https://docs.python.org/3/library/hashlib.html
import hashlib
# hashlib을 사용하면 쉽게 단방향 해시 값을 구할 수 있다
# sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, md5를 기본적으로 제공하며
# 거의 모든 플랫폼에서 sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256를 추가로 제공한다

# 'Hello World'를 sha256으로 해시하고 hex digest를 얻어오자
m = hashlib.sha256()

m.update(b'Hello')
m.update(b' World')
print(m.hexdigest())

# 압축시키면
print(hashlib.sha256(b'Hello World').hexdigest())

m = hashlib.new('ripemd160')
# new()는 통칭적인 생성자로 첫 파라미터에 원하는 알고리즘을 문자열 형태로 전달
# hashlib에서 사용할 수 있는 암호화 알고리즘은 아래처럼 확인할 수 있다
print(hashlib.algorithms_available)

# 해시는 암호학에서 널리 사용되지만 짧은 시간에 데이터를 검색하기 위해 설계되었기 때문에, brute-force에 취약하고(MD5는 보편적으로 1초 당 56억 개의 digest 대입 가능)
# 동일한 메시지가 언제나 동일한 digest를 가지므로, 공격자가 전처리된 digest를 가능한 한 많이 확보한 다음 이를 탈취한 digest와 비교해 원본 메시지를 찾아낼 수 있음(rainbow attack)

# 1. salting
# 단방향 해시 함수에서 digest를 생성할 때 추가되는 바이트 단위의 임의 문자열인 salt를 이용하고, 이를 이용해 digest를 생성하는 것을 salting이라고 한다
# 공격자 입장에서 특정 메시지의 digest를 알고 있더라도, salting된 digest를 대상으로 패시워드 일치 여부를 확인하기 어렵다
# 또한 사용자별로 다른 salt를 사용한다면 동일한 패스워드를 사용하는 각 사용자의 digest가 다르게 생성되어 인식 가능성 문제가 크게 개선된다

# 2. key stretching
# 입력한 패스워드의 digest를 생성하고, 생성된 digest를 입력 값으로 digest를 생성하는 과정을 반복할 수 있다
# 이렇게 하면 입력한 패스워드를 동일한 횟수만큼 해시해야만 입력한 패스워드의 일치 여부를 확인할 수 있다. 이것이 기본적인 key stretching 과정이다
# 하나의 다이제스트를 생성할 때 어느 정도(0.2초 정도)의 시간이 소요되게 설정하는 것이 좋다. 이렇게 되면 brute-force를 쉽게 방어할 수 있다

# Adaptive key derivation function은 digest를 생성할 때 salting과 key stretching을 반복하며 공격자가 쉽게 digest를 유추할 수 없도록 하고
# 보안의 강도를 선택할 수 있다. 가장 많이 사용되는 key derivation function은 PBKDF2(Password-Based Key Derivation Function)이다

import binascii

dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
print(binascii.hexlify(dk).decode())

# PBKDF2와 유사한 adaptive key derivation function이며 더 경쟁력 있는 bcrypt, scrypt도 있다
# hashlib은 Python 3.6 이상에서 scrypt를 제공한다
