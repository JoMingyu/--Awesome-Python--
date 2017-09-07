from smtplib import SMTP
from email.mime.text import MIMEText
# SMTP를 통한 메일 전송을 하기 위해 SMTP와 MIMEText 클래스가 필요함

src_email = 'city7312@naver.com'


def send_email(dst_email, title, content):
    message = MIMEText(content, _charset='utf-8')
    message['subject'] = title
    message['from'] = src_email
    message['to'] = dst_email
    # MIMEText 클래스를 이용해 제목, 송신자, 수신자를 설정

    smtp = SMTP('smtp.naver.com', 587)
    # SMTP 클래스의 인스턴스

    smtp.starttls()
    # tls가 필요한 경우

    smtp.login('city7312', 'password')
    # 로그인

    smtp.sendmail(src_email, dst_email, message.as_string())
    smtp.quit()

send_email('city7310@naver.com', '아아', '아아아')
