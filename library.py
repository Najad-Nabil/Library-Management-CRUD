import json

from book import Book

class Library:

    def __init__(self):
        self.next_id = 1
        self.books = []
        self.load_data()

    def save_data(self):
        data = []

        for book in self.books:
            data.append(book.to_dict())

        with open("lib-data.json" , "w") as file:
            json.dump(data , file , indent=4)

    def load_data(self):
        try:
            with open("lib-data.json" , "r") as file:
                data = json.load(file)

            for book_data in data:
                book = Book.from_dict(book_data)
                self.books.append(book)

        except (FileNotFoundError , json.JSONDecodeError):
            pass

    def add_book(self):
        
        book_title = input("Enter the name of the book : ")
        book_author = input("Enter the author of the book : ")

        book = Book(book_title , book_author , self.next_id)

        self.books.append(book)
        self.save_data()

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

    def search_book(self , book_id):
        for book in self.books:
           if book.book_id == book_id:
               return book
                
        return None  
    
    def borrow_book(self , book_id):
        book = self.search_book(book_id)
        if not book:
            print("Book does not exist")
        elif not book.is_available:
            print("Book is currently unavailable")
        else:
            book.borrow_book()
            self.save_data()
            print(f"You borrowed {book.book_title}")

    def return_book(self , book_id):
        book = self.search_book(book_id)
        if not book:
            print("Book does not exist")
        elif book.is_available:
            print("Book doesn't belong to this library")
        else:
            book.return_book()
            self.save_data()
            print(f"Thanks for returning {book.book_title}")

    def remove_book(self , book_id):
        book = self.search_book(book_id)
        if not book:
            print("Book doesn't exist")
        else:
            self.books.remove(book)
            self.save_data()
            print(f"{book.book_title} removed successfully")
        
