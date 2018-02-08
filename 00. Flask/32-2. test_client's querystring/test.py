import unittest
from main import app


class Case(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def testPost(self):
        res = self.client.get('/', query_string={'test_key': 123})
        # query_string이라는 파라미터를 통해 딕셔너리 타입을 전달하면 querystring을 전달할 수 있다

        self.assertEqual(123, int(res.data))

if __name__ == '__main__':
    unittest.main()
