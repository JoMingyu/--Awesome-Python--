from another import say_name
# 테스트를 위해 모듈을 하나 더 만들어 봤다

print(__name__)
say_name()
# __name__은 해당 모듈의 이름이고, 메인 모듈에서 __name__은 '__main__'이 된다

if __name__ == '__main__':
    # 이를 이용해 해당 모듈을 직접 실행했을 때만 작동되어야 하는 코드를 이 if 블럭 안에 넣곤 한다
    print('main module')
