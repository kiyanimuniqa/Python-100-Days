class Employee:  #define my class
    company= "Apple"   #class variable that is same for all instance of the classs
    def __init__(self,name):
        self.name= name
        self.raise_amount= 0.02
    def showDetails(self):
        print(f"The name of employe is {self.name} and raise amount is {self.raise_amount} and the company name is {self.company}")
emp1= Employee("harry")
emp1.raise_amount= 0.4
emp1.showDetails()
emp2= Employee("muniqa")
emp2.company ="Dell"
emp2.showDetails()