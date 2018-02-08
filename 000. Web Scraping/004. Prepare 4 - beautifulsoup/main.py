# 크롤링 준비 4번째 - beautifulsoup
# pip install bs4
from bs4 import BeautifulSoup as Soup
# DOM 구조를 기반으로 HTML 코드를 탐색
# 웹 프로그래밍에 대한 아주 기본적인 이해만 있다면 정말 편하게 쓸 수 있다
import requests

resp = requests.get('http://www.naver.com')
soup = Soup(resp.text, 'html.parser')
# HTML 본문과 파서 순

# bs 내부에서 제공하는 find 메소드로도 탐색 가능하고, DOM 기반으로 탐색하기 때문에 CSS 선택자 형태로 select도 가능함
# HTML에서 id는 하나의 엘리먼트에만, class는 여러 엘리먼트에 적용 가능하다는 점을 숙지하고 있으면 좋음

keywords = soup.find_all('a', {'class': 'ah_a'})
# 'ah_a' 클래스의 a 태그를 모두 find
# find_all()은 리스트를 반환, find()는 해당 엘리먼트를 반환
# 결과물이 없으면 각각 빈 리스트와 None 반환

for keyword in keywords:
    print(keyword.span)
    # 하위 엘리먼트 접근
    # keyword.find('span')과 같음

    print(keyword.span['class'])
    # 엘리먼트의 attribute 접근

    print(keyword.select_one('span.ah_r'))
    # CSS 선택자 형태 접근
    print(keyword.select_one('span.ah_k').get_text())
    # 접근 후 엘리먼트 내부 문자열 get

# soup과 regex를 결합시키면 아름다운 크롤러 코드 작성이 가능함
