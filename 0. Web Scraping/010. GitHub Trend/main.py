import re

from bs4 import BeautifulSoup as Soup
from requests import get


URL = 'https://github.com/trending'

resp = get(URL)
soup = Soup(resp.text, 'html.parser')

repo_list = soup.select('li.col-12.d-block.width-full.py-4.border-bottom')
for repo in repo_list:
    owner, name = repo.select('div h3 a')[0].get_text().split('/')
    owner = owner.strip()
    name = name.strip()
    description = repo.select('p.col-9.d-inline-block.text-gray.m-0.pr-4')[0].get_text().strip()
    language_el = repo.find('span', {'itemprop': 'programmingLanguage'})
    language = language_el.get_text().strip() if language_el else None
    indicator = repo.select('a.muted-link.d-inline-block.mr-3')
    star_count = int(indicator[0].get_text().strip().replace(',', ''))
    fork_count = int(indicator[1].get_text().strip().replace(',', ''))
    today_star = re.findall('\d+', repo.select('span.d-inline-block.float-sm-right')[0].get_text())[0]
