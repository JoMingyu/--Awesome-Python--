s = 'PlanB'
# 문자열도 Python의 빌트인 Sequence 객체기 때문에 인덱싱과 슬라이싱, 합과 곱 연산 가능

# 1. 인덱싱
print(s[-3])
# 'a'

# s[2] = 'p'
# 특정 인덱스에 대한 item assignment는 불가능

# 2. 슬라이싱
print(s[:-2])
# 'Pla'

# 3. 합과 곱 연산
print(s + '!' * 3)
# 'PlanB!!!'