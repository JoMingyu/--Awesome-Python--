import unittest
from main import app


class Test(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def testSuccess(self):
        rv = self.client.get('/?test_key=123')
        self.assertTrue('200' in rv.status)
        # rv.status를 통해 status code를 얻어올 수 있는데
        # code와 message가 함께 온다 (204 NO CONTENT)

    def testFail(self):
        rv = self.client.get('/')
        self.assertTrue('204' in rv.status)


if __name__ == '__main__':
    unittest.main()
