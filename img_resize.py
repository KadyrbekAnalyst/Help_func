#!/usr/bin/env python3
import os
import sys
import cv2 as cv

# default values
imgs_folder = 'C:\KazakhAI\garbage_328_start'
output_folder = 'C:\KazakhAI\garbage_resize_328START'
width = 640
height = 640
inter = cv.INTER_AREA

# find all images
imgs = [i for i in os.listdir(os.path.join(".", imgs_folder)) if '.jpg' in i or '.jpeg' in i or '.JPEG' in i or '.JPG' in i]

newSize = (int(width), int(height))
for i in imgs:
    # open image
    img = cv.imread(os.path.join(".", imgs_folder, i))

    # resize image
    img = cv.resize(img, newSize, interpolation = inter)

    # save image
    cv.imwrite(os.path.join(".", output_folder, i), img)
    
    # verbose output
    print(f"#imgresize: <{i}> converted!")
    
    
#print(os.path.join(".", imgs_folder, imgs[0]))
