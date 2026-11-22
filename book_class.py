class Book():  #define a class
    def __init__(self, title, author):   #use constructor (__init__) to initialize the object's attributes
        self.title = title      
        self.author = author
    def details(self):   #method to show details
        print(f"{self.title} by {self.author} Rowling")

a=Book("harry Potter", "J.K")  #create object of the class
a.details()  #call the details method
