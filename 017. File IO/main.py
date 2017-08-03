# 이거 보고 파이썬에 영혼을 팔아버릴뻔 했다
# 파일 열때 빌트인 함수 open 쓰면 된다
f = open('temp.txt', 'r')
# 기본적으로 오픈 타입은 r(read)기 때문에 안 써줘도 된다
# 파일에서 문자열을 읽을 땐?
print(f.read())
# 기본 인코딩이 cp949라서(아마도 파이참 때문일거다 IntelliJ 인코딩이 cp949)
# 파일에 한글 포함 시 UnicodeDecodeError 뜬다

# 파일에 read, readline, readlines 메소드가 있는데 3개의 차이는 아래와 같다
# read : 이스케이프 시퀀스가 포함된 쌩 문자열로 모두 읽음
# readline : 라인 하나 읽음
# readlines : 모든 라인을 읽되 리스트로 반환(이스케이프 시퀀스가 포함됨)
# 리스트는 iteration 가능. 아래처럼 응용 가능
f = open('temp.txt')
for line in f.readlines():
    if '\\n' in line:
        print(line[0:-1])
    else:
        print(line)
    # 이스케이프 시퀀스 자르기

# 파일을 w 타입으로 열면 거기에 write 가능함
f = open('temp.txt', 'w')
f.write('hello')
f.close()
# close는 꼭 해주자

# 근데 보니까 다 삭제되고 write된다. 이걸 해결하려면 a(add) 타입으로 열자
f = open('temp.txt', 'a')
f.write('helloyallo')
f.close()

# 바이너리 파일을 열려면 타입 뒤에 b만 붙여주면 된다(wb, rb, ab)
