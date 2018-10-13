d = {'nickname': 'PlanB', 'region': 'Seoul'}

d['new'] = 'hi'
# 새로운 mapping 정의

d.setdefault('new', 'hello')
# .setdefault(key, value)
# 해당 딕셔너리에 key가 존재한다면 그대로 두고, 없다면 새로 생성

del d['new']
# del d[key]
# key에 해당하는 mapping 제거

print(d.pop('region')) # 'Seoul'
# .pop(key)
# key에 해당하는 mapping을 제거하며 반환

print(d.get('region')) # None
# .get(key, d=None)
# key에 해당하는 value를 반환하거나, key가 존재하지 않으면 d를 반환. d의 기본값은 None
# 존재하지 않는 key를 가져오는 경우 에러가 발생하기 때문에, 값을 안전하게 가져오기 위해 사용됨

print(d.keys()) # dict_keys(['nickname'])
print(d.values()) # dict_values(['PlanB'])
print(d.items()) # dict_items([('nickname', 'PlanB')])
# .keys()
# .values()
# .items()
# key list, value list, item list를 각각에 해당하는 새로운 sequence 객체로 반환
