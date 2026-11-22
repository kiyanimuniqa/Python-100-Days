class animal():  #parent class
    def __init__ (self,name):   #method to call a function
        self.name = name
class cat(animal): 
    def sound (self):
        print(self.name, "Meowww")

My_cat = cat ("mimi")
My_cat.sound()