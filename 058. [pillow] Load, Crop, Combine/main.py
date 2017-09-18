from PIL import Image
# PIL 패키지의 Image 모듈

img = Image.open('sample_image.jpg')
# open 함수 사용, 모드는 기본적으로 'r'(read)

print(img)
# mode=RGB, size=1984x1220 등 정보들이 기록된 객체가 출력된다


def show_image():
    input('Press enter to show image')
    print(img.format)
    # 이미지의 확장자
    print(img.size)
    # 사이즈 : (width, height) 형태의 튜플
    print(img.mode)
    # 이미지의 모드(RGB, RGBA 등)

    img.show()
    # show() 메소드를 통해 로컬의 기본 사진 앱을 통해 사진을 띄워준다


def crop_image():
    # 이미지 잘라내기
    input('Press enter to crop image')
    img_width, img_height = img.size
    # 튜플은 이렇게 예쁘게 리턴받을 수 있다

    box = (80, 500, img_width, img_height)
    # 좌측 상단을 (0, 0)으로 두고, 우측 하단 방향으로 값이 상승한다고 치면
    # start_x, start_y, end_x, end_y 순서

    img.crop(box).show()
    # crop된 새로운 이미지를 반환


def combine_image():
    input('Press enter to combine images')
    img_to_combine = Image.open('image_to_combine.png')
    # combine을 위한 이미지 open

    comb_width, comb_height = img_to_combine.size
    comb_box = (300, 300, comb_width + 300, comb_height + 300)
    # 여기도 start_x, start_y, end_x, end_y 순서

    img.paste(img_to_combine, comb_box)
    # paste 함수를 통해 결합, 반환은 없음(이미지 객체에 덮어씌움)
    img.show()

show_image()
crop_image()
combine_image()
