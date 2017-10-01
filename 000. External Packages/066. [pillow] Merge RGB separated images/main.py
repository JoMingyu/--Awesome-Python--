from PIL import Image

img = Image.open('sample_image.jpg')

r, g, b = img.split()
# split() 메소드를 이용해 rgb 채널을 분리했었다
# 얘네를 합치기 위해 Image 모듈의 merge 함수를 사용한다

# r g b 각각의 배열에 따라 6개 경우의 수가 나온다
input('Press enter to show RGB merged image')
Image.merge('RGB', (r, g, b)).show()

input('Press enter to show RBG merged image')
Image.merge('RGB', (r, b, g)).show()
# 붉은 계열

input('Press enter to show BRG merged image')
Image.merge('RGB', (b, r, g)).show()
# 민트색에 가까움

input('Press enter to show BGR merged image')
Image.merge('RGB', (b, g, r)).show()
# 푸른 계열

input('Press enter to show GRB merged image')
Image.merge('RGB', (g, r, b)).show()
# 초록 계열

input('Press enter to show GBR merged image')
Image.merge('RGB', (g, b, r)).show()
# 보라색 계열
