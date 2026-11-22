class rectangle:
    def __init__(self,length,width):
        self.length= length
        self.width= width
    def area(self):
        print(f"Area: {self.length* self.width}")
    def perimeter(self):
        print(f"Perimeter:  { 2 * self.length + self.width}")

a=rectangle(4,5)
a.area()
a.perimeter()