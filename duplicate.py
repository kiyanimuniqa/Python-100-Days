class shape():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return (self.x * self.y)

class circle(shape):
    def __init__(self,radius):
        self.radius = radius
        super() .__init__(radius, radius)
    def area(self):
        return(f"The area of a circle is:{super().area()* 3.14}")
print(circle(7).area())


class triangle (shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
        super() .__init__(base,height)
    def area(self):
        return (f"The area of a triangle is:{super().area() * 0.5}")

print(triangle(3,4).area())
