
from MovingShapes import *

frame = Frame()
numshapes = 3
shapes = []

for i in range(numshapes):
    shapes.append(Square(frame,100))

for i in range(100):
    for shape in shapes:
        shape.moveTick()

    for j in range(1,len(shapes)):
        for k in range(j):
            shapes[j].check_interaction(shapes[k])

