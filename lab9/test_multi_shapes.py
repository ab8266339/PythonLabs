
from MovingShapes import *

frame = Frame()
numshapes = 3
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame,100))
    shapes.append(Diamond(frame,100))
    shapes.append(Circle(frame,100))

for i in range(100):
    for shape in shapes:
        shape.moveTick()

