# https://docs.python.org/3/library/unittest.html
# 파이썬은 단위 테스트(unit test)를 위해 unittest라는 모듈을 제공한다
import unittest
# 파이썬의 unittest는 객체지향적인 방식으로 테스트를 수행하며, 아래의 4가지 개념이 중요하다
# Test fixture : 하나 이상의 테스트를 수행하는 데 필요한 준비 작업 및 클린업 작업. 임시 프록시나 데이터베이스, 디렉토리 작성, 서버 프로세스 시작 등
# Test case : 테스트의 개별 단위. 특정 입력에 대한 반환 결과를 확인함. unittest는 테스트 케이스를 작성하는 데 사용할 수 있는 TestCase 클래스를 제공함
# Test suite : 테스트 케이스, 테스트 suite나 둘 모두의 모음. 함께 실행해야 하는 테스트를 집계하는 데 사용됨
# Test runner : 테스트 실행을 조정하고 사용자에게 결과를 제공하는 구성 요소. 러너는 그래픽 인터페이스 또는 텍스트 인터페이스, 특수 값을 반환하는 등으로 테스트 실행 결과를 나타냄


# 아래의 두 함수를 테스트해보도록 하자
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def error_add(a, b):
    return a + b + 1


# unittest 모듈의 TestCase 클래스를 상속받아 테스트 케이스를 만들 수 있다
class Test(unittest.TestCase):
    # setUp -> 테스트 유닛 -> tearDown 형태로 각 테스트가 돌아가며, 이 사이클에서 setUp과 tearDown이 test fixture로 분류된다
    # 테스트 유닛이 도는 순서는 사전 순서다
    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    # 아래엔 'test'로 시작되는 3개의 테스트들이 메소드 형태로 만들어져 있다
    # 이러한 네이밍 컨벤션은 어떤 메소드가 테스트인지를 test runner가 알 수 있도록 하기 위함이다
    def testAdd(self):
        print('Testing add')
        self.assertEqual(add(20, 10), 30)
        # TestCase에는 이처럼 assertion을 위한 여러가지 메소드들을 제공하며, assert 키워드를 사용하는 것보다 실행의 결과를 확인하기 더 좋다
        
        self.assertIn('test', ['t', 'e', 'test'])
        self.assertNotIn('test', ['t', 'e'])
        self.assertTrue('some')
        self.assertFalse(False)
        self.assertIsInstance(True, bool)
        # ...

    def testSubtract(self):
        print('Testing subtract')
        self.assertEqual(subtract(15, 5), 10)

    def testErrorAdd(self):
        print('Testing error_add')
        self.assertEqual(error_add(3, 4), 7)

if __name__ == '__main__':
    unittest.main()
    # Test runner 실행. 테스트를 돌리기 위한 가장 간단한 구문이며 테스트 스크립트의 결과를 CLI로 제공
