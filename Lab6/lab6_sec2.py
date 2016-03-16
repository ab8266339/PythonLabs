# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 11:15:33 2015

@author: eia14hx
"""

from pylab import *
im=imread('che.png')
[d1,d2,d3]=im.shape
#print size[0],size[1],size[2]
#imshow(im)
#show()
#1
img1=array(im)
img2=array(im)
img3=array(im)
img4=array(im)
img5=array(im)

#for i in range(d1):
#    for j in range(d2):
#        for k in range(d3):
#            img3[i,j,k] = img1[i,j,k]
#            img3[i+d1, j, k] = img2[i,j,k]




for i in range(d1):
    for j in range(d2):
        for k in range(d3):
            if img1[i,j,k] >0.5:
                img1[i,j,k]=1
            else:
                img1[i,j,k]=0
#2
for i in range(d1):
    for j in range(d2):
        pixel2=img2[i,j]
        if sum(pixel2)<1:
            img2[i,j]=(1.0,0.0,0.0)
        else:
            img2[i,j]=(0.0,0.0,0.0)
#3
img3=array(img2)
for j in range(55,140):
    for i in range (53,170):
        pixel3 = img3 [i,j]
        if sum (pixel3)==0:
            img3[i,j]=(1.0,1.0,1.0)
#4
for i in range(d1):
    for j in range(d2):
        pixel4=img4[i,j]
        if average(pixel4)<0.33:
            img4[i,j]=(0.0,0.0,1.0)
        elif average(pixel4)<0.66:
            img4[i,j]=(0.0,1.0,0.0)
        else:
            img4[i,j]=(1.0,0.0,0.0)

#5
imgc=imread('chick.png')
[e1,e2,e3]=imgc.shape
for i in range(e1):
    for j in range (e2):
        img5[i,j]=imgc[i,j]
for i in range (e1):
    for j in range (e2):
        img5[i+53,j+55]=imgc[i,j]



img6=zeros((5*d1,d2,d3))

for i in range(d1):
    for j in range(d2):
        for k in range(d3):
            img6[i,j,k] = img1[i,j,k]
            img6[i+d1, j, k] = img2[i,j,k]
            img6[i+2*d1,j,k] = img3[i,j,k]
            img6[i+3*d1,j,k] = img4[i,j,k]
            img6[i+4*d1,j,k] = img5[i,j,k]
imshow(img6)

show()
