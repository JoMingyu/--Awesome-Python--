# Awesome-Python
Interpreter, Object-Oriented, Dynamically Typed, Iteractive language

<https://www.python.org/>

## Python
- 인터프리터, 바이트코드 컴파일
- 타입 시스템 : 강타입, 동적 타이핑
- 타입 추론 : 암시적, 타입을 명시하는 문법 존재(type decoration)
- Scope : 정적, 함수 스코프
- 함수 : 일급 객체
    - 함수의 런타임 익명 생성을 위해 lambda 키워드 지원
- 패러다임 : 멀티 패러다임
- 객체지향 표현 : class 지원
- 메모리 관리 : Reference counting과 가비지 컬렉션
- 컨벤션 : [PEP8](https://www.python.org/dev/peps/pep-0008/)에 명시되어 있으며, Python에서 인정하는 코드 컨벤션에 대한 정확한 가이드라인
- 기타 특별한 점
    - for statement는 foreach 형태로만 사용 가능
    - 비교 연산자를 chaining 가능(a < b < c처럼)
    - switch가 없음
    - 논리 연산자에 기호를 사용하지 않고, 키워드 사용(and, or, not)
    - 강력한 syntactic sugar들이 많음(unpack, enumeration, comprehension 등)
    - 의존성 관리와 가상 환경 구성에 대한 지원이 JavaScript만큼 강력함
    - 라이브러리 생태계가 매우 큼
    - Python을 만든 귀도 반 로썸이 설계한 Python의 데이터 모델을 시작으로 한, Python만의 강력한 일관성 존재
    - 복잡하지 않으면서 의미가 명확하며, 심플한 파이썬의 철학을 따르는 코드들을 뜻하는 'Pythonic'이라는 단어 존재
    - '가장 아름다운 하나의 답이 존재한다'라는 명제를 기본으로 하여, 'Best Practice'를 찾는 개발자들이 많음
    - 다양한 구현체 존재(.NET 기반의 IronPython, 인터프리터를 call stack과 분리한 Stackless Python, JVM 위에서 돌아가는 Jython, 파이썬 자체로 구현된 PyPy 등)

<https://github.com/vinta/awesome-python>

한 번만 읽으면 졸업할 수 있는 책과 두고두고 다시 보는 책이 있습니다. 첫 번째 부류의 쉬운 책은 많은데, 두 번째 부류의 비급같은 책들은 적습니다. 특히 파이썬은 '쉽다'라는 언어적 특성 때문에 그런 경향이 더 많습니다. 쉽다는 장점이 의외로 단점을 가져오는데, 자유롭게 쓸 수 있는 시점이 빨리 다가오기 때문에 '다 알았다'는 느낌이 들어서 배우기에서 빨리 손을 터는 경우가 많다는 것입니다. 그래서 C++은 적은 초보자와 많은 전문가를 가지고 있고, Python은 많은 초보자와 적은 전문가를 가지고 있습니다. 프로그래밍 언어는 단순히 문제를 해결하기 위한 도구일 뿐이지만, 고급자로 올라서기 위해 참고할 만한 자료들이 그리 많지 않습니다. 아래는 제가 '두고두고 다시 보는 책'들의 목록입니다.

- 파이썬 코딩의 기술([Effective Python](https://github.com/bslatkin/effectivepython))
- 파이썬을 여행하는 히치하이커를 위한 안내서([The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/))
- 실전 파이썬 프로그래밍
- 전문가를 위한 파이썬
- 엔지니어를 위한 파이썬
- 고성능 파이썬

## '예제 모음'에서 어느 정도의 '튜토리얼'이 되기까지
처음에 이 저장소가 만들어진 건, 예제들을 모아 파이썬을 복습하기 위함이었습니다. 조금 체계적으로 정리하려던 욕심이 어느 정도의 순서를 만들게 되었고, 블로그에는 강좌에 가까운 글들도 나름대로 조금씩 썼습니다. 블로그에 쓰던 '프로그래밍 입문자를 위한 Python 가이드' 수준의 너무 구체적인 설명과, 설명 없는 단순한 code snippet 모음 사이의 타협점을 찾고자 했고, '알면 좋은데 굳이 지금 설명해봤자 머리만 아픈 개념'은 굳이 그 때 설명하지 않고 나중으로 미루는 형태의 커리큘럼을 구성했습니다. 대부분의 튜토리얼은 함수를 배우기 전에 타입 캐스팅을 알려주고, 반복문을 배우기 전에 list comprehension을 알려주면서 '나중에 다시 배울 개념이다'라고 이해를 뒤로 미룹니다. 이해를 뒤로 미룰 바에, 설명 자체를 뒤로 미루는 게 차라리 더 나을 것 같았습니다.

많은 예제들이 있으나, 모두 외울 필요는 없습니다. Python에서 제공하는 개념이나 문법, 라이브러리들의 의도만 파악하고 '이런 게 있구나' 하며 나중에 떠올릴 수 있을 정도만 되면 됩니다.

변수, 함수의 개념, 객체지향, 조건 분기, 일급 객체, 클로저와 같은 '프로그래밍 자체'에 대한 설명은 지양하고, 파이썬의 개념들만 알차게 구성되어 있습니다. 'Python으로 시작하는 프로그래밍 입문'보다는 'Python 프로그래밍 입문'이라는 제목이 조금 더 잘 어울릴 튜토리얼일 것입니다. 여기에 들어 있는 예제들 + 패키지 관리 + virtualenv + 의존성 관리(setup.py, requirements.txt) + 테스트와 커버리지 리포트 정도만 배우면 그래도 파이썬의 세상에 한걸음은 떼었다고 보면 됩니다 :)

### 패키지 관리
JavaScript 측에서 npm을 쓰는 것처럼, Python에선 pip를 사용합니다.

`$ pip --version`

`pip install`과 `pip uninstall`을 이용해 각각 패키지를 설치하고, 삭제할 수 있습니다. `pip freeze`를 사용하면 현재 pip에 의해 설치되어 있는 모든 패키지를 확인할 수 있습니다. 이를 이용해 아래와 같이, 현재 설치되어 있는 모든 외부 패키지를 제거하는 커맨드를 작성할 수 있습니다.

`$ pip uninstall -y $(pip freeze)`

Linux나 Linux 기반 운영체제(MacOS 등)에선, python2와 python3를 구분하고 있는 것처럼 pip도 pip2(pip)와 pip3를 구분하고 있습니다.

```
$ pip -V
pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)
$ pip3 -V
pip 9.0.3 from /Users/planb/Library/Python/3.6/lib/python/site-packages (python 3.6)
```

### virtual enviroment
virtual environment는 **디렉토리 단위의 격리된 Python 환경**을 구성해 줍니다. 처음엔 '도대체 이게 왜 필요해?'라고 생각했는데, 3개의 프로젝트에서 사용하는 동일한 라이브러리가 서로 모두 버전이 다르고(프로젝트 A에선 Flask 0.12, 프로젝트 B에선 Flask 1.0.1 사용), 한 프로젝트에선 numpy, pytz, six처럼 '이 프로젝트 말고는 다른 데서 안쓸 패키지'가 많은 걸 보고 납득했습니다. 대표적으로 `virtualenv`라는 유틸리티를 사용하며, 이는 서드파티 유틸리티기 때문에 pip를 이용해 설치해야 합니다.

`$ pip install virtualenv`

virtualenv의 사용법은 아주 간단합니다.

`$ virtualenv .venv`

`virtualenv [venv_name]` 형태입니다. 위의 명령을 실행하면 `.venv`라는 이름의 디렉토리가 생기고, 그 밑에 virtualenv가 설치된 Python 버전으로 환경이 구성됩니다. Python의 특정 버전에 대하여 가상 환경을 구성하려면, `--python`이나 `-p` 옵션을 이용해 Python 버전을 명시하면 됩니다.

```
$ virtualenv -p python3 .venv
$ virtualenv --python python2.7 .venv
```

가상 환경을 활성화하려면 아래 명령을 입력합니다.

```
// MacOS, Linux
$ source .venv/bin/activate

// Windows
$ .venv\Scripts\activate.bat
```

가상 환경이 활성화되고 나면, 아래와 같이 쉘의 맨 앞에 가상 환경의 디렉토리명이 표시됩니다.

`(.venv) jomingyuui-MacBook-Pro:temp planb$ `

활성화된 가상환경 안에서 `pip install ...`을 하면, 해당 가상 환경에만 패키지가 설치되어 적용됩니다. 다시 가상 환경에서 빠져나오려면 아래 명령을 입력합니다.

`$ deactivate`

### 의존성 관리
Python에선 의존성 관리를 위해 `setup.py`와 `requirements.txt`를 사용합니다. 둘은 **추상 의존성**과 **구체적인 의존성**의 차이가 있습니다.
#### setup.py
`setup.py`는 일반적으로 **파이썬 라이브러리**의 메타데이터를 명시하기 위해 사용합니다.

```
from setuptools import setup

setup(
    name="MyLibrary",
    version="1.0",
    install_requires=[
        "requests",
        "bcrypt",
    ],
    # ...
)
```

라이브러리를 가져올 URL이나 버전 등이 명시되어 있지 않습니다. 일종의 추상 의존성(abstract dependencies) 형태입니다.

#### requirements.txt
`requirements.txt`는 **파이썬 어플리케이션**(일반적으로 배포 용도)의 의존성 관리를 위해 사용합니다. 파이썬 어플리케이션은 대부분 의존성 라이브러리에 종속되어 있습니다. 이러한 의존 라이브러리의 정보를 저장할 수 있도록 `pip`는 `requirements` 파일을 생성하고, 해당 파일을 통해 라이브러리를 설치하는 기능을 가지고 있습니다. 아래는 `requirements.txt`의 예입니다.

```
requests==1.2.0
bcrypt==1.0.2
```

setup.py에서는 넓은 범위의 버전 지정을 사용하는 편이지만, 어플리케이션은 특정한 버전에 대해 의존성을 가지는 경우가 많습니다. 따라서 이는 **구체적인 의존성**을 위해 사용됩니다. `pip freeze`로도 requirements.txt를 만들어낼 수 있지만, 이는 로컬에 설치된 모든 외부 라이브러리들을 불러오기 때문에 특정 프로젝트에서만 의존성을 뽑아내려면 [pigar](https://github.com/damnever/pigar)를 사용하는 게 더 좋습니다.

```
$ pigar
$ pip3 install -r requirements.txt
```

특정 디렉토리에서만 의존성을 뽑아낼 수도 있습니다. pigar에 `-P` 플래그를 붙입니다.

```
$ pigar -P [PATH]
```

pigar는 외부 라이브러리를 찾은 이후 **pigar가 설치된 site-packages 디렉토리**에서 해당 라이브러리들의 버전을 찾아 등록하기 때문에, virtual environment를 사용하고 있다면 해당 environment에도 pigar를 설치해 주어야 버전에 관한 문제가 생기지 않습니다. 예를 들어, 글로벌 환경에 Flask 0.12가 설치되어 있고, virtual environment에 Flask 1.0.2가 설치되어 있는 상태에서 글로벌 환경에 설치된 pigar를 실행하면 requirements.txt에는 `Flask==0.12`가 적히는 식입니다.

### 테스트
Python은 내장 테스트 라이브러리를 가지고 있고, 유명한 외부 라이브러리들이 많습니다. 그들 중 unittest, pytest, doctest, tox, nose가 가장 인지도 높습니다.

#### 테스트 프레임워크
- unittest : Python에서 기본으로 제공하고 있는, 가장 기본적인 유닛 테스팅 프레임워크입니다. `unittest.TestCase` 클래스를 상속받아 클래스 단위로 테스트 케이스를 정의하고, 테스트 케이스 실행 전/후에 setUp()과 tearDown() 메소드를 실행하며 각 테스트 케이스를 독립적으로 관리할 수 있습니다. Assertion에 대해 많은 메소드들을 지원하고 있습니다.

```
import unittest

def fun(x):
    return x + 1

class SomeTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

- doctest : 특정 함수의 docstring 안에 Python 세션처럼 보이는 텍스트가 있는지를 검색한 후, 해당 세션을 실행하여 텍스트에 써진 대로 정확히 동작하는지를 확인합니다.

```
def square(x):
    """
    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x

if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

- pytest : 테스트 프레임워크입니다. 외부 라이브러리로서, pip를 통해 설치해야 합니다. unittest처럼 무조건 클래스 단위로 테스트 케이스를 정의하지 않아도 돼, 비교적 더 유연합니다. 모든 기능을 갖추지도 않았고, 확장 가능한 테스트 툴도 아니지만, 단순한 문법을 가지고 있어 간단한 테스트를 작성하기에 유용합니다.

```
def fun(x):
    return x + 1

def test_fun_answer():
    assert func(3) == 5
```

커맨드 라인에서 `py.test`를 실행하면 자동으로 테스트를 검색하여 실행합니다.

```
> py.test
=========================== test session starts ============================
platform darwin -- Python 3.6.5, pytest-3.5.1, py-1.5.3, pluggy-0.6.0
collecting ... collected 1 items

test_sample.py F

================================= FAILURES =================================
_______________________________ test_answer ________________________________

    def test_fun_answer():
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:5: AssertionError
========================= 1 failed in 0.02 seconds =========================
```

#### 테스트 툴
- nose : 테스트를 쉽게 찾아 수행할 수 있도록 unittest를 확장한 것입니다. 자동으로 테스트를 발견하기 때문에, 수작업으로 test suite를 만드는 수고를 덜 수 있습니다. 또한 xUnit 호환 테스트 결과, 커버리지 리포트 등과 같이 다양한 플러그인도 제공합니다.

```
$ pip3 install nose
$ python3 -m "nose" tests/
```

Python3의 경우 위처럼 `python3`에 -m 인자로 "nose"를 전달하여 nosetests를 실행할 수 있고, Python2의 경우 별도의 nosetests 커맨드를 실행하면 됩니다. 테스트에 대한 커버리지 리포트를 저장하려면, `--with-coverage` 파라미터를 붙여 줍니다.

```
$ python3 -m "nose" --with-coverage tests/
```

해당 커맨드를 실행한 디렉토리에 `.coverage` 파일이 생겨납니다. 테스트 수행에 대해 조금 더 구체적인 로그를 보려면 `--verbose` 파라미터를 붙여 줍니다.

```
> python3 -m "nose" --verbose tests/
testCreationFailure_alreadyExists (Server.tests.transplant_class.<locals>.C) ... ok
testCreationSuccess (Server.tests.transplant_class.<locals>.C) ... ok
testForbidden (Server.tests.transplant_class.<locals>.C) ... ok
...
```

- tox : 자동화된 테스트 환경 관리와 다양한 인터프리터 설정 하에서의 테스트를 위한 도구입니다. 아래는 tox의 설정 파일인 `tox.ini`의 예입니다.

```
[tox]
envlist = py27,py35,py36,pypy

[testenv]
commands =
    pip3 install -r requirements.txt
    pytest          # or any other test runner that you might use
```

`tox` 커맨드를 실행하면, 해당 디렉토리에서 `tox.ini`를 찾아 거기에 적혀 있는 대로 테스트를 실행합니다.

```
$ pip3 install tox
$ tox
```

## 진입장벽
파이썬 코드는 프로그래밍을 한 번도 해보지 않은 사람조차도 소스 코드를 통해 프로그램이 어떤 일을 하는지 이해할 정도로 접근하기 쉬운데, 바로 가독성 때문입니다. 가독성(readability)은 파이썬 디자인의 핵심이며, 코드 작성자가 코드를 작성하는 데 소요하는 시간보다 수많은 사람이 코드를 읽는데 소요하는 시간이 훨씬 길다는 인식이 바탕에 깔려 있습니다.

파이썬 코드가 비교적 쉽게 이해되는 것은 완전한 코드 스타일 가이드라인 모음집(PEP8과 PEP20 개선 제안)과 Pythonic이라는 관용어 때문입니다. 베테랑 파이썬 개발자가 코드의 일부분을 '파이썬스럽지' 않다고 한다면, 그 부분은 일반적으로 통용되는 가이드라인에 따라 작성되지 않았으며, 가독성을 고려한 코드 작성에 실패했음을 의미합니다. 그러나 멍청한 일관성은 소인배의 발상(a foolish consistency is the hobgoblin of little minds)이긴 합니다.

### PEP8(코드 스타일 가이드)
[PEP8](https://www.python.org/dev/peps/pep-0008/)은 파이썬을 위한 코드 스타일 가이드이며 네이밍, 코드 레이아웃, 공백 등의 스타일 주제를 다룹니다. 파이썬의 정석적인 코드 스타일을 배우고 싶다면, PEP8을 정독하는 것도 좋습니다. 대체로 파이썬 코드를 작성할 때에는 PEP8을 준수하는 것이 좋습니다. 코드 스타일이 통일되면 여러 개발자가 코드의 일관성을 유지하며 개발할 수 있게 됩니다. 작성하고 있는 파이썬 코드가 PEP8을 잘 따르고 있는지 확인하고 싶다면, pep8이라는 유틸리티를 사용해 봅시다.

```
$ pip install pep8
$ pep8 sample.py
sample.py:69:11: E401 multiple imports on one line
sample.py:77:1: E302 expected 2 blank lines, found 1
sample.py:88:5: E301 expected 1 blank line, found 0
sample.py:222:32: W602 deprecated form of raising exception
sample.py:544:21: W601 .has_key() is deprecated, use 'in'
```

### PEP20(파이썬 계명)
[PEP20](https://www.python.org/dev/peps/pep-0020/)은 파이썬 코드를 작성할 때 겪는 의사 결정에 도움을 주는 원리 모움입니다. 파이썬 쉘에서 import this를 입력하면 전문을 볼 수 있습니다. 이름과는 달리 20개가 아닌 19개의 경구만 포함되어 있고, 마지막 경구는 아직 작성되지 않았습니다.

```
>>> import this

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
...
```

파이썬 계명에 대한 생생한 역사는 배리 바르소의 블로그 게시글 ['import this and Zen of Python'](https://www.wefearchange.org/2010/06/import-this-and-zen-of-python.html)에서 확인할 수 있습니다.