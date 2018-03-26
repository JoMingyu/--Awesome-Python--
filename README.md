# Awesome-Python
Interpreter, Object-Oriented, Dynamically Typed, Iteractive language

<https://www.python.org/>

TIL로 꾸준한 공부와 복습을 위해 정리하던 레포가 점점 커져 예제 저장소가 되었습니다. 제가 정리해 둔 예제들을 통해 저만 복습하는 게 아니라, 많은 파이썬 사용자들에게 도움이 되었으면 좋겠습니다. 필요한 예제가 있다면 Issue로 남기고, 기존 예제 개선/새로운 예제를 만들어 PR해 주시는 것도 큰 도움이 됩니다.

## Python
C로 구현되었고, 1991년에 발표된 인터프리터, 동적 타이핑, 바이트코드 컴파일, 객체지향을 지원하는 멀티 패러다임 언어입니다. 현재 실무와 교육 양 쪽에서 높은 점유율을 보이고 있습니다. 가장 큰 특징이자 장점은 '반복 가능한 객체'이며, 이 덕분에 Comprehension과 unpack, enumeration과 같은 파이썬만의 강력한 개념이 생겨났습니다. 현재는 언어의 유연함이나 Glue Language로서 생겨난 Django, Flask, Tensorflow, Keras 등의 수많은 프레임워크와 라이브러리로 인해 수많은 사람들이 사용하고 있습니다. 문법이 쉬워 배우기는 쉽지만, 다른 언어가 다 그렇듯 잘 쓰기는 어렵습니다.

다른 언어들에서는 쉽게 찾아볼 수 없는 파이썬만의 독특한 매력이 있는데, 바로 '문화'입니다. 파이썬이 성장하며 '가장 아름다운 하나의 답이 존재한다'라는 파이썬의 명제가 성장해 왔습니다. 다른 언어들의 코딩 스타일은 각자의 취향에 맞게 진화하는 반면(C 계열의 중괄호 위치 등), 파이썬은 위의 철학들을 만족시키는 하나의 스타일로 진화해 왔습니다. 이에 PEP8이라는 제안서(코드 스타일 가이드)가 보편적인 코딩 컨벤션으로 자리를 잡으며 파이썬스러움(Pythonic)이라는 단어가 유명해지게 되었는데, 복잡하지 않으면서 의미가 명확하고, 심플한 파이썬의 철학을 따르는 코드들을 지칭하는 개념입니다. 그래서 처음 보는 개발자 둘이 파이썬 코드를 작성하더라도, 코드의 레이아웃이나 컨벤션들이 거의 비슷합니다.

파이썬은 C로 구현되어 있습니다. 일반적으로 생각하는 파이썬은 CPython을 지칭합니다. .NET 위에서 동작하는 IronPython, CPython에서 인터프리터를 호출 스택과 분리한 Stackless Python, 바이트코드로 컴파일되어 JVM 위에서 돌아가는 Jython, 파이썬 자체로 구현된 Pypy등이 있습니다.

<https://github.com/vinta/awesome-python>

한 번만 읽으면 졸업할 수 있는 책과 두고두고 다시 보는 책이 있습니다. 첫 번째 부류의 쉬운 책은 많은데, 두 번째 부류의 비급같은 책들은 적습니다. 특히 파이썬은 '쉽다'라는 언어적 특성 때문에 그런 경향이 더 많습니다. 쉽다는 장점이 의외로 단점을 가져오는데, 자유롭게 쓸 수 있는 시점이 빨리 다가오기 때문에 '다 알았다'는 느낌이 들어서 배우기에서 빨리 손을 터는 경우가 많다는 것입니다. 그래서 C++은 적은 초보자와 많은 전문가를 가지고 있고, Python은 많은 초보자와 적은 전문가를 가지고 있습니다. 프로그래밍 언어는 단순히 문제를 해결하기 위한 도구일 뿐이지만, 고급자로 올라서기 위해 참고할 만한 자료들이 그리 많지 않습니다. 아래는 제가 '두고두고 다시 보는 책'들의 목록입니다.

- 파이썬 코딩의 기술(Effective Python)
- 파이썬을 여행하는 히치하이커를 위한 안내서
- 실전 파이썬 프로그래밍
- 전문가를 위한 파이썬
- 엔지니어를 위한 파이썬
- 고성능 파이썬

## Python의 패키지 관리
pip를 사용하고, 모든 외부 라이브러리들은 <a href="https://pypi.python.org/">Python Package Index - PyPI</a>에서 관리됩니다.

## Tutorials
<a href="https://wikidocs.net/book/1">점프 투 파이썬</a>  
<a href="http://tcpschool.com/python/intro">TCPSchool - Python</a>  
<a href="https://docs.python.org/3/tutorial/">The Python Tutorial</a>

## 읽을거리
<a href="https://tech.ssut.me/2017/04/06/yes-python-is-slow-and-i-dont-care/">네 Python은 느립니다. 하지만 저는 신경쓰지 않습니다.</a>  
<a href="https://www.python.org/dev/peps/pep-0008/">PEP8 Style Guide</a>  
<a href="https://github.com/SigmaQuan/Better-Python-59-Ways">Better Python 59 Ways</a>  
<a href="https://gist.github.com/sloria/7001839">The Best of the Best Practices Guide for Python</a>   
<a href="https://github.com/faif/python-patterns">A collection of design patterns/idioms in Python</a>  
<a href="http://book.pythontips.com/en/latest/ternary_operators.html">Python Tips</a>

## 웹 프레임워크
- Micro : Flask, Bottle
- Full-Stack : Django

## 진입장벽
파이썬 코드는 프로그래밍을 한 번도 해보지 않은 사람조차도 소스 코드를 통해 프로그램이 어떤 일을 하는지 이해할 정도로 접근하기 쉬운데, 바로 가독성 때문입니다. 가독성(readability)은 파이썬 디자인의 핵심이며, 코드 작성자가 코드를 작성하는 데 소요하는 시간보다 수많은 사람이 코드를 읽는데 소요하는 시간이 훨씬 길다는 인식이 바탕에 깔려 있습니다.

파이썬 코드가 비교적 쉽게 이해되는 것은 완전한 코드 스타일 가이드라인 모음집(PEP8과 PEP20 개선 제안)과 Pythonic이라는 관용어 때문입니다. 베테랑 파이썬 개발자가 코드의 일부분을 '파이썬스럽지' 않다고 한다면, 그 부분은 일반적으로 통용되는 가이드라인에 따라 작성되지 않았으며, 가독성을 고려한 코드 작성에 실패했음을 의미합니다. 그러나 멍청한 일관성은 소인배의 발상(a foolish consistency is the hobgoblin of little minds)이긴 합니다.

### PEP8(코드 스타일 가이드)
<a href="https://www.python.org/dev/peps/pep-0008/">PEP8</a>은 파이썬을 위한 코드 스타일 가이드이며 네이밍, 코드 레이아웃, 공백 등의 스타일 주제를 다룹니다. 파이썬의 정석적인 코드 스타일을 배우고 싶다면, PEP8을 정독하는 것도 좋습니다. 대체로 파이썬 코드를 작성할 때에는 PEP8을 준수하는 것이 좋습니다. 코드 스타일이 통일되면 여러 개발자가 코드의 일관성을 유지하며 개발할 수 있게 됩니다. 작성하고 있는 파이썬 코드가 PEP8을 잘 따르고 있는지 확인하고 싶다면, pep8이라는 유틸리티를 사용해 봅시다.
~~~
$ pip install pep8
$ pep8 sample.py
sample.py:69:11: E401 multiple imports on one line
sample.py:77:1: E302 expected 2 blank lines, found 1
sample.py:88:5: E301 expected 1 blank line, found 0
sample.py:222:32: W602 deprecated form of raising exception
sample.py:544:21: W601 .has_key() is deprecated, use 'in'
~~~

### PEP20(파이썬 계명)
<a href="https://www.python.org/dev/peps/pep-0020/">PEP20</a>은 파이썬 코드를 작성할 때 겪는 의사 결정에 도움을 주는 원리 모움입니다. 파이썬 쉘에서 import this를 입력하면 전문을 볼 수 있습니다. 이름과는 달리 20개가 아닌 19개의 경구만 포함되어 있고, 마지막 경구는 아직 작성되지 않았습니다.
~~~
>>> import this

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
...
~~~
파이썬 계명에 대한 생생한 역사는 <a href="https://www.wefearchange.org/2010/06/import-this-and-zen-of-python.html">배리 바르소의 블로그 게시글 'import this and Zen of Python'</a>에서 확인할 수 있습니다.

### 개인적으로 정말 중요하다 생각하는 팁
- `Comprehension`은 List 말고도 여러 종류가 있습니다 - List Comprehension, Dictionary Comprehension, Set Comprehension, Generator Expression
- 함수가 일급 객체인 파이썬에게 클로저와 데코레이터는 정말 강력한 무기입니다.
- 실행 비용이 비싸지만 동일한 입력을 했을 때 동일한 결과를 반환하는 함수라면 `메모이제이션(@memoize)`을 사용하면 좋습니다.
- 파이썬의 함수는 오버로딩 불가능합니다. 인자에 기본값을 주는 형태로 오버로딩을 흉내낼 수 있으며, 이는 파이썬으로 함수 오버로딩을 구현하기 위해 권장되는 방식입니다.
- 파이썬의 comparison operator는 체이닝 가능합니다.(`5 < a  and a < 7`은 `5 < a < 7`로 표현 가능)
- double leading underscore 방식의 네이밍(`__example`)은 파이썬 인터프리터에 의해 맹글링되기 때문에 private처럼 보이는 효과가 있는데, 이런 특징을 private를 표현하기 위해 사용하진 않아야 합니다.
- 한 슬라이스에 start, end, stride를 함께 쓰지 않는 것이 좋습니다. stride 문법이 종종 예상치 못한 동작을 해서 버그를 만들어내기도 하고, 슬라이싱 문법의 stride 부분이 혼란스러울 수 있습니다.
- Comprehension에서 표현식을 두 개 이상 사용하지 않는 것이 좋습니다. 한 Comprehension에서 for가 두 개 중첩되어 있다고 치면, 읽기 정말 어렵습니다.
- `키워드 전용 인수`를 사용하면 명료성을 강요할 수 있습니다.
- 파이썬에선 기본적으로 `GC`와 `레퍼런스 카운팅`을 통해 메모리를 관리합니다. 다만, 파이썬의 가비지 컬렉팅은 순환 참조를 탐지하고 해결하기 위해 존재하므로 순환 참조를 만들지 않는다고 확신할 수 있으면 `gc.disable()`을 통해 GC를 비활성화시켜도 됩니다.
#### 같은 값으로 채워진 길이가 N인 리스트 만들기
~~~
l = [0] * 4
print(l)
# [0, 0, 0, 0]
~~~
#### Comprehension에 고집을 부리지 않는다
~~~
l = [i for i in range(10000000)] # Comprehension. 메모리에 1000만 개를 미리 준비하므로 리소스 낭비 가능성이 높음
l = (i for i in range(10000000)) # Generator. yield를 이용해 원하는 시기에 다음 요소에 접근할 수 있는 iterator
print(next(l))
# 0
print(next(l))
# 1
~~~
#### 인덱스 기반 loop는 Iterator에 최적화된 enumerate() 활용
~~~
l = [i for i in range(10)]
for i in range(len(l)):
    print(i, l[i])

for i, item in enumerate(l):
    print(i, item)
~~~
#### 함수 인자의 기본값 평가
함수 인자의 기본값은 모듈 로드 시점의 함수 정의 과정에서 딱 한 번만 바인딩됩니다.
~~~
from datetime import datetime
def f(now=datetime.now()):
    print(str(now))
~~~
따라서 값이 동적인 키워드 인수에는 기본값으로 None을 사용하고, 함수의 docstring에 실제 기본 동작을 문서화하는 것이 좋습니다.
#### unpacking
리스트나 튜플의 길이를 알면, 각 element의 값을 여러 개의 변수에 지정할 수 있습니다.
~~~
a, b, c = [1, 2, 3]
a, b = b, a
# 두 변수의 값 치환을 위해 사용

a, *anothers = [1, 2, 3, 4]
# Python 3의 확장 언패킹

a, _, _, b = [1, 2, 3, 4]
# 값 무시
~~~

## Helpable Utilities
<a href="https://github.com/damnever/pigar">Pigar</a>  
<a href="https://github.com/pypa/twine">Twine</a>  
<a href="https://github.com/timothycrosley/isort">Isort</a>

## 파이썬 엑셀 라이브러리 비교
- 읽기 : xlrd, openpyxl
1. 모두 .xlsx 지원, xlrd는 .xls도 지원.
2. 성능은 xlrd이 더 빠름.
3. xlwt가 .xls만 지원하는 것과 다르게 .xlsx도 지원하므로 읽기는 xlrd를 쓰는 편이 좋을 것 같음.

- 쓰기 : xlwt, openpyxl, xlsxwriter, pyexcelerate
1. xlwt를 제외하고 모두 .xlsx를 지원.
2. 문서는 xlsxwriter가 가장 좋음.
3. 성능은 pyexcelerate, xlwt, xlsxwriter, openpyxl 순으로 좋음.
4. 어지간하면 xlsxwriter가 무난한 선택. 성능이 중요하다면 pyexcelerate 쓰자. .xlsx 지원이 필요하면 xlwt는 쓰지 말자.
