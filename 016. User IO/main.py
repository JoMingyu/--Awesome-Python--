# Input에 대한 처리도 해보자
user_input = input()
print(user_input)

# input 함수 안에 문자열을 집어넣어서 hint(prompt)를 제공할 수 있다
user_input = input('입력 > ')
print(user_input)

# input 함수의 타입은 무조건 str
# 데이터를 가변으로, 모두 int로 받으려면
user_input = [int(data) for data in input().split(' ')]
