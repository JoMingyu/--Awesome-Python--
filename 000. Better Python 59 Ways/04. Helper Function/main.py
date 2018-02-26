# 파이썬에서 복잡하고 반복되는 프로세싱을 하게 되는 경우 코드의 가독성이 떨어지는 경우가 많다.
# 이럴 때에는 Helper function 을 만들면 가독성을 높일 수 있다.
# Helper function 을 쓰는 당신! 힙한 pythonista 시군요!

# 예시를 들어 쿼리스트링을 디코드 해야 한다고 하자
from urllib.parse import parse_qs
color = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(color))
# color = {'red': ['5'], 'green': ['0'], 'blue': ['']}


# color에서 red, green, blue 에 있는 리스트의 값을 int 형으로 값을 뽑아보자.
# 만약 값이 없다면 기본값 0을 넣기로 하자
red = int(color.get('red')[0] or 0)
green = int(color.get('green')[0] or 0)
blue = int(color.get('blue')[0] or 0)

print('red: {}'.format(red))
print('green: {}'.format(green))
print('blue: {}'.format(blue))

# 딕셔너리에서 변수에 값을 뽑아 넣는 코드의 가독성이 매우 떨어진다.
# 이를 해결할 수 있는 함수를 만들어 보자.
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

# 이렇게 멋진 Helper function 을 만들었으니 사용해보자.
red = get_first_int(color, 'red')
green = get_first_int(color, 'green')
blue = get_first_int(color, 'blue')

print('red: {}'.format(red))
print('green: {}'.format(green))
print('blue: {}'.format(blue))

# Helper function 을 사용하니 가독성이 훨씬 좋아진 것을 볼 수 있다.
