from flask import Flask, request

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():
    # request.files를 이용해 multipart/form-data로 전달되는 파일에 접근할 수 있다
    f = request.files['file']

    f.save('uploads/uploaded_file.txt')
    # 디렉토리가 존재하지 않으면 오류가 발생한다

    # 업로드 당시 클라이언트에서의 파일명을 알고 싶다면, filename 속성에 접근할 수 있다
    print(f.filename)

    for f in request.files:
        # 요청으로 들어온 모든 파일에 접근
        pass

    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
