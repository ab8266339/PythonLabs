# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:16:54 2015

@author: eia14hx
"""
from pylab import *
def circle_area(d):
    a=pi*0.5*d*0.5*d
    return a


dl=[]
alist=[]
def list_of_clrcles(dl):
    for n in dl:
        area=circle_area(n)
        alist.append(area)
        print area
    return alist