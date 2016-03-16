from pylab import *
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:39:49 2015

@author: Hao Xu
"""
in_fs = open('noisy_signal.txt')
#in_ps = open('pure_signal.txt')
ts=[]
vs=[]
x=[]
y=[]
bs=[]


for line in in_fs:
	vals=line.split()
	#print vals
	t=float(vals[0])
	ts.append(t)
	v=float(vals[1])
	vs.append(v)
#print 'ts',ts
#print 'vs',vs
subplot(211)
plot(ts,vs,'go-')


for i in range(0,3000):
	j=i+20
	x=vs[i:j]
	b=sum(x)
	b1=b/20
	bs.append(b1)
#	if j==3000: break
	

#plot(x,y)
subplot(212)
plot(ts,bs,'go-')


