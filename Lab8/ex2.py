# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:16:47 2015

@author: eia14hx
"""
a=[]
b=[]
n=0
def add_numlists(a,b):
	c=[]
	if len(a)==len(b):
		leng=len(a)
#		print leng
		for n in range(leng):
			value=a[n]+b[n]
			c.append(value)
		print c
		return c
	else: return None

	
