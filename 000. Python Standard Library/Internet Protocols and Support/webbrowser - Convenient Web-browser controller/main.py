# https://docs.python.org/3/library/webbrowser.html
import webbrowser
# https://github.com/python/cpython/blob/3.6/Lib/webbrowser.py
# 웹브라우저를 컨트롤하기 위한 모듈

webbrowser.open_new('https://github.com/JoMingyu/Awesome-Python')
# 기본 브라우저를 통해 url을 새로운 창에 띄워 줌. 불가능하다면 브라우저 창에서 URL을 염

webbrowser.open_new_tab('https://github.com/JoMingyu/Awesome-Python')
# 기본 브라우저의 새 페이지(탭)에서 URL을 open. 가능하다면 open_new와 동일함
