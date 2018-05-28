""" This function supports dynamic execution of Python code. """
# exec 함수는 문자열로 이루어진 표현식을 인자로 받는다.
# exec 함수는 인자로 받은 문자열을 실행해준다. (단, python 인터프리터가 해석할 때 구문오류가 없어야한다)

# example1 : 간단하게 a 에 5를 할당하고 a 에 5를 더해주는 결과를 낼 수 있다.
a = 5
ex = 'a = a + 5'
exec(ex)
print(a)

# example2 : 문자열 내에 표현식을 인터프리터가 해석할 수 있도록 넘겨주는 함수이므로 'print()' 와 같은 함수들도 당연히 실행된다.
a = 4
b = 3
ex2 = 'print("result = {}".format(str(a+b)))'
exec(ex2)
