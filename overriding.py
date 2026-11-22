class shape:    #define a class
    def __init__(self,x,y):  #use constructor
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class rectangle(shape):     #child classs of parent class
    def __init__(self,length,width):
        super() .__init__ (length, width)
    def area(self):
        return (f"The area of rectangle is:{super().area()}")
print(rectangle(4,5).area())
class square(shape):    #child classs of parent classs
    def __init__ (self,side):
        self.side = side
        super() .__init__ (side, side)
    def area(self):
        return (f"The area of sqaure is:{super().area()}")
print(square(6).area())
class triangle(shape):  #child class of parent class
    def __init__ (self,base,height):
        self.base= base
        self.height= height
        super() .__init__(base,height)
    def area(self):
        return (f"The area of a triangle is:{super().area() * 0.5}")
print(triangle(10,4).area())

