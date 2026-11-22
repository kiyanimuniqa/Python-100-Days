class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # Triggered by print() or str()
    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    # Triggered by len()
    def __len__(self):
        return self.pages

    # Triggered by +
    def __add__(self, other):
        return self.pages + other.pages

book1 = Book("Dune", 412)
book2 = Book("1984", 328)

print(book1)          # Calls __str__ -> 'Dune' (412 pages)
print(len(book1))     # Calls __len__ -> 412
print(book1 + book2)  # Calls __add__ -> 740
