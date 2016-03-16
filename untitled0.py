# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 20:23:57 2015

@author: eia14hx
"""

def sum_of_reciprocals(N):
    value=0
    value1=0
    for a in range (N):
        value=(1/(a+1.0))
        value1=value+value1
    print value1
    return value1
sum_of_reciprocals(2)