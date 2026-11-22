class vehicle(): #parent class
    def start(self):  #method ( function: inside a class)
        print("vehicle started")
    
class car(vehicle):  #child class of parent classs
    pass
my_car = car()
my_car.start()

class bird():  #parent class
    def fly(self):
        print("bird fly")
class eagle(bird):  #child class of parent class
    pass   #use this word bcz child class have any function and it inherits from parent class
my_eagle = eagle()   #create an object
my_eagle.fly()    #calling a function


