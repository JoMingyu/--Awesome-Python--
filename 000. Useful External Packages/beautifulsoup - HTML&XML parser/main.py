# https://code.launchpad.net/beautifulsoup
# pip install bs4
from urllib.request import urlopen
import re
import ssl

from bs4 import BeautifulSoup
# HTML DOM이나 XML에 접근해 쉽게 내용을 긁어올 수 있는 파서

def get_redirected_url(url):
    # https 주소로 접속할 때 ssl context를 생성하기 위함
    context = ssl._create_unverified_context()
    return urlopen(url, context=context)

data = get_redirected_url('http://stu.dje.go.kr/sts_sci_md00_001.do?schulCode=G100000170&schulCrseScCode=4&schulKndScScore=04&schYm=201708')
# print(data.read().decode('utf-8'))
# 유니코드로 데이터가 오기 때문에 decode 과정이 필요

soup = BeautifulSoup(data, 'html.parser')
# BeautifuleSoup의 생성자로 response 객체와 파서 종류를 넘겨줌
print(soup.prettify())
# 말 그대로 HTML 코드를 '예쁘게' 만들어 준다

print(soup.title)
print(soup.find('title'))
# 엘리먼트 접근은 도트 연산 또는 find

print(soup.find_all('iframe'))
# 여러개의 엘리먼트가 있는 경우
# 리스트로 반환됨

print(soup.find(id='srchSchulBtn'))
print(soup.find(class_='box_type1 mb20'))
# id나 class로 접근

print(soup.select('.btn_type3 button'))
# select()나 select_one() 메소드를 이용해 CSS 셀렉터로 접근할 수 있다
# select()는 해당 셀렉터에 맞는 요소를 0개 이상 반환
# select_one()은 해당 셀렉터에 맞는 요소를 1개 이하 반환

print(soup.select_one('.btn_type3 button')['id'])
# 속성(attribute) 접근

print(soup.title.string)
print(soup.title.get_text())
# 태그 제거

monthly_meal = [td.get_text() for td in soup.find(class_='tbl_type3 tbl_calendar').find_all('td')]
# BeautifulSoup은 HTML의 DOM에 접근해서 파싱 가능. List Comprehension과 regex를 조합하면 파싱 코드가 굉장히 아름다워진다
# 각 날짜별 td의 text를 가지고 있는 리스트

for daily_meal in monthly_meal:
    if len(daily_meal) > 2 and daily_meal != '자료가 없습니다.':
        day = int(re.findall('\\d+', daily_meal)[0])
        menus = re.findall('[가-힇]+', daily_meal)
        print(menus)
