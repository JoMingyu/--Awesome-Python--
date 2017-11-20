# 크롤링 연습 1번째 - 네이버 실시간 검색어 파싱
from requests import get
from bs4 import BeautifulSoup as Soup

resp = get('https://www.naver.com')
soup = Soup(resp.text, 'html.parser')

ul = soup.select_one('ul.ah_l')
# 실시간 검색어 리스트

# 네이버 메인의 HTML 코드에는 ah_l 클래스에 ul이 3개 있음
# 1번째 ul은 모든 실시간 검색어(1~20)를 다루고 있고
# 2번째 ul은 1~10위, 3번째 ul은 11~20위를 다룸
# 실시간 검색어들만 필요하므로 첫번째 ul을 가져오는 게 좋음

items = ul.select('a.ah_a')
# ul 하위에 복수 개의 li로 아이템들이 있는데, 실제로 랭킹과 키워드가 있는 부분은 span 두개가 감싸진 a 태그이므로
# 아래는 ul 하위에 있는 li 리스트의 예
'''
<li class="ah_item">
    <a href="#" class="ah_a" data-clk="lve.keyword">
        <span class="ah_r">1</span>
        <span class="ah_k">독도새우</span>
    </a>
</li>
<li class="ah_item">
    <a href="#" class="ah_a" data-clk="lve.keyword">
        <span class="ah_r">2</span>
        <span class="ah_k">트럼프 국회연설</span>
    </a>
</li>
'''

for item in items:
    print('Rank : {0}'.format(item.select_one('span.ah_r').get_text()))
    print('Keyword : {0}'.format(item.select_one('span.ah_k').get_text()), end='\n\n')
