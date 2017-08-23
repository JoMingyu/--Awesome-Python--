from pyfcm import FCMNotification
# fcm 푸쉬 메시지는 data message를 전송할 수 있다

fcm = FCMNotification(api_key='')

data = {'key1': 123, 'key2': 1234}
fcm.notify_single_device(data_message=data)
