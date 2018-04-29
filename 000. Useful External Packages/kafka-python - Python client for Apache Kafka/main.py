# https://github.com/dpkp/kafka-python
# pip install kafka-python
from kafka import KafkaConsumer, KafkaProducer
# Apache Kafka에 접근하여 메시지를 produce/consume할 수 있는,
# 공식 Java client와 매우 유사하게 디자인된 kafka client 라이브러리

# -- KafkaProducer
consumer = KafkaProducer()
# 기본적으로 localhost:9092를 broker로 판단하며, localhost:9092가 kafka broker의 주소가 아니라면
KafkaProducer(bootstrap_servers='https://some.kafka.broker.address:12345')
# 와 같은 형태로 bootstrap_servers 인자를 통해 전해주면 된다

# Kafka가 클러스터 환경에서 동작하고 있다면, 아래처럼 List나 Tuple과 같은 iterable 타입으로 넘겨준다
KAFKA_BROKERS = (
    'localhost:9092',
    'localhost:9093',
    'localhost:9094'
)

producer = kafkaProducer(bootstrap_servers=KAKFA_BROKERS)
producer.send('test', b'message!')
# .send()를 통해 메시지를 produce할 수 있으며, 인자는 각각 topic name, message 순

# 직렬화된 json 메시지를 produce한다면, send할 때마다 json.dumps()하지 않고
# KafkaProducer 생성자에 value serializer를 붙여주는 방식으로 구현할 수 있다
import json

producer = kafkaProducer(bootstrap_servers=KAKFA_BROKERS, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('test', {'key': 'value'})

# -- KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
# KafkaConsumer에는 bootstrap_servers에 대해 기본값이 정의되어 있지 않아 인자를 전달해 주어야 함
# Consumer는 1개 이상의 topic을 subscribe한 채로 메시지를 가져올 수 있엄
# KafkaConsumer 객체는 iterator를 상속받은 클래스기 때문에, 즉시 반복 가능
consumer.subscribe(['test'])
for msg in consumer:
    print(msg)
    # ConsumerRecord(topic='test', partition=0, offset=35, timestamp=1515992785585, timestamp_type=0, ...)

# 메시지의 첫 offset부터 불러오려면, KafkaConsumer 객체 생성 시 auto_offset_reset 인자의 값을 earliest로 주면 됨
consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)
