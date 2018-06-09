# https://docs.python.org/3/library/pkgutil.html
import pkgutil
# https://github.com/python/cpython/blob/3.6/Lib/pkgutil.py
# pkgutil을 활용해 프로젝트의 패키지와 모듈들을 동적으로 다룰 수 있다
import test


for loader, name, is_package in pkgutil.iter_modules(test.__path__):
    # FileFinder 객체, 모듈 이름, 패키지 여부 순
    print(loader, name, is_package)

    module_ = loader.find_module(name).load_module(name)
    # 모듈 동적 load
    print(module_)

# 재귀함수를 구성하고, 특정 패키지 하위의 모든 모듈들을 불러오는 식의 리플렉션을 구현할 수 있을 것이다
# https://github.com/JoMingyu/Reflections
