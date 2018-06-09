# https://docs.python.org/3/library/argparse.html
import argparse
# https://github.com/python/cpython/blob/3.6/Lib/argparse.py
# argparse 모듈을 이용하면 커맨드 라인에서 실행 시의 인자를 파싱할 수 있다
# sys.argv를 사용해도 되지만, argparse를 이용하면 훨씬 쉽게 관리할 수 있다

parser = argparse.ArgumentParser(description='명령행 인자를 쉽게 설정하는 argparse')
# Parser 생성

parser.add_argument('primary', help='This is primary argument')
# add_argument() 메소드를 이용해 인자를 추가
# https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
# 인자는 파이썬의 함수처럼 위치 인자(positional argument)와 선택 인자(optional argument)로 나뉨
# 위는 위치 인자 설정. 기본적으로 required가 True이다

parser.add_argument('-o', '--option', dest='opt', type=int, required=True)
# 선택 인자 설정
# --로 시작해야 하며, 짧은 버전도 같이 설정해줄 수 있다
# 선택 인자는 기본적으로 required가 False인데, 직접 설정해줄 수 있다
# required를 설정함과 동시에 선택 인자의 짧은 버전도 같이 설정해 주자

args = parser.parse_args()

print(args.primary)
print(args.opt)
