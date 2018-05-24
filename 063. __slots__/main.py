# Python의 모든 클래스는 인스턴스 속성을 가지고 있으며, 이러한 인스턴스 속성을 다루기 위해 기본적으로 Python은 딕셔너리를 사용하고 있다
# 이는 런타임에 임의의 새 속성을 설정할 수 있으므로(동적 attribute) 유용하나, 알려진(known) 속성을 가진 소규모 클래스의 경우
# 딕셔너리가 낭비하는 RAM 때문에 병목이 발생할 수 있다
# 이는 Python은 객체 생성 시 정적으로 메모리를 할당할 수 있다는 특징을 통해 해결 가능
# 인스턴스 속성에 딕셔너리를 사용하지 말 것을 알려주기 위해 __slots__를 사용하고, 속성의 고정된(fixed) set을 위해서만 메모리를 할당한다


class WithoutSlots:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class WithSlots:
    __slots__ = ['name', 'identifier']
    # 알려진(known) 속성
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


without_slots = WithoutSlots('PlanB', 1)
print(without_slots.__dict__)
# {'name': 'PlanB', 'identifier': 1}
without_slots.new_attr = 3
# 런타임에 새 속성을 설정(동적 attribute)할 수 있어 유용

with_slots = WithSlots('PlanB', 1)
print(with_slots.__slots__)
# ['name', 'identifier']
print(with_slots.__dict__)
# AttributeError: 'WithSlots' object has no attribute '__dict__'
# 이처럼 __slots__가 선언되어 있는 클래스는 속성들을 딕셔너리로 관리하지 않음


# WithoutSlots보다 WithSlots가 RAM을 약 4~50% 절약한다
# 아래의 ipython-memory-usage를 사용한 IronPython 코드를 통해 __slots__의 메모리 효율을 확인할 수 있다
"""
In [1]: class WithoutSlots:
   ...:     def __init__(self, name, identifier):
   ...:         self.name = name
   ...:         self.identifier = identifier
   ...:

In [2]: class WithSlots:
   ...:     __slots__ = ['name', 'identifier']
   ...:     def __init__(self, name, identifier):
   ...:         self.name = name
   ...:         self.identifier = identifier
   ...:

In [3]: import ipython_memory_usage.ipython_memory_usage as imu

In [4]: size = 1024 * 256

In [5]: imu.start_watching_memory()
In [5] used 0.0000 MiB RAM in 5.31s, peaked 0.00 MiB above current, total RAM usage 15.57 MiB

In [6]: x = [WithoutSlots(1, 1) for _ in range(size)]
In [6] used 22.6680 MiB RAM in 0.80s, peaked 0.00 MiB above current, total RAM usage 38.24 MiB

In [7]: x = [WithSlots(1, 1) for _ in range(size)]
In [7] used 9.3008 MiB RAM in 0.72s, peaked 0.00 MiB above current, total RAM usage 47.54 MiB
"""
