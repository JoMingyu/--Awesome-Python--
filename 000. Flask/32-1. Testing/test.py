import unittest
import main


class Case(unittest.TestCase):
    # unittest의 TestCase 클래스를 상속받고 setUp과 tearDown을 만들었다
    def setUp(self):
        print('Setup')
        self.app = main.app.test_client()
        # Flask 클래스의 인스턴스는 test_client를 통해 FlaskClient 객체를 얻을 수 있다

    def tearDown(self):
        print('Teardown')

    def testIndex(self):
        response = self.app.get('/')
        self.assertEqual('hello', response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
