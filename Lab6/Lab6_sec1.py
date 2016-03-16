# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 10:53:23 2015

@author: eia14hx
"""

from pylab import *
img = imread('chick.png')
imshow(img)
show()

(d1,d2,d3)=img.shape
for i in range(d1):
	for j in range(d2):
		for k in range (d3):
			img [i,j,k]= 1 - img[i,j,k]

for i in range (d1):
	for j in range (d2):
		pixel = img[i,j]
		if sum(pixel)<1.5:
			img[i,j]=(.0,.0,.0)
