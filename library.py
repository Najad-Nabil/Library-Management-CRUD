from book import Book

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

    def view_all_books(self):
       for index , book in enumerate(self.books , start = 1):
            print(f"""Book No : {index}
Book Name : {book.book_title}
Author : {book.book_author}
Book ID : {book.book_id}""")
            if book.is_available:
                print("Availablity : Currently available")
            else:
                print("Availablity : Out of Stock")
            print("-" * 30)

    def search_books(self , book_id):
        found = False
        for book in self.books:
           if book.book_id == book_id:
               print(book)
               found = True
               break
                
        if not found:
           print(f"Book with ID {book_id} does not exist")  