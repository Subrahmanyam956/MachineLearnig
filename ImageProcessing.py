#!/usr/bin/env python
# coding: utf-8

##ImageProcessing One

from PIL import Image

#open a Particular Image From a Path
try :
    img = Image.open("detection1Learn.jpg")
except IOError:
    pass



#Retrieving the Size of an Image
#Image.size attribute returns the Image width first and then Height of the Image
img = Image.open("detection1Learn.jpg")
try :
    
    width, height = img.size   
    print(width)
    print(height)
except IOError :
    print("something went wrong")



#Saving an image
img.save("imageSaving.jpg")
#format is optional , if not given the default format is the format extension of the image



#Rotating the Image
#using img.rotate()
img2 = img.rotate(45)
img2.save("RotatedImageFor45.jpg")



##Cropping the Image
#Changing the Width and Height of the Image
#image.crop takes a 4 tuple input i.e., the area of the cropped image 
#those are the Coordinates for the Cropping
width, height = img.size
width2 = width/2
height2 = height/2
area = (0, 0, width2, height2)
crop = img.crop(area)
crop.save("croppedHalf.jpg")



#notWorking
##Resizing the Image
#image.resize
res = img.resize((width2, height2))
res.save("resizedToHalf.jpg")


##pasting One Image over the Other
#img.paste()
pasteImg = Image.open("detection1Learn.jpg")
pasteImg2 = Image.open("detection2Learn.jpg")

pasteImg.paste(pasteImg2, (20, 20))
pasteImg.save("PastedOneOverOther.jpg")



##Histogram of the Image
print(img.histogram())


#transposing of an Image
#Mirror Image

transposedImg = img.transpose(Image.FLIP_LEFT_RIGHT)
transposedImg.save("transposedIsMirror.jpg")


##splitting image into parts
print(img.split())


#not Working
##Conversion into BitMap
#tobitMap
print(img.mode)
print(img.tobitmap())
#print(type((img.tobitmap())))




##Thumbnail Creation
img.thumbnail((200, 200))
img.save("ThumbnailCreated.jpg")






