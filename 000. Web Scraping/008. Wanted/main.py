# 원티드에 있는 회사들의 정보를 가져오도록 해보자
# 원티드는 React를 사용하기 때문에 Selenium이 필요하다
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import time


_URL_BASE = 'https://www.wanted.co.kr/company/{0}'
_PARSE_COUNT = 300


def parse():
    browser = webdriver.Chrome('C:/Users/dmdkz/Desktop/chromedriver')
    browser.implicitly_wait(10)

    for i in range(1, _PARSE_COUNT + 1):
        browser.get(_URL_BASE.format(i))
        time.sleep(3)
        # 네트워크 속도 문제로 full load 실패 시 발생될 잠재적 문제 방어
        soup = Soup(browser.page_source, 'html.parser')

        title = soup.select_one('div.company-header.text-center').h1.get_text()
        logo_url = soup.select_one('img.logo')['src']
        info = soup.select_one('div.company-info-content').get_text()
        hiring_positions = [position.h1.get_text() for position in soup.select('div.summary.col-xs-10')]
        etc_info = [etc.get_text() for etc in soup.select('div.company-info-etc.row')]


if __name__ == '__main__':
    parse()
