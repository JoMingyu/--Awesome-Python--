# 파이썬은 단위 테스트(unit test)를 위한 모듈을 제공한다
import unittest


# 아래의 두 함수를 테스트해보도록 하자
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def error_add(a, b):
    return a + b + 1


# unittest 모듈의 TestCase 클래스를 상속받으면 테스트 케이스를 만들 수 있다
class Test(unittest.TestCase):
    # setUp과 tearDown 메소드는 하나의 테스트 유닛이 돌 때마다 호출된다
    # setUp -> 테스트 유닛 -> tearDown
    # 테스트 유닛이 도는 순서는 (아마도) 사전 순서다
    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    def testAdd(self):
        print('Testing add')
        self.assertEqual(add(20, 10), 30)

    def testSubtract(self):
        print('Testing subtract')
        self.assertEqual(subtract(15, 5), 10)

    def testErrorAdd(self):
        print('Testing error_add')
        self.assertEqual(error_add(3, 4), 7)
        # 메소드명 앞에 'test'가 빠져 있으면 테스트 유닛으로 인식되지 않는다

if __name__ == '__main__':
    # 이 구문이 빠져 있으면 테스트 케이스가 제대로 작동하지 않는다
    unittest.main()
    # 만들어 둔 테스트 케이스를 실행하는 구문
