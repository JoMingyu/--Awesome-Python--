import os
# 파이썬의 주요 모듈 중 하나인 os 모듈
# 운영체제에서 제공되는 기본적인 기능들을 다룰 수 있다

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
# 환경 변수

print(os.getpid())
# 프로세스 id

os.system('calc')
# 커맨드 실행

# 디렉터리 하위를 순회하는 walk, src를 dst로 리네임하는 rename 등 많고 편리한 함수들이 많다
