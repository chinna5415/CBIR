import cv2
import numpy as np
import operations as op
from scipy import stats

img = cv2.imread('urop.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

h, s, v = op.hsv(img)

# mean
mean_h, mean_s, mean_v = np.mean(h), np.mean(s), np.mean(v)

# standard deviation
sd_h, sd_s, sd_v = np.std(h), np.std(s), np.std(v)

# skewness
skew_h, skew_s, skew_v = stats.skew(h), stats.skew(s), stats.skew(v)

# kurtosis
kurtosis_h, kurtosis_s, kurtosis_v = stats.kurtosis(h), stats.kurtosis(s), stats.kurtosis(v)

#color feature vector
color_v = [[mean_h,sd_h,skew_h,kurtosis_h],
           [mean_s,sd_s,skew_s,kurtosis_s],
           [mean_v,sd_v,skew_v,kurtosis_v]]

imx = cv2.imread('urop.jpeg',0)

#edges image
edges = op.Canny_Operation(imx)

