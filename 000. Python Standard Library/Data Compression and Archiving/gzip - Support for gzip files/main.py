# https://docs.python.org/3/library/gzip.html
import gzip
# https://github.com/python/cpython/tree/3.6/Lib/gzip.py
# GNU의 gzip/gunzip과 유사한 형태의 간단한 gzip compress/decompress API를 제공한다
# ZIP과 같이, LZ77 알고리즘을 통해 데이터를 압축한 뒤, 중복되는 내용에 대한 위치와 길이를 허프만 부호화를 사용하여 한 번 더 압축하는
# Deflate 알고리즘을 따르며, 여러 파일을 하나의 파일로 압축하는 옵션이 없다는 점에서 차이가 난다

import json
import random

data_origin = json.dumps([{
    'idx': idx,
    'random_str': ''.join(random.choice('abc') for _ in range(100)),
    'random_int': random.randint(1, 10),
    'random_float': round(random.random(), 3)
} for idx in range(10000)])

print(len(data_origin))
# 1728785

zipped_data = gzip.compress(data_origin.encode(), compresslevel=1)
# 압축
# compresslevel은 압축의 수준을 관리하기 위한 0과 9 사이의 정수
# 1은 가장 빠르고 압축율이 낮으며, 9에 가까워질 수록 느려지고 압축율이 높아짐. 기본값은 9

print(len(zipped_data))
# 338991

unzipped_data = gzip.decompress(zipped_data)
# 압축 해제

print(len(unzipped_data))
# 1728785

# gzip의 defalte 알고리즘은 중복 내용을 압축하는 허프만 부호화 과정이 있기 때문에, 문자열에 규칙성이 있으면 더 압축율이 높다
print(len(gzip.compress(b'abcd' * 300)))
# 33

content = b'PlanB'

with gzip.open('file.txt.gz', 'wb') as f:
    # gzip 형태로 파일에 write
    f.write(content)

with gzip.open('file.txt.gz', 'rb') as f:
    # gzip 파일 read
    print(f.read())
