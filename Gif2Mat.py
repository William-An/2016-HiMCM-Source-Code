from PIL import Image

im=Image.open("./map/AK99501.gif")

source=im.split()
source[0].show()
mask1=source[0].point(lambda i:i== 255 and 255)
mask2=source[1].point(lambda i:i==209 and 255)
mask3=source[2].point(lambda i:i== 36 and 255)
im.paste(im,None,mask1)
im.paste(im,None,mask2)
im.paste(im,None,mask3)
im.show()

