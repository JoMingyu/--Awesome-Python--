import re
from requests import get
from bs4 import BeautifulSoup as Soup

_URL = 'http://coinmarketcal.com/?page={0}'


def load_all():
    cal_items = []
    page = 1
    while True:
        resp = get(_URL.format(page))
        if resp.status_code == 404:
            break

        soup = Soup(resp.text, 'html.parser')
        items = soup.select('div.row.multi-columns-row article div.content-box-general')

        for item in items:
            reminder = item.select_one('.reminder')
            cal_item = {
                'date': reminder['data-date'],
                'coin': reminder['data-coin'],
                'title': reminder['data-title'],
                'description': item.select_one('p.description').get_text(),
                'real': int(re.findall('\d+', item.select_one('div span').get_text())[0]),
                'progress': int(item.select_one('div.progress-bar.pb-dark')['aria-valuenow'])
            }

            cal_item['fake'] = int(round(cal_item['real'] * 100 / cal_item['progress'] - cal_item['real']))

            cal_items.append(cal_item)

        page += 1

    return cal_items


print(load_all())
