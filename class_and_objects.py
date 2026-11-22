# class Person:
#     name="Muniqa Kiyani"
#     occupation="Software Developer"
#     newworth= 10
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a=Person()
# # # a.name="munazza"
# # # a.occupation="Accountant"
# # print(a.name,a.occupation)
# a.info()

# class employe: #define a class
#     employe_id=0 #define a property
# #create 2 objects of the class
# employe1 = employe()
# employe2 = employe()
# #access properties using emplye1
# employe1.employe_id=47767
# print(f"employe ID:{employe1.employe_id}")
# #access properties using employe2
# employe2.employe_id=1222
# print(f"employe ID:{employe2.employe_id}")

class person:

    def __init__(self,name,occ):
        print("hey i am a person")
        self.name= name
        self.occ= occ

    def info(self):
        print(f"{self.name} is a {self.occ}")
    
a=person("muniqa","HR")
b=person("sara","accountant")
c=person("biya","banker")
a.info()
b.info()
c.info()