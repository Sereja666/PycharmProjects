from PIL import Image

im = Image.open('C:\\PyTest\\abby\\я1.jpg')

im_rotate = im.rotate(90, expand=True)
im_rotate.save('guido_90.jpg', quality=95)
im.close()