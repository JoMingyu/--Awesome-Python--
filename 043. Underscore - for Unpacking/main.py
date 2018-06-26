# 언더스코어는 Unpacking 시 값을 무시하기 위한 용도로도 사용된다
a, _, _, b = [1, 2, 3, 4]
a, *_, b = [1, 2, 3, 4, 5]
# extended unpacking에도 사용 가능