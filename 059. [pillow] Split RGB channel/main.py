from PIL import Image

img = Image.open('sample_image.jpg')
# 이미지에는 mode라는 속성이 있다
print(img.mode)
# RGB 모드라고 나온다. 이 RGB를 따로 분리할 수 있다

r, g, b = img.split()
print(type(r))
# 타입은 PIL.Image.Image
# 엄연한 이미지 객체

input('Press enter to show R channel')
r.show()

input('Press enter to show G channel')
g.show()

input('Press enter to show B channel')
b.show()
