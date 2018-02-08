# onoffmix의 모임 정보
# onoffmix는 '비 브라우저'의 트래픽을 좋아하지 않으므로 User-Agent 헤더를 이용해 이러한 트래픽을 차단하려고 함
# requests의 기본 User-Agent는 python-requests / x.x.x 이기 때문에 Session을 이용해 브라우저인 척 속이거나 Selenium을 사용할 수 있음
# 이번에는 bs를 사용하지 않고 selenium으로 모두 처리해 보도록 하자
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

_URL = 'http://onoffmix.com/event'


def load_items():
    wd = webdriver.Chrome('C:/Users/dmdkz/Desktop/chromedriver')
    wd.implicitly_wait(10)
    wd.get(_URL)

    last_event_len = 0
    items = []
    while True:
        wd.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        # 스크롤을 내려 더 많은 정보를 load
        time.sleep(5)
        # load에 걸릴 시간을 확보하기 위해
        events = wd.find_elements_by_class_name('todayEvent')
        # Onoffmix는 스크롤이 내려가며 모임 정보들이 div에 ul.todayEvent로 추가되는 방식

        if len(events) == last_event_len:
            # 스크롤 이후 event length와 마지막 event length가 같다면(더 로드되지 않았다면)
            # items = events
            # break
            pass
            # 그러나 위의 if문으로 이어가면 수천개 이벤트까지 스크롤이 내려갈 것 같으므로 제거

        # last_event_len = len(events)
        # 더 로드되었다면 마지막 event length 갱신

        if len(events) > 20:
            items = events
            break

    return items

elements = load_items()
for el in elements:
    try:
        event_thumbnail = el.find_element_by_css_selector('li.eventThumbnail a')
        link = event_thumbnail.get_attribute('href')
        image = event_thumbnail.find_element_by_css_selector('img').get_attribute('src')
        title = el.find_element_by_css_selector('li.eventTitle a').get_attribute('title')
        pin_count = el.find_element_by_css_selector('span.pinNumber').text
        personnel_count = el.find_element_by_css_selector('li.eventPersonnel span').text

        print(link, image, title, pin_count, personnel_count)
    except NoSuchElementException:
        break
