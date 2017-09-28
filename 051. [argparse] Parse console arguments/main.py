import argparse
# 파이썬 3 표준 라이브러리에 이미 있다
# argparse 모듈을 이용하면 커맨드 라인에서 실행 시의 매개변수를 파싱할 수 있다
# sys.argv를 사용해도 되지만, argparse를 이용하면 훨씬 쉽게 관리할 수 있다

parser = argparse.ArgumentParser(description='명령행 인자를 쉽게 설정하는 argparse')

# option 리스트를 설정
parser.add_argument('primary', help='This is primary argument')
# 위치 인자 설정
# 위치 인자는 기본적으로 required가 True이다

parser.add_argument('--option', help='This is option argument. insert int data', type=int)
# 선택 인자 설정
# --로 시작해야 한다

# 선택 인자는 기본적으로 required가 False인데, 직접 설정해줄 수 있다
# required를 설정함과 동시에 선택 인자의 짧은 버전도 같이 설정해 주자
parser.add_argument('-r', '--required', help='This is option argument but required', required=True)

args = parser.parse_args()

print(args.primary)
print(args.option)
print(args.required)
