# Python 코드에서 오류가 발생하는 경우, Error가 발생하며 코드는 그대로 중지된다
print(3 / 0)
# ZeroDivisionError: division by zero

# Python에서는 오류 핸들링을 위해 try - except - else - finally 구문을 사용한다

try:
    print(3 / 0)
except:
    print('Error!')

# 특정 에러만 잡아내기 위해 except 뒤에 에러를 명시해줄 수도 있다
try:
    print(3 / 0)
except ZeroDivisionError:
    # except [ErrorClass]
    # except를 broad하게 잡는 것보다 이처럼 명시하는 것이 더 좋다
    print('ZeroDivisionError')

# 에러를 여러 개 잡을 때
try:
    print(3 / 0)
except (ZeroDivisionError, ValueError):
    print('Error!')

# except 블럭에서만 사용 가능한 오류 객체를 가져올 수 있다
try:
    print(3 / 0)
except ZeroDivisionError as e:
    # except [ErrorClass] as [obj]
    print('ZeroDivisionError - {}'.format(e.args))

# try에서 에러가 발생하지 않은 경우 else 블럭이 호출되며,
# 에러 발생 여부에 관계없이 finally가 호출된다
try:
    print(3 / 1)
except ZeroDivisionError as e:
    print('ZeroDivisionError - {}'.format(e.args))
else:
    print('No error')
finally:
    print('Finally!')