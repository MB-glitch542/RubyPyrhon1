# managing a library system
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        return f"The Title {self.title}, Author {self.author}"

# child class

class LibraryBook(Book):
    def __int__(self,title,author,isbn,copies_available):
        super().__init__(title,author)
        self.isbn=isbn
        self.copies_available=copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"no of copies {self.title} unavailable"
    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. Copies left: {self.copies_available}"
# usage
book1=LibraryBook("inheritance","Adrian",789,20)
print(book1.display_info())
print(book1.borrow_book())