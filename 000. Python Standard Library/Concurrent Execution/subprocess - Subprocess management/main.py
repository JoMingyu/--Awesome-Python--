# https://docs.python.org/3/library/subprocess.html
import subprocess
# https://github.com/python/cpython/blob/3.6/Lib/subprocess.py
# https://www.python.org/dev/peps/pep-0324/
# subprocess 모듈은 새로운 프로세스를 생성하고, 그들의 input/output/error pipe에 연결하고, 반환 코드를 얻어올 수 있게 돕는다

print(subprocess.call(['ls']))
# 가장 간단한 형태의 subprocess 호출
# 성공하는 경우 0이 리턴된다

print(subprocess.check_call(['ls']))
# call() 함수는 서브 프로세스를 통해서 주어진 명령을 실행하고 리턴하나, 이 과정에서 리턴 코드를 받아오긴 하지만
# 해당 명령이 처리에 실패하고 비정상 종료를 하는 경우에도 이후의 코드가 무사히 실행이 될 것이다
# call()이 성공하면 리턴 코드가 0이 반환되긴 하지만, 아예 서브 프로세스에 의한 처리가 성공하는 것이 보장되어야 하는 경우 check_call을 사용한다
# 처리가 실패하는 경우, CalledProcessError를 raise한다

print(subprocess.check_output(['ls'])
# 서브프로세스를 실행하고 해당 커맨드에 대한 출력 문자열을 리턴
# 실행되어 출력된 결과를 문자열로 받고 싶을 때 사용한다
# check_call처럼 리턴 코드가 0이 아닌 경우, check_call처럼 CalledProcessError를 raise한다
