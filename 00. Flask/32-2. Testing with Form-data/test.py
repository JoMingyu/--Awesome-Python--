import unittest
from main import app


class Case(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def testPost(self):
        rv = self.client.post('/', data={'test_key': 123})
        # post 메소드에 data라는 파라미터를 통해 body-data를 보내줄 수 있다

        self.assertEqual(123, int(rv.data))

if __name__ == '__main__':
    unittest.main()
