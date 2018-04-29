# https://github.com/Julian/jsonschema
# pip install jsonschema
from jsonschema import validate
# JSON Schema(http://json-schema.org/)의 Python용 구현체이며 Python 2.7+과 Python 3를 지원한다
# Python에 내장된 JSON 표현인 list와 dictionary의 스키마 검증을 돕는 라이브러리

schema = {
    'type': 'object',
    'properties': {
        'price': {'type': 'number'},
        'name': {'type': 'string'}
    }
}

data = {
    'name': 'egg',
    'price': 300
}

validate(data, schema)

data = {
    'name': 'egg',
    'price': 'something'
}

validate(data, schema)
# jsonschema.exceptions.ValidationError: 'something' is not of type 'number'

# CLI로도 지원하며, 아래처럼 사용할 수 있다
# > jsonschema -i something.json something.schema