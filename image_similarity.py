import skimage
from skimage import data, io, filter
import numpy as np
import math

def loadImg(filename):
    img = io.imread(filename)*255
    return img

def imageSSD(file1, file2):
    img1 = loadImg(file1)
    img2 = loadImg(file2)
    if img1.shape != img2.shape:
        return "Images Not Same Size!"
    else:
        x, y, z = img1.shape
        return math.sqrt(np.sum((img1[:,:,0:3]-img2[:,:,0:3])**2) / (x * y * 3));


print "SSD (v1s1, v2s1) " + str(imageSSD("images/v1s1.png", "images/v2s1.png"))
print "SSD (v1s2, v2s2)  " + str(imageSSD("images/v1s2.png", "images/v2s2.png"))
print "SSD (v1s3, v2s3)  " + str(imageSSD("images/v1s3.png", "images/v2s3.png"))

print "SSD (v1s2, v2s3)  " + str(imageSSD("images/v1s2.png", "images/v2s3.png"))
print "SSD (v1s3, v2s2)  " + str(imageSSD("images/v1s3.png", "images/v2s2.png"))
print "SSD (v1s3, large)  " + str(imageSSD("images/v1s3.png", "images/large.png"))
