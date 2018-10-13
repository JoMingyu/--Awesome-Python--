# 논리 연산자는 하나 이상의 boolean에 대한 논리적인 연산을 위해 사용한다
# 타 언어의 &&, ||, !은 각각 Python에서 and, or, not으로 표현된다

# C와 같은 언에서의 and, or 연산은 두 boolean의 피연산자에 대한 논리 연산의 결과(true/false)로 boolean을 반환하지만
# Python은 타입들에 bool 평가가 가능해서, and와 or는 피연산자 중 하나를 그대로 반환한다(bool condition이 아닌 value를 반환)
# 이 특징 때문에 Python의 논리 연산자를 'Boolean Operator'라고 부르기도 한다

# -- or
print(1 or 0) # 1
print(1.0 or 3) # 1.0
print(0 or 3) # 3
# [conditionA] or [conditionB]
# conditionA가 True로 평가되면 'or'의 조건에 충족하므로 conditionA를 반환하고,
# 그렇지 않으면 conditionB를 반환

# -- and
print(1 and 3) # 3
print(0 and 3) # 0
print('' and '') # ''
# [conditionA] and [conditionB]
# conditionA가 False로 평가되면 'and'의 조건에 충족하지 않으므로 False로 평가된 conditionA를 그대로 반환하고,
# 그렇지 않으면 conditionB를 반환

# -- not
print(not 1) # False
print(not '') # True
# not [condition]
# condition이 True로 평가되면 False를 반환하고, 그렇지 않으면 True를 반환

# -- in & not in
# Iterable 객체 안에 특정 요소가 들어 있는지(in)와 들어 있지 않은지(not in)를 평가할 수 있다
print(1 in [1, 2, 3, 4, 5]) # True
print(1 not in {3, 4, 5}) # True

# -- is & not is
# 두 객체의 주소값을 비교(is)할 수 있다
print('PlanB' is 'PlanB') # True
print('PlanB' is not 'PlanB') # False
