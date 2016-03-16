# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:48:40 2015

@author: eia14hx
"""

from pylab import *
img=imread('USFD_hidden_msg.png')
(d1,d2,d3)= img.shape

for i in range(d1):
    for j in range (d2):
        for k in range (d3):
#            print img[i,j,k]
            img[i,j,k]=10*img[i,j,k]
            img[i,j,k]=img[i,j,k]-int(img[i,j,k])
            if img[i,j,k]<0.5:
                img[i,j,k]=0
            else:img[i,j,k]=1
            
imshow(img)
show()