# Eve
Flask 기반의 API 서버 전용 프레임워크
~~~
pip install eve
~~~

## 개요
(당연히) 오픈소스로 이루어져 있으며 철저히 Flask 기반으로 설계되어 있는 Python을 위한 REST API 프레임워크. Flask와 Cerberus에 의해 구동되며 MongoDB에 대한 기본 지원을 제공하고 있음.(eve의 dependency에 cerberus, simplejson, wekzeug, markupsafe, flask, flask-pymongo가 포함됨) SQL, ElasticSearch나 Neo4j 등의 백엔드 지원은 extension들을 통해 제공됨. Flask와 다를 거 없이 극도의 간결함을 가지고 있음.
~~~
from eve import Eve

app = Eve()
app.run()
~~~
settings.py를 정말 좋아하는 프레임워크.
