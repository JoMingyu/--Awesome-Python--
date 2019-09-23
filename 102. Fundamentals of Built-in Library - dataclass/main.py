# PEP 557에 의해 Python 3.7에 만들어진 표준 패키지
# https://www.python.org/dev/peps/pep-0557/

from dataclasses import dataclass, field
from dataclasses import asdict, astuple
from typing import List


# dataclass 데코레이터는 클래스를 검사해 attribute들을 찾음
# 이 attribute들은 type hinting된 클래스 변수들임
# (kotlin같은)여타 언어들이 제공하는 data class처럼, __init__, __repr__같이 재정의하기 따분한 것들을 알아서 재정의해줌
# dacite같은 라이브러리의 도움을 받으면, API 단에서도 VO나 DTO 역할로 사용하기 매우 편하고 좋음!
@dataclass
class Item:
    name: str
    weight: float

item_1 = Item(name='potion', weight=0.1)
item_2 = Item(name='sword', weight=15)

print(item_1) # Item(name='potion', weight=0.1)
# __repr__이 자동 오버라이딩되어 간편함

# @dataclass나 @dataclass()나 똑같음
@dataclass()
class BundledItem:
    item: Item
    quantity: int
    total_weight: float = field(init=False)
    # 필드에 type hinting과 기본값 설정만으로 어려운 작업들을 field 함수를 통해 해결할 수 있다
    # init이 False로 전달되면, 자동 생성된 __init__ 메소드의 매개변수에 포함되지 않음

    def __post_init__(self):
        self.total_weight = self.item.weight * self.quantity

bundled_item_1 = BundledItem(
    item=item_1,
    quantity=15
)
print(bundled_item_1.total_weight) # 1.5
# weight가 0.1인 아이템과 함께, quantity 15를 넘겼으므로 __post_init__에 의해 total_weight가 1.5로 초기화되었음

bundled_item_2 = BundledItem(
    item=item_2,
    quantity=1
)

print(bundled_item_1) # BundledItem(item=Item(name='potion', weight=0.1), quantity=15, total_weight=1.5)
print(asdict(bundled_item_1)) # {'item': {'name': 'potion', 'weight': 0.1}, 'quantity': 15, 'total_weight': 1.5}
print(astuple(bundled_item_1)) # (('potion', 0.1), 15, 1.5)
# dataclass가 다중으로 엮이는 경우에도 잘 convert됨


@dataclass
class Inventory:
    items: List[BundledItem] = field(default_factory=list)


inventory = Inventory(items=[bundled_item_1])
inventory.items.append(bundled_item_2)

# 단, dataclass property에 명시한 타입들은 단순히 hinting임에 주의해야 함
Item(name=123, weight='PlanB')
# dataclass를 위한 대표적인 헬퍼인 dacite, pydantic.dataclass, dataclass-json 라이브러리를 써보고
# 뜯어보며 원리를 알아보면 dataclass를 이해하기 더 좋을 것 같다
