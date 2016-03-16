from pylab import *

x = []
for i in range(0,200):
	x.append(i/10.0)
	
Ys1=[]
Ys2=[]
for i in x:
	y1=i*i+20
	y2=(i/2)**3-100
	Ys1.append(y1)
	Ys2.append(y2)

subplot(211)	
plot(x,Ys1,'go-')
subplot(212)	
plot(x,Ys2,'go-')
show()
    
    
