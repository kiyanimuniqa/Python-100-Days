class library():
    def __init__(self):
        self.no_of_books= 0
        self.books= []
    def add_books(self,book):
        self.books.append(book)
        self.no_of_books +=1
    def show_books(self):
        print(f" The books are {self.books}")
    def count_books(self):
        print(f"The library has {self.no_of_books} books")

l = library()
l.add_books("python")
l.add_books("java")
l.show_books()
l.count_books()
