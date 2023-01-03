class Book:
    def __init__(self, nm, pr, pgs):
        self.book_name = nm
        self.price = pr
        self.pages = pgs

    def __add__(self, other):
        return self.price + other.price # Operator Overloading '+'
    
b1 = Book("Basic Python", 250, 300)

b2 = Book("Advance Python", 450, 700)

print(b1 + b2)