# https://docs.python.org/3/library/urllib.parse.html
# URL을 특정 컴포넌트별로 나누기 위한 모듈
from urllib.parse import urlparse

url = 'https://www.github.com:80/JoMingyu?tab=repositories'
o = urlparse(url)

print(o)
# scheme, netloc, path, params, query, fragment로 이루어진 ParseResult 객체를 리턴
# 이 6개 정보 + username, password, hostname, port를 속성으로 가지고 있는 객체

print(o.scheme)
# URL scheme specifier : https

print(o.netloc)
# Network location part : www.github.com:80

print(o.path)
# Hierarchical path : /JoMingyu

print(o.params)
# Parameters for last path element : ''(empty string)

print(o.query)
# Query component : tab=repositories

print(o.fragment)
# Fragment identifier : ''(empty string)

print(o.username)
# None

print(o.password)
# None

print(o.hostname)
# www.github.com

print(o.port)
# 80

from urllib.parse import parse_qs

qs = parse_qs(o.query)
# 쿼리 부분에서 querystring만 검출
# {'key1': ['value1', 'value2'], 'key2': [ ... ], ...} 형태
print(qs)
# {'tab': ['repositories']}
print(qs['tab'][0])
# repositories
