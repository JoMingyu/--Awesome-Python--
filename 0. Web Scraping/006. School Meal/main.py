# 크롤링 연습 2번째 - 학교 급식 파싱
import re

from requests import get
from bs4 import BeautifulSoup as Soup

_URL = 'http://stu.dje.go.kr/sts_sci_md00_001.do'
params = {
    'schulCode': 'G100000170',
    # 학교 코드
    'schulCrseScCode': '4',
    'schulKndScScore': '04',
    # 학교 타입(유치원 1, 초등학교 2, 중학교 3, 고등학교 4)
    'schYm': '201711'
}

resp = get(_URL, params=params)
soup = Soup(resp.text, 'html.parser')

calendar = soup.select_one('table.tbl_type3.tbl_calendar')
day_menus = [re.findall('[가-힇]+\(\w+\)|[가-힇]+', menu.get_text()) for menu in calendar.find_all('td') if menu.get_text() != ' ']

for day_menu in day_menus:
    menu_dict = {}

    timing = [menu for menu in day_menu if re.match('[조중석]식', menu)]

    for idx, dine in enumerate(timing):
        if idx + 1 == len(timing):
            menu_dict[dine] = day_menu[day_menu.index(dine) + 1:]
        else:
            menu_dict[dine] = day_menu[day_menu.index(dine) + 1: day_menu.index(timing[idx + 1])]

    menu_dict['breakfast'] = menu_dict.pop('조식', None)
    menu_dict['lunch'] = menu_dict.pop('중식', None)
    menu_dict['dinner'] = menu_dict.pop('석식', None)
