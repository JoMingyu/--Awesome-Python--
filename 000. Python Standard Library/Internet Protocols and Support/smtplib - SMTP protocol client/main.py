# https://docs.python.org/3/library/smtplib.html
from smtplib import SMTP
# https://github.com/python/cpython/blob/3.6/Lib/smtplib.py
# smtplib 모듈은 SMTP나 ESMTP listener daemon에게 메일 전송이 가능한 SMTP 클라이언트 세션 객체이다
# RFC 821(Simple Mail Transfer Protocol), RFC 1869(SMTP Service Extensions) 기반으로 설계되어 있다
from email.mime.text import MIMEText

src_email = 'city7312@naver.com'
dst_email = 'city7310@naver.com'

smtp = SMTP('smtp.naver.com', 587)
# SMTP 클래스의 인스턴스

smtp.starttls()
# tls가 필요한 경우

smtp.login('city7312', 'password')
# 로그인

message = MIMEText('내용내용', _charset='utf-8')
message['subject'] = '제목'
message['from'] = src_email
message['to'] = dst_email
# MIMEText 클래스를 이용해 제목, 송신자, 수신자를 설정

smtp.sendmail(src_email, dst_email, message.as_string())
smtp.quit()

# 추가적으로, SMTP 인스턴스는 __enter__()와 __exit__()이 구현되어 있기 때문에 with-as 문을 사용하는 것도 좋다
