class dog():
    def __init__(self,name,age):
        self.name= name
        self.age= age
    def bark(self):
        print(f"{self.name} says Woof  WOOf!")

a= dog("Tomy",7)
a.bark()
