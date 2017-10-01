import os

# 시스템의 환경 변수에 접근하기 위해 os 모듈의 environ 필드를 읽는다
# Windows에선 환경 변수 편집기, Ubuntu에선 export VARNAME="value" 방식으로 환경 변수를 추가한다
data = dict(os.environ)
for k, v in data.items():
    print(k, v)

try:
    print(os.environ['Test'])
except KeyError:
    print('Key Error')
    # 해당 환경 변수가 없을 경우 KeyError가 뜬다
    # 이를 해결하기 위해 environ 필드를 읽는 방법을 문법적으로 개선하거나, getenv 함수를 이용한다

print(os.environ.get('Test', default='Default value'))
print(os.getenv('Test', default='Default value'))
