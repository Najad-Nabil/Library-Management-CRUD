from library import Library
library = Library()

def get_valid_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Enter a valid number")
    
while True:    
    print("""1. Add books
2. Remove book
3. Search book
4. View all books
5. Borrow book
6. Return book
7. Add member
8. Search Member
9. Remove Member
10. View books borrowed by a user
0. Exit""")
    choice = get_valid_int("Enter your choice : ")
    
    if choice == 1:
        library.add_book()

    elif choice == 2:
        book_id = get_valid_int("Enter the ID of the book you want to remove : ")
        library.remove_book(book_id)

    elif choice == 3:
        book_id = get_valid_int("Enter the ID of the book you want to search for : ")
        book = library.search_book(book_id)
        if book:
            print(book)
        else:
            print("Book not found")

    elif choice == 4:
        library.view_all_books()

    elif choice == 5:
        book_id = get_valid_int("Enter the ID of the book you want to borrow : ")
        member_id = get_valid_int("Enter the ID of the member who needs the book : ")
        library.borrow_book(book_id , member_id)

    elif choice == 6:
        book_id = get_valid_int("Enter the ID of the book you want to return : ")
        member_id = get_valid_int("Enter the ID of the member who needs to return the book : ")
        library.return_book(book_id , member_id)

    elif choice == 7:
        name = input("Enter the name of the person : ")
        library.add_member(name)

    elif choice == 8:
        member_id = get_valid_int("Enter the ID of the member you want to search for : ")
        member = library.search_member(member_id)
        if member:
            print(member)
        else:
            print(f"Member with ID {member_id} does not exist")

    elif choice == 9:
        member_id = get_valid_int("Enter the ID of the member you want to remove : ")
        result = library.remove_member(member_id)

        if result == "MEMBER_DELETED":
            print(f"Member with ID {member_id} successfully deleted")
        elif result == "MEMBER_NOT_FOUND":
            print(f"Member with ID {member_id} does not exist")
        elif result == "HAS_BOOKS":
            print(f"Person with ID {member_id} currently have books and cannot be deleted")

    elif choice == 10:
        member_id = get_valid_int("Enter the ID of the member you want get the list of borrowed books of : ")
        library.view_borrowed_books(member_id)

    elif choice == 0:
        break

    else:
        print("Enter a valid number")





