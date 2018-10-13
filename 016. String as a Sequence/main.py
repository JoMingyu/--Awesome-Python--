# Python의 문자열도 어떻게 보면 Sequence의 필요조건인 '순서 있는 열거'를 만족하고 있고,
# 실제로 문자열은 Python에서 Sequence로 분류된다. 따라서 인덱싱/슬라이싱/합/곱 연산 모두 가능하다

s = 'hello'

print(s[0]) # 'h'
print(s[-1]) # 'o'
print(s[1:-1]) # 'ell'
print(s[::2]) # 'hlo'
print(s + '!') # 'hello!'
print(s * 3 + '!') # 'hellohellohello!'
