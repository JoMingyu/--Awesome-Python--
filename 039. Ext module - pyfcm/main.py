from pyfcm import FCMNotification
# FCM 푸쉬 메시지를 전송하기 위한 모듈
# 이거 보고 놀랐다 와 이렇게 편할수가 있냐

fcm = FCMNotification(api_key='')
# FCM 서버 키를 통해 객체를 만들자

# 클라이언트 하나에 보내기, 여러 곳에 보내기, topic subscriber에 보내기가 대표적인 메소드다
fcm.notify_single_device(registration_id='', message_title='제목이야', message_body='배고프다')
# 매개변수 종류 진짜 엄청 많다

fcm.notify_multiple_devices(registration_ids=['', ''], message_title='제-목', message_body='배고파')
# 여러 클라이언트에 보내는 거
