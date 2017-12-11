# TIL-Python
Interpreter, Object-Oriented, Dynamically Typed, Iteractive language

<https://www.python.org/>

## Python
1991년에 발표된 인터프리터, 객체지향적, 동적 타이핑 언어. 가장 큰 특징이자 장점은 '반복 가능한 객체'이다. 반복 가능한 객체 덕분에 Comprehension과 Ternary operator, unpack, lambda 와 같은 개념이 생겨났다. 현재는 언어의 유연함이나 Glue Language로서 생겨난 Django, Flask, Tensorflow, Keras 등의 수많은 프레임워크와 리이브러리 인해 엄청나게 많은 사람들이 사용하고 있다. 문법이 쉬워 배우기는 쉽지만, 다른 언어가 다 그렇듯 잘 쓰기는 어렵다.

다른 언어들에서는 쉽게 찾아볼 수 없는 파이썬만의 독특한 매력이 있다. 파이썬이 성장하며 '가장 아름다운 하나의 답이 존재한다'라는 파이썬의 명제 또한 성장해 왔다. Beautiful is better than ugly, Explicit is better than implicit, Simple is better than complex, Complex is better than complicated라는 4가지 철학 또한 수많은 파이썬 개발자들이 명심하고 있다. 따라서 다른 언어들의 코딩 스타일은 각자의 취향에 맞게 진화하는 반면(C 계열의 중괄호 위치 등), 파이썬은 위의 철학들을 만족시키는 하나의 스타일로 진화한다. 이에 PEP8이라는 코딩 컨벤션이 자리를 잡으며 파이썬스러움(Pythonic)이라는 단어가 유명해지게 되었는데, 복잡하지 않으면서 의미가 명확하고, 심플한 파이썬의 철학을 따르는 코드들을 지칭하는 개념이다. 물론, 이와 같이 선택지를 좁히는 게 자유도를 제약한다는 평도 있다.

자바에서 private 필드에 접근하고 싶다면 리플렉션을 사용하거나, 클래스의 소스코드 자체를 편집해 버리면 된다. 파이썬에는 이에 대해 문화적인 차이가 존재한다. 파이썬에서는 private와 같은 보안에 대한 속임수를 없애버리고 프로그래머로 하여금 책임감을 갖도록 장려한다. 그리고 이는 실제로 효과가 있다고 한다. PEP8에서는 변수명 앞에 언더스코어(_, 또는 __)를 붙이는 방법으로 protected, 또는 private 변수를 모방한다. 원칙적으로 '해당 변수로의 접근이 막혀있지 않더라도 접근하지 말라'라는 의미로 사용된다.

파이썬은 C로 구현되어 있다. .NET 위에서 동작하는 IronPython, C기반 파이썬에서 스택을 없앤 Stackless Python, JVM 위에서 돌아가는 Jython, 파이썬 자체로 구현된 Pypy등이 있다. 파이썬으로 할 수 있는 일들은 여기서 볼 수 있다.

<https://github.com/vinta/awesome-python>

## Python Best Practices
[The Best of the Best Practices Guide for Python] <https://gist.github.com/sloria/7001839>  
[Python Tips] <http://book.pythontips.com/en/latest/ternary_operators.html>

## My own projects using Python
### PyPI Library
[Flask-restful-autoroute] <https://github.com/JoMingyu/Flask-restful-autoroute>  
[Reflections] <https://github.com/JoMingyu/Reflections>  
[TourAPI] <https://github.com/JoMingyu/TourAPI>  
[CoinAPI] <https://github.com/JoMingyu/CoinAPI>  
[SchAPI] <https://github.com/JoMingyu/Schapi>

### Flask
[2017 드림쉐어 메디컬 해커톤 : DingDong] <https://github.com/Ding-Dong-App/Ding-Dong_Backend>  
[Tellin Backend Part] <https://github.com/Tellin-Inner-Communication/Tellin_Backend>  
[Flask Large Application Example] <https://github.com/JoMingyu/Flask-Large-Application-Example>  
[동아리 Jumpup : CompanyView] <https://github.com/DSM-GRAM/Jumpup-CompanyView>  
[스마트리빙 메이커톤 : Knock Knock] <https://github.com/Smart-Living-Knock-Knock/Knock-Knock_Backend>  
[1회 하이톤 : TT] <https://github.com/KimGenius/HighThon-Trump>  
[DMS] <https://github.com/DSM-DMS/DSM-Dormitory-Management-System>  
[2017 스마트 관광앱 공모전 : 대동여관광] <https://github.com/Daedongyo-Tourism/Daedongyo-Tourism_Backend>  
[2017 서울시 앱 공모전 : 서울사람] <https://github.com/Seoul-People/Seoul-People_Backend>  
[안드로이드 실시간 사전 : Pick] <https://github.com/JoMingyu/Pick>  
[Java 프로젝트 도와주기 : WakeHeart] <https://github.com/JoMingyu/WakeHeart>  
[동아리 경진대회 리메이크] <https://github.com/DSM-GRAM/Artist-Soongsil>  
[2017 Java 프로젝트 : 대전사람] <https://github.com/JoMingyu/Daejeon-People>

[Whale 확장앱 : SideDish] <https://github.com/JoMingyu/Whale-SideDish>

[17회 청소년동아리 경진대회 : Artist] <https://github.com/DSM-GRAM/Artist>  
[4회 대한민국 SW융합 해카톤대회 : Bubble] <https://github.com/JoMingyu/Bubble>  
[Flask Server Quickstart] <https://github.com/JoMingyu/Server-Quickstart-Flask>  
[2회 에너지 해커톤 : Voltalk] <https://github.com/JoMingyu/Voltalk>  
[1차 팀 프로젝트 : Howmuch] <https://github.com/JoMingyu/Ccomet-Howmuch-ExchangeRate>  
[12회 AppJam : Helpable] <https://github.com/JoMingyu/Helpable>

## Helpable Utilities
[Pigar] <https://github.com/damnever/pigar>  
[Twine] <https://github.com/pypa/twine>  
[Isort] <https://github.com/timothycrosley/isort>

## 알아 두면 쓸데 많은 파이썬의 개념들
- 모듈과 패키지 개념
- 언더스코어(_)의 활용 : protected 표현, 매직 메소드 등
- Python 3.6의 fstring
- Comprehension과 unpack
- Dictionary와 List의 여러가지 표현(_dict['new_name'] = _dict.pop('legacy_name'), sorted(_list, key=lambda) 등)
- lambda
- ternary operator(삼항 연산자) : if ternary&tupled ternary
- 단순 객체복제, Shallow copy, Deep copy의 차이
- docstring
- assertion
- with-as, import-as
- datetime, pickle, re, json, urllib, bs 등의 메이저한 패키지
- pip(requirements.txt, pigar, setup.py, twine)

## 팁
- double leading underscore 방식의 네이밍(__example)은 파이썬 인터프리터에 의해 맹글링되기 때문에 private처럼 보이는 효과가 있는데, 이런 특징을 private를 표현하기 위해 사용하진 않아야 합니다.
- 한 슬라이스에 start, end, stride를 함께 쓰지 않는 것이 좋습니다. stride 문법이 종종 예상치 못한 동작을 해서 버그를 만들어내기도 하고, 슬라이싱 문법의 stride 부분이 혼란스러울 수 있습니다.
- map과 filter 대신 Comprehension을 사용합시다.
- Comprehension에서 표현식을 두 개 이상 사용하지 않는 것이 좋습니다. 한 Comprehension에서 for가 두 개 중첩되어 있다고 치면, 읽기 정말 어렵습니다.
- Comprehension의 크기가 큰데도 불구하고 Comprehension에 고집을 부리지 맙시다. Generator가 있습니다.
- 인덱스 기반 loop를 위해 range(len())을 사용하기보다 enumerate()를 사용합시다.
- import는 빌트인 - site-package - 사용자 정의 모듈 순으로 합시다.
- 함수의 기본 인수는 모듈 로드 시점의 함수 정의 과정에서 딱 한 번만 평가됩니다. 따라서 값이 동적인 키워드 인수에는 기본값으로 None을 사용하고, 함수의 docstring에 실제 기본 동작을 문서화합시다.
- 키워드 전용 인수를 사용하면 명료성을 강요할 수 있습니다.
- 리스트에서 원하는 값을 제거하려면 del list_[list_.index()]보다 list_.remove() 구문이 더 좋습니다.
- 데이터베이스 컨트롤에 SQLAlchemy를 사용하면 정말 편합니다.

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
