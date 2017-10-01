from flask_restful_swagger_2 import swagger, Resource, request
from flask_jwt import jwt_required, current_identity

from pymongo.collection import ObjectId

from database.models.post import Post as PostCol
from database.models.user import User


class Post(Resource):
    @jwt_required()
    @swagger.doc({
        'tags': ['게시글'],
        'description': '게시글 업로드',

        'parameters': [
            {
                'name': 'title',
                'description': '게시글 제목',
                'in': 'formData',
                'type': 'String'
            },
            {
                'name': 'content',
                'description': '게시글 내용',
                'in': 'formData',
                'type': 'String'
            }
        ],

        'responses': {
            '201': {
                'description': '게시글 업로드 성공'
            },
            '401': {
                'description': 'JWT UNAUTHORIZED'
            }
        }
    })
    def post(self):
        id = str(current_identity)
        title = request.form.get('title')
        content = request.form.get('content')

        PostCol(title=title, content=content, author=User(id, User.objects(id=id).first().pw)).save()

        return '', 201

    @swagger.doc({
        'tags': ['게시글'],
        'description': '게시글 목록 조회',

        'responses': {
            '200': {
                'description': '게시글 조회 성공(데이터 있음)',
                'examples': {
                    'application/json': [
                        {
                            "_id": "59ca4a726751801b80c89e2b",
                            "author": "123",
                            "title": "제목이야",
                            "content": "내용이다",
                            "post_date": "2017-09-26"
                        },
                        {
                            "_id": "59ca4a7c6751801b80c89e2c",
                            "author": "123",
                            "title": "제목이야!",
                            "content": "내용이다!",
                            "post_date": "2017-09-26"
                        }
                    ]
                }
            },
            '204': {
                'description': '반환할 게시글 없음'
            }
        }
    })
    def get(self):
        posts = list(PostCol.objects().as_pymongo())
        for idx in range(len(posts)):
            posts[idx]['_id'] = str(posts[idx]['_id'])

        return posts

    @jwt_required()
    @swagger.doc({
        'tags': ['게시글'],
        'description': '게시글 수정',

        'parameters': [
            {
                'name': '_id',
                'description': '수정할 게시글의 id',
                'in': 'formData',
                'type': 'String'
            },
            {
                'name': 'title',
                'description': '게시글 제목',
                'in': 'formData',
                'type': 'String'
            },
            {
                'name': 'content',
                'description': '게시글 내용',
                'in': 'formData',
                'type': 'String'
            }
        ],

        'responses': {
            '200': {
                'description': '게시글 수정 성공'
            },
            '204': {
                'description': '수정 권한 없음'
            },
            '401': {
                'description': 'JWT UNAUTHORIZED'
            }
        }
    })
    def patch(self):
        id = str(current_identity)
        _id = request.form.get('_id')
        title = request.form.get('title')
        content = request.form.get('content')

        data = PostCol.objects(id=_id).first()
        if not data or data.author.id != id:
            return '', 204

        data.update(title=title, content=content)

        return '', 200

    @jwt_required()
    @swagger.doc({
        'tags': ['게시글'],
        'description': '게시글 삭제',

        'parameters': [
            {
                'name': '_id',
                'description': '삭제할 게시글의 id',
                'in': 'formData',
                'type': 'String'
            }
        ],

        'responses': {
            '200': {
                'description': '게시글 삭제 성공'
            },
            '204': {
                'description': '삭제 권한 없음'
            },
            '401': {
                'description': 'JWT UNAUTHORIZED'
            }
        }
    })
    def delete(self):
        id = str(current_identity)
        _id = request.form.get('_id')

        data = PostCol.objects(id=_id).first()
        if not data or data.author.id != id:
            return '', 204

        data.delete()

        return '', 200
