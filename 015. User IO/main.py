# 지금까지 출력만 했는데 이제 입력을 알아보자
user_input = input()
print(user_input)
# 참고로 파이썬 2버전은 raw_input 함수를 써야 한다

# input 함수 안에 문자열을 집어넣어서 hint(=prompt)를 제공할 수 있다
user_input = input('입력 > ')
print(user_input)

# input 함수의 타입은 무조건 str
# 타입 캐스팅을 해야 하지만 016에서 알아보도록 하자
