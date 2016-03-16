# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:10:45 2015

@author: eia14hx
"""
v=[]
def get_negatives(v):
    nv=[]
    for n in v:
        if n<0:
            nv.append(n)
    return nv