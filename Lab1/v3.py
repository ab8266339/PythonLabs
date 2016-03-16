# -*- coding: utf-8 -*-
"""
Created on Fri Oct 02 14:25:39 2015

@author: eia14hx
"""

# Converts distance in miles to kilometers
def convert_distance(miles):
    kilometers = (miles * 8.0) / 5.0
    print "Converting distance in miles to kilometers:"
    print "Distance in miles:     ", miles
    print "Distance in kilometers:", kilometers
convert_distance(50)