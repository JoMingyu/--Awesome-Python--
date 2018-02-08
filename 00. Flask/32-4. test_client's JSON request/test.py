import json
import unittest
from main import app


class Case(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def testPost(self):
        res = self.client.post('/', data=json.dumps({'test_key': 123}), content_type='application/json')
        # data라는 파라미터를 통해 직렬화된 JSON 데이터를 전달하고
        # 헤더의 Content-Type을 application/json으로 설정하면 JSON 데이터를 요청에 실어줄 수 있다(content_type 파라미터)

        self.assertEqual(123, int(res.data))

if __name__ == '__main__':
    unittest.main()
