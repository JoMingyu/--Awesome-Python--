from PIL import Image
from math import sqrt

img = Image.open('sample_image.jpg')

width, height = img.size


def show_pixels():
    # 1. for loop and getpixel()
    for i in range(int(sqrt(width))):
        for j in range(int(sqrt(height))):
            # for loop가 너무 길어지기 때문에 제곱근을 취함
            # 좌측 상단부터 sqrt(width) x sqrt(height) 만큼의 픽셀이 출력됨
            print(img.getpixel((i, j)))
            # 튜플로 들어가는 걸 주의

    # 2. load()
    pixels = img.load()
    print(pixels[3, 40])
    # 튜플로 인덱싱하는 신기한 방식이다
    # 로딩된 픽셀 맵은 리스트로 캐스팅 불가

    # 3. getdata()
    print(list(img.getdata()))
    # getdata()는 iterable해서 리스트로 캐스팅 가능
    # 성능 문제가 발생할 수도 있겠다

    # 2번의 load()가 가장 좋은 것 같다

show_pixels()


def set_pixels(rgb):
    pixels = img.load()
    for i in range(width):
        for j in range(int(height / 2)):
            pixels[i, j] = rgb
            # 픽셀 맵에 튜플 형태로 값을 던져주면 알아서 세팅된다

set_pixels((30, 30, 80))
img.show()
