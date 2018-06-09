# https://docs.python.org/3/library/os.html
import os
# https://github.com/python/cpython/blob/3.6/Lib/os.py
# 파이썬의 주요 모듈 중 하나인 os 모듈
# 운영체제에 관한 여러가지 데이터들을 다룰 수 있다

print(os.name)
# 모듈이 import된 OS의 이름

print(os.getcwd())
# 현재 디렉토리

print(os.access('C://', os.F_OK))
# path에 대해 mode에 해당하는 작업이 가능한지 여부 반환
# F_OK : path의 존재 여부
# R_OK : read 가능 여부
# W_OK : write 가능 여부
# X_OK : execute 가능 여부

print(os.listdir(os.getcwd()))
# 해당 경로에 존재하는 파일과 디렉터리들의 리스트 반환

print(os.environ)
# 시스템의 환경 변수에 접근하기 위해 os 모듈의 environ 필드를 읽는다
# Windows에선 환경 변수 편집기, Ubuntu에선 export VARNAME="value" 방식으로 환경 변수를 추가한다
try:
    print(os.environ['Test'])
except KeyError:
    print('Key Error')
    # 해당 환경 변수가 없을 경우 KeyError가 뜬다
    # 이를 해결하기 위해 environ 필드를 읽는 방법을 문법적으로 개선하거나, getenv 함수를 이용한다

print(os.environ.get('Test'))
print(os.getenv('Test', default='Default value'))

print(os.getpid())
# 프로세스 id

os.system('calc')
# 커맨드 실행

# 디렉터리 하위를 순회하는 walk, src를 dst로 리네임하는 rename, mkdir, chown 등 좋은 함수들이 많이 제공된다
