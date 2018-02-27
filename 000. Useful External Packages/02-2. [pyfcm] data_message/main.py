from pyfcm import FCMNotification
# fcm 푸쉬 메시지는 data message를 전송할 수 있다. 일반적으로 JSON이며 pyfcm 측에서는 data_message 인자로 딕셔너리를 전달하면 알아서 직렬화 처리해준다

fcm = FCMNotification(api_key='')

data = {'key1': 123, 'key2': 1234}
fcm.notify_single_device(registration_id='', data_message=data)
# notify_*** 메소드에도 data_message 파라미터가 있지만, pyfcm 측에서 data messaging을 위한 메소드를 만들어 두었다

fcm.single_device_data_message(registration_id='', data_message=data)
fcm.multiple_devices_data_message(registration_ids=['', '', ''], data_message=data)
