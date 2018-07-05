# https://github.com/jiaaro/pydub
# pip install pydub
from pydub import AudioSegment
# http://pydub.com/
# 연산자 오버로딩이 잘 적용되어 있어, 매우 Pythonic한 인터페이스를 가진 오디오 처리 라이브러리
# 프로그래밍 언어에서 연산자 오버로딩이 왜 강력한 개념으로 꼽히는지를 알 수 있음

song = AudioSegment.from_wav('brobob.mp3')
# AudioSegment.from_***(cls, file, parameters=None)
# classmethod로, 내부적으로는 AudioSegment.from_file을 호출한다

song = AudioSegment.from_file('brobob.mp3', 'mp3')
# AudioSegment.from_file(cls, file, format=None, codec=None, parameters=None, **kwargs)

first_10_seconds = song[:10000]
last_5_secnds = song[-5000:]
# 첫 10초, 마지막 5초를 잘라 새로운 AudioSegment 객체 생성

beginning = first_10_seconds + 6
# 6dB 증가

end = last_5_secnds - 3
# 3dB 감소

without_the_middle = beginning + end
# AudioSegment 합치기

backwards = song.reverse()
# 뒤집기

beginning_repeat_3_times = beginning * 3
# repeat

faded = song.fade_in(2000).fade_out(3000)
# fade in과 fade out

faded.export('mashup.wav', format='wav')
# 다른 확장자로 export