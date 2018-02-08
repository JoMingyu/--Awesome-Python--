import unittest
import main


class Case(unittest.TestCase):
    # unittest의 TestCase 클래스를 상속받고 setUp과 tearDown을 만들었다
    def setUp(self):
        print('Setup')
        self.client = main.app.test_client()
        # Flask 클래스의 인스턴스는 test_client를 통해 FlaskClient 객체를 얻을 수 있다

    def tearDown(self):
        print('Teardown')

    def testIndex(self):
        res = self.client.get('/')
        # FlaskClient.method를 이용해 쉽게 request할 수 있고

        self.assertEqual('hello', res.data.decode('utf-8'))
        # response body는 .data 프로퍼티에 접근하며, bytes 타입이기 때문에 문자열로 사용하려면 decode 필요
        # unittest.TestCase에서 지원하는 assertion을 이용해 검증


if __name__ == '__main__':
    unittest.main()
