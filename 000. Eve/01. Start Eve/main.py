# pip install eve
from eve import Eve

app = Eve()
# config나 debug 속성에 접근하면 알 수 있겠지만, 아주 철저히 Flask 기반으로 설계되어 있다

if __name__ == '__main__':
    # app이 run하기 위해서는 settings.py에 DOMAIN이라는 이름의 딕셔너리가 선언되어 있어야 한다
    # DOMAIN = {'user': {}}로 선언해 두었는데, 'user'를 위한 자원이 있음을 뜻한다
    app.run(debug=True)
    # Flask와 동일하게 localhost:5000으로 run
    # localhost:5000/에 요청해 보면 아래의 응답을 볼 수 있다
    '''
    {
        "_links": {
            "child": [
                {
                    "href": "user",
                    "title": "user"
                }
            ]
        }
    }
    '''
    # 특정 API 리소스를 호출하지 않았으므로 사용 가능한 모든 리소스가 표시됨
    # localhost:5000/user에 요청을 해보면 이에 대한 응답을 볼 수 있다
    '''
    {
        "_items": [],
        "_links": {
            "parent": {
                "title": "home",
                "href": "/"
            },
            "self": {
                "title": "user",
                "href": "user"
            }
        },
        "_meta": {
            "page": 1,
            "max_results": 25,
            "total": 0
        }
    }
    '''
