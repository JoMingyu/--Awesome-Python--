# settings.py에 user 리소스에 대한 스키마를 정의해 두었다
# key field들을 정의했다고도 볼 수 있는데, PostMan Client에서 이 key field들을 가지고 POST 요청을 시도해 보면 405를 반환한다
# Eve는 기본적으로 GET 요청만 허용하기 때문에, settings.py에서 리소스의 메소드를 정의해 주어야 한다
from eve import Eve

app = Eve()

if __name__ == '__main__':
    app.run(debug=True)

# 아무튼 그렇게 요청을 열심히 하고 나면, 응답이 이렇게 온다
# 참고로 MongoDB 서버가 켜져 있어야 한다
'''
{
    "_updated": "Mon, 16 Oct 2017 13:18:35 GMT",
    "_created": "Mon, 16 Oct 2017 13:18:35 GMT",
    "_etag": "05ca2afbf3ecd0897d910eff81cf08c2bf1c95f5",
    "_id": "59e4b1ab6751803bb85a7c24",
    "_links": {
        "self": {
            "title": "User",
            "href": "user/59e4b1ab6751803bb85a7c24"
        }
    },
    "_status": "OK"
}
'''
# Eve가 POST /user에 대한 라우팅을 settings.py를 기반으로 진행한 것이다
# 이 데이터가 담기는 곳은 로컬의 MongoDB 서버

# 다시 /user에 GET요청을 하면 유저 데이터가 실제로 들어간 걸 볼 수 있다
'''
{
    "_items": [
        {
            "_id": "59e4b1ab6751803bb85a7c24",
            "id": "qwe",
            "pw": "123",
            "name": "조민규",
            "_updated": "Mon, 16 Oct 2017 13:18:35 GMT",
            "_created": "Mon, 16 Oct 2017 13:18:35 GMT",
            "_etag": "05ca2afbf3ecd0897d910eff81cf08c2bf1c95f5",
            "_links": {
                "self": {
                    "title": "User",
                    "href": "user/59e4b1ab6751803bb85a7c24"
                }
            }
        }
    ],
    "_links": {
        ...
    },
    "_meta": {
        ...
    }
}
'''
