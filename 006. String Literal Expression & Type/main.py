# Python에는 4가지의 문자열 리터럴 표현식이 있다

"planb"
'planb'
"""planb"""
'''planb'''
# char 타입이 없기 때문에, 따옴표의 종류에 상관 없이 모두 문자열로 해석된다

'common'
# 일반적인 문자열 표현은 하나의 작은따옴표로 감싸진 텍스트('...')를 사용하며,
"""Hello from the
other side
"""
# docstring이나 여러 줄에 걸친 문자열을 편히 표현하기 위해 세 개의 큰따옴표로 감싸진 텍스트를 사용한다
# 위의 문자열은 'Hello from the\nother side'로 해석되며,
# 따옴표 세 개로 이루어진 문자열 리터럴은 개행이나 따옴표 사용 등에 대해 비교적 자유롭다

'playerunknown\'s battleground'
"he said \"Let's go pochinki\""
# 작은따옴표로 감싸진 문자열에서 작은따옴표 / 큰따옴표로 감싸진 문자열에서 큰따옴표를 사용하는 경우
# backslash로 이스케이핑해줄 수 있다
