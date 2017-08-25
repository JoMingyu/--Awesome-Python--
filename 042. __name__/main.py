from another import say_name
# 파이썬이 언더바를 참 좋아한다
# 테스트를 위해 모듈을 하나 더 만들어 봤다
print(__name__)

say_name()
# __name__은 해당 모듈의 이름이고, 메인 모듈에서 __name__은 '__main__'이 된다
