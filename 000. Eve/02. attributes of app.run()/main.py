from eve import Eve

app = Eve()

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
    # host, port, debug 속성을 정의해줄 수 있다. 아직 Flask와 다를 건 없다
