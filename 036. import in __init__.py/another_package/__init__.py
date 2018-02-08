# 예를 들어 from flask import Flask 구문에서 flask는 패키지고 Flask는 클래스인데도 불구하고 import가 가능하다
# from flask.app import Flask라면 바로 이해할 수 있을텐데 말이다
# flask 패키지의 __init__.py에선 하위 모듈에 있는 클래스들을 import하는 부분이 있다

# __init__.py는 패키지에 대한 초기화를 담당하는데, 이 범위엔 import도 속해 있다
# __init__.py는 패키지 레벨 모듈이라고 생각하면 된다
from .another_module import AnotherClass
