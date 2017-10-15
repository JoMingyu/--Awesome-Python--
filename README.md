# TIL-Python
Interpreter, Object-Oriented, Dynamically Typed, Iteractive language

## Python Best Practices
[The Best of the Best Practices Guide for Python] <https://gist.github.com/sloria/7001839>  
[Flask Hacks and Best Practices] <http://slides.skien.cc/flask-hacks-and-best-practices/>

## My own projects using Python
### PyPI Library
[PyPI] <https://github.com/JoMingyu/TourAPI>  
[PyPI] <https://github.com/JoMingyu/CoinAPI>  
[PyPI] <https://github.com/JoMingyu/Schapi>  

### Flask
[Flask] <https://github.com/Seoul-People/Seoul-People_Backend>  
[Flask] <https://github.com/Daedongyo-Tourism/Daedongyo-Tourism_Backend>  
[Flask] <https://github.com/DSM-GRAM/Artist-Soongsil>  
[Flask] <https://github.com/JoMingyu/Daejeon-People>  

[Flask] <https://github.com/JoMingyu/DMS-Baseline-API>  
[Flask] <https://github.com/JoMingyu/DMS-Migrates-to-Python>  
[Flask] <https://github.com/JoMingyu/Whale-SideDish>  

[Flask] <https://github.com/DSM-GRAM/Artist>  
[Flask] <https://github.com/JoMingyu/Bubble>  
[Flask] <https://github.com/JoMingyu/Server-Quickstart-Flask>  
[Flask] <https://github.com/JoMingyu/Voltalk>  
[Flask] <https://github.com/JoMingyu/Ccomet-Howmuch-ExchangeRate>  
[Flask] <https://github.com/JoMingyu/Helpable>

## Helpable Utilities
[Pigar] <https://github.com/damnever/pigar>  
[Twine] <https://github.com/pypa/twine>  
[Isort] <https://github.com/timothycrosley/isort>

## Python
동적 타이핑 인터프리터 언어. 함수와 변수명에 스네이크 케이스, 클래스명에 파스칼 케이스를 사용. 반복 가능한 객체에 부여해 주는 syntactic sugar들이 많다. 현재는 언어의 유연함이나 Django와 Tensorflow로 인해 엄청나게 많은 사람들이 사용하고 있다.

다른 언어들에서는 쉽게 찾아볼 수 없는 파이썬만의 독특한 매력이 있다. Comprehension과 Ternary operator, unpack, lambda 등 코드를 한 줄에 표현하는 것을 좋아한다. 'Life is short, you need python'이라는 말이 생겨날 정도로 파이썬은 생산성이 매우 높은 언어다. 현재의 소프트웨어 판에 참 잘 어울리는 '모듈화' 개념이 있으며 PEP로 인해 여러 개발자들 사이에 코딩 스타일이 굉장히 비슷하다. IDE 단에서 코딩 컨벤션을 강력하게 잡는다.

자바에서 private 필드에 접근하고 싶다면 리플렉션을 사용하거나, 클래스의 소스코드 자체를 편집해 버리면 된다. 파이썬에는 이에 대해 문화적인 차이가 존재한다. 파이썬에서는 private와 같은 보안에 대한 속임수를 없애버리고 프로그래머로 하여금 책임감을 갖도록 장려한다. 그리고 이는 실제로 효과가 있다고 한다. PEP8에서는 변수명 앞에 언더스코어(_, 또는 __)를 붙이는 방법으로 protected, 또는 private 변수를 모방한다. 원칙적으로 '해당 변수로의 접근이 막혀있지 않더라도 접근하지 말라'라는 의미로 사용된다.

파이썬은 C로 구현되어 있다. .NET 위에서 동작하는 IronPython, C기반 파이썬에서 스택을 없앤 Stackless Python, JVM 위에서 돌아가는 Jython, 파이썬 자체로 구현된 Pypy등이 있다. 파이썬으로 할 수 있는 일들은 여기서 볼 수 있다.

<https://github.com/vinta/awesome-python>

## 알아 두면 쓸데 많은 파이썬의 개념들
- 모듈과 패키지 개념
- 언더스코어(_)의 활용
- Python 3.6의 fstring
- Comprehension과 unpack
- Dictionary와 List의 여러가지 표현(instance.__dict__, _dict['new_name'] = _dict.pop('legacy_name'), sorted(_list, key=lambda) 등)
- lambda
- ternary operator
- For loop 내부에서 수행되는 Shallow copy, Deep copy
- docstring in function
- assertion
- Decorators
- with-as, import-as
- datetime, pickle, re, json, numpy, PIL, urllib 등의 메이저한 패키지
- pip(requirements.txt, pigar, setup.py, twine)
