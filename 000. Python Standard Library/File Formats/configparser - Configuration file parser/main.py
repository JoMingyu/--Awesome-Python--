# https://docs.python.org/3/library/configparser.html
import configparser
# https://github.com/python/cpython/tree/3.6/Lib/configparser.py
# Java의 Properties처럼, config 파일을 읽고 쓰기 위한 라이브러리
# 백엔드 어플리케이션의 설정을 관리한다고 가정하고, config를 read/write하도록 해보자

config = configparser.ConfigParser()

config['MongoDB'] = {
    'host': 'localhost',
    'port': 27017,
    'db': 'Awesome'
}

config['RUN-SETTING'] = {
    'port': 5000,
    'debug': True
}

with open('config.conf', 'w') as file:
    config.write(file)

config.read('config.conf')

print(config['MongoDB'])
# <Section: MongoDB>

for k, v in config['MongoDB'].items():
    print(k, v)
    # key, value는 무조건 str

print(config['RUN-SETTING']['debug'])
# 'True'

print(config['RUN-SETTING'].getboolean('debug'))
# True