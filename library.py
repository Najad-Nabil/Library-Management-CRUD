import json

from book import Book
from member import Member

class Library:

    def __init__(self):
        self.next_id = 1
        self.next_member_id = 1
        self.books = []
        self.members = []
        self.load_data()

    def save_data(self):
        data = {
            "next_id" : self.next_id,
            "next_member_id" : self.next_member_id,
            "books" : [],
            "members" : []
        }

        for book in self.books:
            data["books"].append(book.to_dict())

        for member in self.members:
            data["members"].append(member.to_dict())

        with open("lib-data.json" , "w") as file:
            json.dump(data , file , indent=4)

    def load_data(self):
        try:
            with open("lib-data.json" , "r") as file:
                data = json.load(file)

            self.next_id = data["next_id"]
            self.next_member_id = data["next_member_id"]

            for book_data in data["books"]:
                book = Book.from_dict(book_data)
                self.books.append(book)

            for member_data in data["members"]:
                member = Member.from_dict(member_data)
                self.members.append(member)

        except (FileNotFoundError , json.JSONDecodeError):
            pass

    def add_book(self):
        
        book_title = input("Enter the name of the book : ")
        book_author = input("Enter the author of the book : ")

        book = Book(book_title , book_author , self.next_id)

        self.books.append(book)

        print(f"{book.book_title} has been added successfully with ID {self.next_id}")
        self.next_id += 1
        self.save_data()

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
    
    def borrow_book(self , book_id , member_id):
        book = self.search_book(book_id)
        if not book:
            print("Book does not exist")
        elif not book.is_available:
            print("Book is currently unavailable")
        else:
            member = self.search_member(member_id)
            if member is None:
                print(f"No member exist with ID {member_id}")
            else:
                member.borrowed_books.append(book_id)
                book.borrow_book()
                book.borrowed_by = member_id
                self.save_data()
                print(f"Enjoy {book.book_title}")

    def return_book(self , book_id , member_id):
        book = self.search_book(book_id)
        if not book:
            print("Book does not exist")
        elif book.is_available:
            print("Book already available in this library")
        else:
            member = self.search_member(member_id)
            if member is None:
                print(f"Member with ID {member_id} does not exist")
            else:
                book.return_book()
                member.borrowed_books.remove(book_id)
                book.borrowed_by = None
                self.save_data()
                print(f"Thanks for returning {book.book_title}")

    def remove_book(self , book_id):
        book = self.search_book(book_id)
        if not book:
            print("Book doesn't exist")
        elif book.borrowed_by:
            member = self.search_member(book.borrowed_by)
            print(f"Book is currently borrowed by {member.member_name}")
        else:
            self.books.remove(book)
            self.save_data()
            print(f"{book.book_title} removed successfully")
        
    def add_member(self , member_name):
        member = Member(member_name , self.next_member_id)
        self.members.append(member)
        print(f"Member added successfully with ID {self.next_member_id}")
        self.next_member_id += 1
        self.save_data()

    def search_member(self , member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        
        return None
    
    def remove_member(self , member_id):
        member = self.search_member(member_id)
        
        if not member:
            return "MEMBER_NOT_FOUND"
        if member.borrowed_books:
            return "HAS_BOOKS"
        self.members.remove(member)
        self.save_data()
        return "MEMBER_DELETED"