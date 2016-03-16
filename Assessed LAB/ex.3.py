# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:22:48 2015

@author: eia14hx
"""

from pylab import *
tmp=range(41)# for some reason, arrange function does not work
x=[]
for n in tmp:
    tmpv=n/2.0
    x.append(tmpv)

y1value=[]
y2value=[]
y3value=[]

for n in x:
    y1=3*n**2
    y1value.append(y1)
for n in x:
    y2=(-0.3)*n**2.8+11*n+600
# unfinished task3 due to limited time
#    for r in range(41):
#        for n in y1value:  
#            if n<y2:
#                print y1value[r]
#                return y1value[r]
            
    y2value.append(y2)    
plot(x,y1value,x,y2value)
show()


