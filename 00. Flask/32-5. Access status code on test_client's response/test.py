import unittest
from main import app


class Test(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def testSuccess(self):
        res = self.client.get('/?test_key=123')
        self.assertEqual(200, res.status_code)
        # status_code 프로퍼티를 이용해 status code를 얻어올 수 있다

    def testFail(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()
