# https://docs.python.org/3/library/os.path.html
from os import path
# https://github.com/python/cpython/blob/3.6/Lib/posixpath.py (운영체제 별로 따로 만들어져 있다 : posixpath, ntpath, macpath)
# os.path는 디렉토리 경로에 대한 유용한 함수들을 제공하고 있으며, 파일과 디렉토리를 다룰 때 os 모듈과 함께 매우 자주 사용된다

print(path.abspath('.'))
# /Users/planb/Documents/GitHub/개인 프로젝트/--Awesome-Python--/000. Python Standard Library/Generic Operation System/os.path - Common Pathname Manipulations
print(path.abspath('../../..'))
# /Users/planb/Documents/GitHub/개인 프로젝트/--Awesome-Python--
# os.path.abspath(path)
# 현재 경로를 기준점으로 해, path에 대한 절대 경로를 반환

import os

print(path.dirname(os.getcwd()))
# /Users/planb/Documents/GitHub/개인 프로젝트/--Awesome-Python--/000. Python Standard Library/Generic Operation System
# os.path.dirname(path)
# path에 대한 directory name(상위 path에 대한 abspath)을 반환

print(path.basename(os.getcwd()))
# os.path - Common Pathname Manipulations
# os.path.basename(path)
# path에 대한 base name(최하위 path 이름)을 반환

print(path.commonpath(['/Users/planb/Documents/abc', '/Users/planb/Desktop/abc', '/Users/planb/Downloads/abc']))
# /Users/planb
# os.path.commonpath(paths)
# sequence로 전달된 path들에 대해 공통으로 들어 있는 가장 긴 sub-path를 반환
# 위의 경우 공통되는 부분이 /Users/planb, /abc로 두 개가 있지만 가장 긴 sub-path가 /Users/planb이므로 위의 결과가 나옴

print(path.commonprefix(['/Users/planb/Documents/abc', '/Users/planb/Desktop/abc', '/Users/planb/Downloads/abc']))
# /Users/planb/D
# os.path.commonprefix(paths)
# 공통으로 들어 있는 prefix string을 반환
# 단순히 문자열을 비교하므로, 예상과 다르게 동작할 가능성이 있음

print(path.join(os.getcwd(), 'main.py'))
# /Users/planb/Documents/GitHub/개인 프로젝트/--Awesome-Python--/000. Python Standard Library/Generic Operation System/os.path - Common Pathname Manipulations/main.py
# os.path.join(path, *paths)
# path에 paths를 합친 결과를 반환

print(path.isfile(path.join(os.getcwd(), 'main.py')))
# True
# os.path.isfile(path)
# path가 파일 형태로 존재하는 경우 True를 반환

print(path.isdir(os.getcwd())))
# True
# os.path.isdir(path)
# path가 디렉토리 형태로 존재하는 경우 True를 반환