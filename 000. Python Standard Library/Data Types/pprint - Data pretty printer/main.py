# https://docs.python.org/3/library/pprint.html
# 파이썬 데이터를 예쁘게 출력하기 위한 모듈
import pprint

data = ('Some', 'thing', 'problems', ('lumberjack', 'knights', 'hi', 'ham', 'miss', 'wonderful'))
pp = pprint.PrettyPrinter(indent=4)
# PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False)
pp.pprint(data)
# (   'Some',
#     'thing',
#     'problems',
#     ('lumberjack', 'knights', 'hi', 'ham', 'miss', 'wonderful'))

data = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead'))))))
pp = pprint.PrettyPrinter(width=41)
pp.pprint(data)
# ('spam',
#  ('eggs',
#   ('lumberjack',
#    ('knights', ('ni', 'dead')))))

pp = pprint.PrettyPrinter(depth=3)
pp.pprint(data)
# ('spam', ('eggs', ('lumberjack', (...))))
