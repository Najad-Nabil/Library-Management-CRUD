class Book:

    def __init__(self , book_title , book_author , book_id):
        self.book_title = book_title
        self.book_author = book_author
        self.book_id = book_id
        self.is_available = True
        self.borrowed_by = None

    def to_dict(self):
        return {
            "title" : self.book_title,
            "book_author" : self.book_author,
            "book_id" : self.book_id,
            "is_available" : self.is_available,
            "borrowed_by" : self.borrowed_by
        }
    
    @classmethod
    def from_dict(cls , data):
        book = cls(
            data["title"],
            data["book_author"],
            data["book_id"]
        )

        book.is_available = data["is_available"]
        book.borrowed_by = data["borrowed_by"]
        return book

    def __str__(self):
        return f"{self.book_title} by {self.book_author} with ID : {self.book_id}"
    
    def __repr__(self):
        return self.__str__()

    def borrow_book(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True