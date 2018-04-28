# https://github.com/esnme/ultrajson
# pip install ujson
import ujson
# 빌트인 json 모듈과 비슷하거나 상황에 따라 3~5배 이상 더 빠름

import time

data_for_test = [0] * 1000000


def test_json():
    import json

    before = time.time()
    json.dumps(data_for_test)
    after = time.time()

    print('JSON module : {}'.format(after - before))


def test_ujson():
    before = time.time()
    ujson.dumps(data_for_test)
    after = time.time()

    print('JSON module : {}'.format(after - before))

test_json()
test_ujson()
# length가 1,000,000인 list를 dump 시 2.5~3배 정도 차이
