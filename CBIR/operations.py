import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.fftpack import dct
import cv2

def dct2(img):
    '''Discrete cosine transform'''
    return dct(dct(img, axis=0, norm='ortho'), axis=1, norm='ortho')

def Canny_Operation(img):
    '''Canny operation for edges'''
    edges = cv2.Canny(img, 100, 200)
    return edges

def hsv(img):
    h = []
    s = []
    v = []
    
    for i in range(256):
        for j in range(256):
            #print(img[i][j][0],img[i][j][1])
            x=float(img[i][j][0])/100
            y=float(img[i][j][1])/100
            #print(x,y)
            if x<=0.2:
                img[i][j][0]=0
            elif x<=0.7:
                img[i][j][0]=1
            else:
                img[i][j][0]=2
                
            if y<=0.2:
                img[i][j][1]=0
            elif y<=0.7:
                img[i][j][1]=1
            else:
                img[i][j][1]=2
                
            if img[i][j][2]<=20:
                img[i][j][2]=0
            elif img[i][j][2]<=50:
                img[i][j][2]=1
            elif img[i][j][2]<=75:
                img[i][j][2]=2
            elif img[i][j][2]<=140:
                img[i][j][2]=3
            elif img[i][j][2]<=160:
                img[i][j][2]=4
            elif img[i][j][2]<=195:
                img[i][j][2]=5
            elif img[i][j][2]<=285:
                img[i][j][2]=6
            elif img[i][j][2]<=305:
                img[i][j][2]=7
            elif img[i][j][2]<=340:
                img[i][j][2]=8
            else:
                img[i][j][2]=0
                
            h.append(img[i][j][0])
            s.append(img[i][j][1])
            v.append(img[i][j][2])
            
    return h,s,v
