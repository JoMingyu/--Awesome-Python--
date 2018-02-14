from PIL import Image, ImageFilter
# ImageFilter라는 모듈을 통해 간편하게 이미지 필터링을 해볼 수 있다

img = Image.open('sample_image.jpg')

input('Press enter to see BLUR')
img.filter(ImageFilter.BLUR).show()

input('Press enter to see EMBOSS')
img.filter(ImageFilter.EMBOSS).show()

input('Press enter to see CONTOUR')
img.filter(ImageFilter.CONTOUR).show()

input('Press enter to see EDGE_ENHANCE')
img.filter(ImageFilter.EDGE_ENHANCE).show()

input('Press enter to see SMOOTH')
img.filter(ImageFilter.SMOOTH).show()

input('Press enter to see SMOOTH_MORE')
img.filter(ImageFilter.SMOOTH_MORE).show()

input('Press enter to see FIND_EDGES')
img.filter(ImageFilter.FIND_EDGES).show()

input('Press enter to see SHARPEN')
img.filter(ImageFilter.SHARPEN).show()
