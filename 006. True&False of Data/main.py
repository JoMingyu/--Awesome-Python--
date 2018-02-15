# 모든 자료형은 참과 거짓이 있다. 참과 거짓의 상태를 파이썬에선 bool 타입으로 관리한다
# 대문자로 시작하는 True, False 키워드가 각각 참과 거짓을 나타낸다

# 문자열을 포함하여 비어 있는(길이가 0인) iterable 객체('', [], (), {} 등)는 거짓
# 숫자형에서 0(0.0 포함)은 거짓
# None은 거짓
# https://wikidocs.net/17

# if문은 그러려니 하고 보도록 하자
if 'hello':
    print('hello')

if 1:
    print('number 1')

if [1, 2]:
    print('list')

if None:
    print('None')
