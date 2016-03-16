# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:04:23 2015

@author: eia14hx
"""

def sum_of_reciprocals(innum):
#	innum=input("Type in the number you want")
	valuesum=0
	for n in range(innum):
		value=1/(n+1.0)
		valuesum=value+valuesum
#		print value
	print valuesum
	return 

		