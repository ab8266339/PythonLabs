# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:46:16 2015

@author: eia14hx
"""

from pylab import *
ap1=[-150.4,200.5]
ap2=[122.6,64.0]
av1=[4.9,-7.1]
av2=[-5.2,-2.95]

#d=[sqrt((ap1[0]-ap2[0])**2+(ap1[1]-ap2[1])**2)]
#print d

d=[]
for n in range(50):
	ap1[0]=ap1[0]+av1[0]
	ap1[1]=ap1[1]+av1[1]
	ap2[0]=ap2[0]+av2[0]
	ap2[1]=ap2[1]+av2[1]
	d.append(sqrt((ap1[0]-ap2[0])**2+(ap1[1]-ap2[1])**2))
	
	print d
plot(range(50),d)