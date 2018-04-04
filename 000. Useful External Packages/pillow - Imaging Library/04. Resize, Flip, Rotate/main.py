from PIL import Image

img = Image.open('sample_image.jpg')

input('Press enter to show resized image')
img.resize((1000, 1000)).show()

input('Press enter to show flipped image')
img.transpose(Image.FLIP_LEFT_RIGHT).show()

input('Press enter to show span image')
img.transpose(Image.ROTATE_180).show()
