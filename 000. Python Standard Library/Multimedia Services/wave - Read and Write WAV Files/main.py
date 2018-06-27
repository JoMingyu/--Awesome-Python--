# https://docs.python.org/3/library/wave.html
import wave
# https://github.com/python/cpython/blob/3.6/Lib/wave.py
# .wav 파일을 읽고 쓸 수 있는 라이브러리

w = wave.open('SineWaveMinus16.wav')
# wave.open(file, mode=None)
# 'rb'와 'wb'를 mode로 사용할 수 있다. 각각 read only, write only 모드를 의미한다

print(w.getframerate())
# 44100
# Frame rate(샘플링 주파수)

print(w.getnframes())
# 2646000
# 전체 프레임 수

print(w.getnchannels())
# 2
# 채널 수(1은 mono, 2는 stereo)

print(w.getparams())
# _wave_params(nchannels=2, sampwidth=4, framerate=44100, nframes=2646000, comptype='NONE', compname='not compressed')
# (채널 수, 샘플링 width, frame rate, 전체 프레임 수, 압축 타입, human readable한 압축 타입) 반환

print(w.readframes(20))
# b'\x02\x00\x00\x00\x00\x00\x00\x00\\h\xe1\x02\\h\xe1\x02(\xdf\xb3\x05'
# w.readframes(n)
# n개 만큼의 frame을 read하여 bytes 객체로 반환
# 전체 프레임을 읽는 경우, n 자리에 w.getnframes() 전달