# 기본적으로 파이썬의 타입 힌팅은 빌트인 타입을 가지고 사용한다
a: str
b: int

# 그러나 Iterable, Any처럼 빌트인 타입에 명시되지 않은 타입을 사용해야 하거나
# '문자열로 이루어진 리스트'같은 복잡한 타이핑을 사용하려면 typing 패키지의 도움을 받아야 한다
from typing import Any, List, Dict
from typing import Union, Optional
from typing import Callable

_: List[str] = ['a', 'b', 'c']
# 문자열로 이루어진 리스트
_: List[Union[str, int]] = ['a', 1, 2]
# 문자열이나 int로 이루어진 리스트
_: List[Optional[str]] = ['a', 'b', None]
# nullable한 문자열로 이루어진 리스트
_: Dict[str, float] = {
    'key_a': 123,
    'key_b': 80.12
}
# key가 str, value가 float으로 이루어진 딕셔너리

def merge_list_to_str(source: List[str], joined_with: str = ' ') -> str:
    return joined_with.join(source)

f: Callable[[List[str], str], str] = merge_list_to_str
# 순서대로 List[str]과 str 타입의 인자를 받아 str 타입을 리턴하는 callable
