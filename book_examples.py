class Book:
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))

    def increase_no_of_copies(self, how_much):
        self.copies += how_much

    def decrease_no_of_copies(self, how_much):
        self.copies -= how_much


book1 = Book('Python Programming', 200)
book1.increase_no_of_copies(25)
book2 = Book('Crypto using BTC', 100)
book2.decrease_no_of_copies(50)

print(book1)
print(book2)
