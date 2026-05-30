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
        self.is_available = False

    def return_book(self):
        self.is_available = True