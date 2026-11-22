class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 

e1= Employee("muniqa", 12000)
print(e1.name)
print(e1.salary)


string = "harry-120000"
e2= Employee(string.split("-")[0], string.split("-")[1])
print(e2.name)
print(e2.salary)