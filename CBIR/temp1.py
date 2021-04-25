from os import listdir
import os
import operations as op
import cv2

def loadImages(path, result):
    imagesList = listdir(path)
    i = 0
    
    for image in imagesList:
        filename = result+str(i)+'.jpg'
        
        frame = cv2.imread(os.path.join(path, image))
        edges = op.Canny_Operation(frame)
        
        cv2.imwrite(filename, edges)
        i += 1

path = "C:/Users/DELL/Pictures/Screenshots/back/"
result = 'H:/Python/CBIR/temp/'

# your images in an array
imgs = loadImages(path, result)
