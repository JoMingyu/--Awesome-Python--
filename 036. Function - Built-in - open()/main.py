# 빌트인 함수 open을 이용해 파일을 읽고 쓸 수 있다
f = open('temp.txt', 'r')
# 전달된 파일 이름과 open mode에 따라 파일을 열어 file 객체를 반환
# 파일을 여는 mode는 r(read), w(write), a(append)가 있으며, text 파일을 위한 t, binary 파일을 위한 b 옵션이 있어 이들을 혼합해 사용
# open 함수의 기본 open mode는 rt(read + text)
# 파일을 열지 못하는 상황인 경우, OSError가 raise됨

print(f.read())
# Escape sequence가 포함된 하나의 문자열로 모두 읽음

print(f.readline())
# \n으로 구분되는 행 하나를 읽음

print(f.readlines())
# 전체 line을 읽되 이들은 list로 반환

f.close()
# 파일 객체를 안전히 닫기

# 파일을 w 타입으로 열면 값 insert 가능
f = open('temp.txt', 'w')
f.write('hello')
f.close()

# write는 내용을 모두 지우고 시작. a(append) 타입으로 열면 파일에 데이터를 추가할 수 있다
f = open('temp.txt', 'a')
f.write('helloyallo')
f.close()