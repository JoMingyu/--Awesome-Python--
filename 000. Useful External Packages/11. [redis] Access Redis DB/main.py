# pip install redis
import redis
# 고성능 k-v store 인메모리 NoSQL 데이터베이스인 Redis DB에 접근하기 위한 패키지
# NoSQL & Cache 솔루션이며 메모리 기반으로 구성, 명시적으로 삭제 또는 expire를 설정하지 않으면 데이터는 영구적으로 보존됨
# 데이터베이스, 또는 Cache로 사용될 수 있으며 성능은 초당 2만 ~ 10만회

# Redis 설치 : https://github.com/MicrosoftArchive/redis/releases
# NET STOP Redis 후 Redis 설치 경로에서 redis-server.exe를 통해 redis server를 열어 주자

r = redis.Redis()
# Redis 클래스는 StrictRedis 클래스를 상속받고 있는데, 이 클래스의 생성자는 기본적으로 host='localhost', port=6379
# 따라서 기본 설정으로 Redis Server가 동작하고 있다면 host와 port는 파라미터로 던져주지 않아도 된다

print(r.set('key', 125))
# name, value 순
# ex, px, nx, xx 파라미터를 넘겨줄 수 있음
# ex는 second 단위의 expire flag
# px는 millisecond 단위의 expire flag
# nx가 True이면 key가 존재하지 않을 때만 set
# xx가 True이면 key가 이미 존재할 때만 set

print(r.get('key'))
# get에서 반환되는 값은 무조건 bytes

print('Key exists :', r.exists('key'))
# key 존재 여부

print('Set expire :', r.expire('key', 3))
# 3초 후 만료되도록 설정
# 만료 설정 성공 시 True, key가 존재하지 않아 실패하면 False를 반환

import time
time.sleep(4)

print('Key exists :', r.exists('key'))
# sleep 후 key는 존재하지 않음

print('Key delete :', r.delete('key'))
# delete, 성공하면 1, key가 존재하지 않아 실패하면 0을 반환

pl = r.pipeline()
# 단일 요청으로 서버에 여러 명령을 버퍼링하도록 지원하는 Redis의 하위 클래스
# 클라이언트와 서버 간의 앞뒤 TCP 패킷 수를 줄임으로써 성능을 크게 향상시킴
pl.set('key2', 123)
pl.set('key3', 515)
pl.execute()
