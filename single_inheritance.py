#parent class
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by the animal")
#child class
class dog(animal):
    def __init__(self,name,breed):
       animal.__init__(self,name,species="dog")
       self.breed= breed
    def make_sound(self):
        print("Bark!")
        
d = dog("Tommy", "German Shepherd")
d.make_sound()
a=animal("dog","dog")
a.make_sound()