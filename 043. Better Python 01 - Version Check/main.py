# 파이썬에는 2개의 메이저 버전이 있다(Python 2, Python 3)
# 어떤 파이썬 버전을 사용하고 있는지를 아는 것은 정말 중요하다
# Python 2를 지원하는 패키지, Python 3를 지원하는 패키지가 다르고(이전의 Pandas나 MySQL-Python 등)
# 문법적인 차이(String formatting 등), 내부적인 차이(Python 2의 xrange, Python 3의 range)들도 존재하기 때문
import sys

print(sys.version_info)
# 파이썬은 버전을 major, minor, micro로 나누고 있음
print(sys.version)

# python --version, python -V 명령을 통해서도 확인할 수 있다
import os

os.system('python --version')
os.system('python -V')
