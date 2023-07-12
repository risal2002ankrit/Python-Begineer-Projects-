# install pillow
# import pillow
# open up the image we want to resize
# print the current size of that image
# specify the  size we wanna change it to
# save the new resized image

from PIL import Image


def resized_image(size1, size2):
    image= Image.open('mypic.jpg')

    print(f"current size : {image.size}")

    resize_image = image.resize((size1, size2))

    resize_image.save('mynewpic.jpg')

size1 = int(input('enter width: '))
size2 = int(input('enter length: '))
resized_image(size1, size2)


