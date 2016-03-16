
from MovingShapes import *

frame = Frame()
shape1 = Square(frame,100)

x=0
y=0
for i in range(100):
    shape1.moveTick()

