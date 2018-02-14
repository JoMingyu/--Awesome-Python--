# Awesome-Python
Interpreter, Object-Oriented, Dynamically Typed, Iteractive language

<https://www.python.org/>

TIL로 꾸준한 공부와 복습을 위해 정리하던 레포가 점점 커져 예제 저장소가 되었습니다. 제가 정리해 둔 예제들을 통해 저만 복습하는 게 아니라, 많은 파이썬 사용자들에게 도움이 되었으면 좋겠습니다. 필요한 예제가 있다면 Issue로 남기고, 기존 예제 개선/새로운 예제를 만들어 PR해 주시는 것도 큰 도움이 됩니다.

## Python
1991년에 발표된 인터프리터, 객체지향적, 바이트코드 컴파일을 지원하는 동적 타이핑 언어. 가장 큰 특징이자 장점은 '반복 가능한 객체'이다. 반복 가능한 객체 덕분에 Comprehension과 unpack, enumeration과 같은 파이썬만의 강력한 개념이 생겨났다. 현재는 언어의 유연함이나 Glue Language로서 생겨난 Django, Flask, Tensorflow, Keras 등의 수많은 프레임워크와 라이브러리로 인해 엄청나게 많은 사람들이 사용하고 있다. 문법이 쉬워 배우기는 쉽지만, 다른 언어가 다 그렇듯 잘 쓰기는 어렵다.

다른 언어들에서는 쉽게 찾아볼 수 없는 파이썬만의 독특한 매력이 있다. 파이썬이 성장하며 '가장 아름다운 하나의 답이 존재한다'라는 파이썬의 명제 또한 성장해 왔다. 따라서 다른 언어들의 코딩 스타일은 각자의 취향에 맞게 진화하는 반면(C 계열의 중괄호 위치 등), 파이썬은 위의 철학들을 만족시키는 하나의 스타일로 진화한다. 이에 PEP8이라는 제안서(코드 스타일 가이드)가 보편적인 코딩 컨벤션으로 자리를 잡으며 파이썬스러움(Pythonic)이라는 단어가 유명해지게 되었는데, 복잡하지 않으면서 의미가 명확하고, 심플한 파이썬의 철학을 따르는 코드들을 지칭하는 개념이다.

파이썬은 C로 구현되어 있다. 일반적으로 생각하는 파이썬은 CPython을 지칭한다. .NET 위에서 동작하는 IronPython, CPython에서 인터프리터를 호출 스택과 분리한 Stackless Python, 바이트코드로 컴파일되어 JVM 위에서 돌아가는 Jython, 파이썬 자체로 구현된 Pypy등이 있다. 파이썬으로 할 수 있는 일들은 여기서 볼 수 있다.

<https://github.com/vinta/awesome-python>

## Loadmap
- [x] Python basics(data types, if statement, looping, comprehension, function, error, decorator, module, package, ...)
- [x] Flask basics(routing, redirection, template, request, response, blueprint, middleware, aborting, config, testing, ...)
- [x] Basic internal packages(datetime, pickle, random, re, os, json, threading, socket, time, ...)
- [x] Useful external packages(requests, openpyxl, urllib, beautifulsoup, ...)
- [x] Web scraping examples
- [ ] 68 Built-in functions example
- [ ] 33 Built-in keywords example
- [ ] Standard libraries(Built-in packages) example
- [ ] Better Python 59 ways(in 'Effective Python') example
- [ ] Hidden features of Python example
- [ ] Flask code reading
- [ ] Werkzeug code reading

## Pythonic(파이썬스러운) 코드를 작성하기 위한 팁
파이썬 코드는 프로그래밍을 한 번도 해보지 않은 사람조차도 소스 코드를 통해 프로그램이 어떤 일을 하는지 이해할 정도로 접근하기 쉽습니다. 가독성(readability)은 파이썬 디자인의 핵심이며, 코드 작성자가 코드를 작성하는 데 소요하는 시간보다 수많은 사람이 코드를 읽는데 소요하는 시간이 훨씬 길다는 인식이 바탕에 깔려 있습니다.

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
- double leading underscore 방식의 네이밍(__example)은 파이썬 인터프리터에 의해 맹글링되기 때문에 private처럼 보이는 효과가 있는데, 이런 특징을 private를 표현하기 위해 사용하진 않아야 합니다.
- 한 슬라이스에 start, end, stride를 함께 쓰지 않는 것이 좋습니다. stride 문법이 종종 예상치 못한 동작을 해서 버그를 만들어내기도 하고, 슬라이싱 문법의 stride 부분이 혼란스러울 수 있습니다.
- Comprehension에서 표현식을 두 개 이상 사용하지 않는 것이 좋습니다. 한 Comprehension에서 for가 두 개 중첩되어 있다고 치면, 읽기 정말 어렵습니다.
- 키워드 전용 인수를 사용하면 명료성을 강요할 수 있습니다.
- 리스트에서 원하는 값을 제거하려면 del list_[list_.index()]보다 list_.remove() 구문이 더 좋습니다.
#### 같은 값으로 채워진 길이가 N인 리스트 만들기
~~~
l = [0] * 4
print(l)
# [0, 0, 0, 0]
~~~
#### Comprehension에 고집을 부리지 않는다
~~~
l = [i for i in range(10000000)] # Comprehension
l = (i for i in range(10000000)) # Generator
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

## 이 책 좋아요
- 파이썬을 여행하는 히치하이커를 위한 안내서
- 처음 시작하는 파이썬
- 고성능 파이썬
- 파이썬 코딩의 기술(Effective Python)
- 전문가를 위한 파이썬

## 읽을거리
<a href="https://tech.ssut.me/2017/04/06/yes-python-is-slow-and-i-dont-care/">네 Python은 느립니다. 하지만 저는 신경쓰지 않습니다.</a>

## 파이썬 예제 모음
<a href="https://www.programcreek.com/python/">ProgramCreek.com/python</a>

## Best Practices
<a href="https://www.python.org/dev/peps/pep-0008/">PEP8 Style Guide</a>  
<a href="https://github.com/SigmaQuan/Better-Python-59-Ways">Better Python 59 Ways</a>  
<a href="https://gist.github.com/sloria/7001839">The Best of the Best Practices Guide for Python</a>   
<a href="https://github.com/faif/python-patterns">A collection of design patterns/idioms in Python</a>  
<a href="http://book.pythontips.com/en/latest/ternary_operators.html">Python Tips</a>

## My own projects using Python
### PyPI Library
<a href="https://github.com/JoMingyu/Flask-restful-autoroute">Flask-restful-autoroute</a>  
<a href="https://github.com/JoMingyu/Reflections">Reflections</a>  
<a href="https://github.com/JoMingyu/TourAPI">TourAPI</a>  
<a href="https://github.com/JoMingyu/CoinAPI">CoinAPI</a>  
<a href="https://github.com/JoMingyu/Schapi">Schapi</a>

### Flask
<a href="https://github.com/Highthon-Stepping-Stone/Stepping-Stone-Backend">2회 하이톤 : 디딤돌</a>
<a href="https://github.com/TblMaker/TableMaker-Backend">TableMaker</a>
<a href="https://github.com/Modu-Buy-App/Modu-Buy_Backend">모두바이</a>  
<a href="https://github.com/DSM-DMS/Project-DMS-Backend">DMS Backend Rebuilding</a>  
<a href="https://github.com/Gongjung-Bunhae-App/Gongjung-Bunhae_Backend">14회 AppJam : 공중분해</a>  
<a href="https://github.com/JoMingyu/BookCheck-Backend">책첵</a>  
<a href="https://github.com/JoMingyu/Bubble-Backend">SW융합 해카톤대회 수상작 서비스화 : Bubble</a>  
<a href="https://github.com/Ding-Dong-App/Ding-Dong_Backend">2017 드림쉐어 메디컬 해커톤 : DingDong</a>  
<a href="https://github.com/Tellin-Inner-Communication/Tellin_Backend">Tellin Backend Part</a>  
<a href="https://github.com/JoMingyu/Flask-Large-Application-Example">Flask Large Application Example</a>  
<a href="https://github.com/DSM-GRAM/Jumpup-CompanyView">동아리 Jumpup : CompanyView</a>  
<a href="https://github.com/Smart-Living-Knock-Knock/Knock-Knock_Backend">스마트리빙 메이커톤 : Knock Knock</a>  
<a href="https://github.com/KimGenius/HighThon-Trump">1회 하이톤 : TT</a>  
<a href="https://github.com/DSM-DMS/DSM-Dormitory-Management-System">DMS</a>  
<a href="https://github.com/Daedongyo-Tourism/Daedongyo-Tourism_Backend">2017 스마트 관광앱 공모전 : 대동여관광</a>  
<a href="https://github.com/Seoul-People/Seoul-People_Backend">2017 서울시 앱 공모전 : 서울사람</a>  
<a href="https://github.com/JoMingyu/Pick">안드로이드 실시간 사전 : Pick</a>  
<a href="https://github.com/JoMingyu/WakeHeart">Java 프로젝트 도와주기 : WakeHeart</a>  
<a href="https://github.com/DSM-GRAM/Artist-Soongsil">동아리 경진대회 리메이크</a>  
<a href="https://github.com/JoMingyu/Daejeon-People">2017 Java 프로젝트 : 대전사람</a>  
<a href="https://github.com/JoMingyu/Whale-SideDish">Whale 확장앱 : SideDish</a>  
<a href="https://github.com/DSM-GRAM/Artist">17회 청소년동아리 경진대회 : Artist</a>  
<a href="https://github.com/JoMingyu/Bubble">4회 대한민국 SW융합 해카톤대회 : Bubble</a>  
<a href="https://github.com/JoMingyu/Voltalk">2회 에너지 해커톤 : Voltalk</a>  
<a href="https://github.com/JoMingyu/Ccomet-Howmuch-ExchangeRate">1차 팀 프로젝트 : Howmuch</a>  
<a href="https://github.com/JoMingyu/Helpable">12회 AppJam : Helpable</a>

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
