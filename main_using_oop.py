class Book:

    def __init__(self , book_title , book_author , book_id):
        self.book_title = book_title
        self.book_author = book_author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"{self.book_title} by {self.book_author} with ID : {self.book_id}"
    
    def __repr__(self):
        return self.__str__()

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Enjoy reading {self.book_title}")
        else:
            print("Currently not available")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Hope you enjoyed {self.book_title}")
        else:
            print("Book doesn't belong to this library")


class Library:

    def __init__(self):
        self.next_id = 1
        self.books = []

    def add_book(self):
        
        book_title = input("Enter the name of the book : ")
        book_author = input("Enter the author of the book : ")

        book = Book(book_title , book_author , self.next_id)

        self.books.append(book)
        print(f"{book.book_title} has been added successfully with ID {self.next_id}")
        self.next_id += 1
    

library = Library()
library.add_book()
library.add_book()
print(library.books)



