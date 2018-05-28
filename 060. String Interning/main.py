# 새로운 문자열 객체를 생성할 떄마다 새로운 주소를 할당하는 Java와 다르게
# Python은 String Interning이라고 부르는, 문자열에 관한 메모리 최적화가 내장되어 있다
# 이는 문자열 객체 생성 시, 만들어져 있던 기존의 문자열 객체를 참조하는 것이다

# 1. 길이가 0 또는 1인 문자열
# 2. ASCII 문자/숫자/언더스코어만으로 이루어진 문자열
# 의 경우 string interning이 이루어지며, 동적으로 문자열을 만들어내는 경우에는 intern되지 않는다(컴파일 타임에만 intern)

a = 'PlanB_'
b = 'PlanB_'
print(a is b)
# True
# ASCII 문자/숫자/언더스코어만으로 이루어진 문자열

a = 'PlanB!'
b = 'PlanB!'
print(a is b)
# False
# ASCII 문자/숫자/언더스코어 외의 문자가 들어가 intern되지 않음

a = '!'
b = '!'
print(a is b)
# True
# 길이가 0 또는 1인 문자열