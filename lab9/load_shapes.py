
from Shapes import *

frame = Frame()
s1= Shape('square',100)
s1.goto(200,100)
x=0
y=0
for i in range (100):
	s1.goto(x,y)
	x=x+dx
	y=y+dy