import unittest
from main import app


class Case(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def testPost(self):
        res = self.client.post('/', data={'test_key': 123})
        # data라는 파라미터를 통해 딕셔너리 타입을 전달하면 body 데이터를 보내줄 수 있다
        # 헤더의 Content-Type 기본값이 application/x-www-form-urlencoded이므로 이대로 보내면 잘 전달된다
        # form-data를 전달하려면 헤더의 Content-Type을 application/form-data로 설정하자

        self.assertEqual(123, int(res.data))

if __name__ == '__main__':
    unittest.main()
