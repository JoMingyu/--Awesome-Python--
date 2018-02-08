from flask import Flask, request

app = Flask(__name__)
# Flask를 사용하면 업로드된 파일들을 참 쉽게 다룰 수 있다


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save('uploads/uploaded_file.txt')
    # 디렉토리가 존재하지 않으면 오류가 발생한다

    # 업로드 당시 클라이언트에서의 파일명을 알고 싶다면, filename 속성에 접근할 수 있다
    print(f.filename)

    # Flask documentation에 따르면 이 값은 위조될 수 있다고 한다
    # 또한, 모든 종류의 파일을 올릴 수 있도록 하면 보안적으로 위험하다. XSS 문제를 야기할 수도 있기 때문이다
    # Form validator를 이용해 file extension을 검증하고, 파일 이름을 가져와야 한다면 werkzeug의 secure_filename 등을 사용하도록 하자

    return 'hello'

app.run(debug=True)
