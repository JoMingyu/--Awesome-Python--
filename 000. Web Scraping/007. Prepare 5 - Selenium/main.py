# 크롤링 준비 5번째 - Selenium
# pip install selenium
from selenium import webdriver
# 페이지 렌더링 후 컴포넌트들을 ajax 등을 이용해 비동기적으로 불러오는 웹 페이지의 경우
# 단순 request로는 데이터에 접근 불가능. 로컬 또는 원격 컴퓨터의 브라우저를 구동할 수 있게 하는 '테스트 도구'인 selenium을 사용하여 해결
# Selenium은 웹 어플리케이션 테스트를 위한 프레임워크이고, Java, C#, Groovy, PHP, Python, Ruby 등을 지원하며 대부분의 브라우저, Linux, Windows, Mac OS를 지원
# + 오픈소스(Apache 2.0)

browser = webdriver.Chrome()
# Safari, Edge, Chrome 등 많은 브라우저를 사용할 수 있다
# webdriver가 작동하기 위해 매개변수에 해당 브라우저의 webdriver 경로를 넣거나, 환경 변수에 PATH를 넣어두어야 한다

browser.get('https://www.naver.com')

print(browser.page_source)
# page_source 속성을 통해 BeautifulSoup도 사용할 수 있고

browser.find_element_by_id()
browser.find_elements_by_class_name()
browser.find_element_by_class_name()
browser.find_elements_by_css_selector()
browser.find_element_by_css_selector()
# find element by id
# JS에서 버튼에 이벤트를 달아줄 때 getElementById, getElementsByClassName을 쓰는 것처럼 탐색 가능

print(browser.current_url)
print(browser.mobile)
print(browser.title)
# 브라우저가 현재 탐색하고 있는 페이지의 데이터

browser.back()
browser.forward()
# 뒤로가기/앞으로가기

found_element = browser.find_element_by_id()
# 엘리먼트 가져오기

print(found_element.tag_name)
print(found_element.id)
print(found_element.location)
print(found_element.is_displayed())
print(found_element.is_enabled())
print(found_element.is_selected())

found_element.click()
found_element.submit()
# 엘리먼트에 대해 여러가지 일들을 수행할 수 있음
