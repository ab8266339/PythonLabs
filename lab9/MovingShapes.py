
from Shapes import *
from pylab import random as r

####################################################

class MovingShape:
    def __init__(self,frame,shape,diameter):
        self.shape = shape
        self.diameter = diameter
        self.figure = Shape(shape,diameter)
        self.minx = diameter/2
        self.maxx = frame.width - diameter/2
        self.miny = diameter/2
        self.maxy = frame.height - diameter/2
        self.x = self.minx + r() *(self.maxx-self.minx)
        self.y = self.miny + r() *(self.maxy-self.miny)
        self.dx=10*r()+5
        self.dy=10*r()+5	

    def goto(self,x,y):
        self.figure.goto(x,y)
            
    def moveTick(self):
        self.x+=self.dx
        self.y+=self.dy
        self.goto(self.x,self.y)
    
        if self.x+(1/2)*self.diameter >= self.maxx:
            self.dx*=-1
            self.report_bounce()
        if self.y+(1/2)*self.diameter >= self.maxy:
            self.dy*=-1
            self.report_bounce()
        if self.x<= self.minx:
            self.dx*=-1
            self.report_bounce()
        if self.y<= self.miny:
            self.dy*=-1
            self.report_bounce()
####################################################       
    def area(self):
        return self.diameter ** 2
#        self.area=0
#        if self.shape=="square":
#            area=self.diameter**2
#        elif self.shape=="diamond":
#            area=self.diameter**2/2
#        elif self.shape=="circle":
#            area=self.diameter**2*3.14
#        else:pass
#        return area
    def report_bounce(self):
#        if self.x== 0 or self.x==frame.width:
        print "I am a bouncing", self.shape, "my area is ",self.area()
    def check_interaction(self):
        
        

        

####################################################

class Square(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'square',diameter)
        

####################################################
class Diamond(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'diamond',diameter)
        self.diameter=diameter*(2)**(1/2)
        self.minx = (diameter*(2)**(1/2))/2
        self.maxx = frame.width - (diameter*(2)**(1/2))/2
        self.miny = (diameter*(2)**(1/2))/2
        self.maxy = frame.height - (diameter*(2)**(1/2))/2
        
#    def area(self):
#        self.area=self.diameter**2
        
####################################################

class Circle(MovingShape):
    def __init__(self,frame,diameter):
        MovingShape.__init__(self,frame,'circle',diameter)

    def area(self):
        return (0.5*self.diameter)**2*3.14
        

####################################################

