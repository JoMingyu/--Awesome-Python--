# 빌트인 함수 input()을 사용해 커맨드 라인에서 사용자의 입력을 받을 수 있다
data = input()
# Enter(\n)이 들어올 때까지 코드의 실행이 멈춘다

# 함수에 문자열을 전달하여 prompt(hint)를 전달할 수 있다
data = input('Input data > ')

print(type(data))
# input data는 무조건 string 타입

# 데이터를 가변으로, 모두 int 타입으로 받으려면
data = [int(data) for data in input.split(' ')]