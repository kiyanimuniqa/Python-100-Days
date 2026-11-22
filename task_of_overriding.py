class Animal:
    def __init__(self,name):
        self.name = name
    def sound(self):
        return ("koi awaz")

class dog(Animal):
    def __init__(self,name,breed):
        super(). __init__(name)
        self.breed=breed
    def sound(self):
        return (super().sound() + " - Bhow Bhow !")

d= dog("Tommy"," German shepherd")
print(d.name)
print(d.breed)
print(d.sound())
    
