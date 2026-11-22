class Car:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
    def drive(self):
        print(f"{self.color} {self.brand} is driving")   

a=Car("red","corolla")
b=Car("black","ferrarri")
a.drive()
b.drive()


