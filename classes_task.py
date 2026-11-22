class student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks
    def info(self):
        print(f"{self.name} got {self.marks} marks")
    
a=student ("Muniqa", 989)
b=student ("hammad", 766)
a.info()
b.info()

