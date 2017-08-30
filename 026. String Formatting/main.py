# 포매팅 방식은 여러가지가 있다
format1 = 'My %s is %s!!'
print(format1 % ('Name', 'PlanB'))

# str 객체엔 format이라는 메소드가 있다
# 문자열로 포맷을 만들고, format 메소드의 인자로 값들을 넘겨주면 된다
format2 = "This is {0} formatting!"
print(format2.format('awesome'))
# 타입 안정성이 높고, 정렬이나 공백 채우기 등의 고급 포매팅이 가능해서 이걸 많이 쓴다
