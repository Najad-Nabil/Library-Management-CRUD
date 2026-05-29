import json

def load_data():
    try:
        with open("data.json" , "r") as file:
            return json.load(file)
    except:
        return {
            "next_id" : 1,
            "book_info" : []
        }

def save_data(data):
    with open("data.json" , "w") as file:
        json.dump(data , file)

def add_book():
    book_title = input("Enter the name of the book : ")
    book_author = input("Enter the author of the book : ")

    new_id = data['next_id']

    book = {
        "book_title" : book_title,
        "book_author" : book_author,
        "book_id" : new_id,
        "available" : True
    }

    data['book_info'].append(book)
    data['next_id'] += 1
    save_data(data)

    print(f"New book created with ID = {new_id}")

def remove_book():
    removal_id = int(input("Enter the id of the book you want to remove : "))
    found = False

    for book in data['book_info']:
        if book['book_id'] == removal_id:
            found = True
            name = book['book_title']
            data['book_info'].remove(book)
            break
    
    if found:
        save_data(data)
        print(f"Book named {name} has been deleted")
    else:
        print("Book not found")

def search_books():
    try:
        search_id = int(input("Enter the id of the book you want to search for : "))
    except:
        print("Invalid entry")
        return
    
    found = False

    for book in data["book_info"]:
        if search_id == book['book_id']:
            print(f"Book Name : {book['book_title']}")
            print(f"Author of book : {book['book_author']}")
            if book['available']:
                print("Available for borrowing")
            else:
                print("Out of stock")
            found = True
            break
    
    if not found:
        print("Book doesn't exist")

def view_all_books():
    for index , book in enumerate(data['book_info']):
        print(f"Book No {index + 1}")
        print(f"Book Name : {book['book_title']}")
        print(f"Author of book : {book['book_author']}")
        print(f"ID of the book : {book['book_id']}")
        if book['available']:
            print("Available for borrowing")
        else:
            print("Out of stock")
        
        print("-" * 30)
    
    if data['book_info'] == []:
        print("Library is empty. No books to borrow")

def borrow_book():
    found = False
    while True:
        try:
            borrow_id = int(input("Enter the id of the book you want to borrow : "))
            break
        except ValueError:
            print("Invalid input. Enter a valid number")

    for book in data['book_info']:
        if book['book_id'] == borrow_id:
            if book['available']:
                book['available'] = False
                print("Enjoy the book")
            else:
                print(f"{book['book_title']} is currently out of stock")
            found = True
            break

    if not found:
        print(f"Book with ID {borrow_id} does not exists")
    else:
        save_data(data)

def return_book():
    found = False
    while True:
        try:
            return_id = int(input("Enter the ID of the book you want to borrow"))
            break
        except ValueError:
            print("Invalid input, enter a valid nummber")
        
    for book in data['book_info']:
        if book['book_id'] == return_id:
            if book['available']:
                print("Book is not being borrowed by anyone")
            else:
                book['available'] = True
                print("Thanks for using our service!!!")
            found = True
            break
    
    if not found:
        print("Book don't belong to this library")
    else:
        save_data(data)
    
data = load_data()    

while True:
    print("Library Management System")
    print(f"""
        1. Add Books
        2. Remove Books
        3. Search books
        4. View All Books
        5. Borrow Books
        6. Return Books
        0. Exit
    """)
    while True:
        try:
            choice = int(input("Enter your choice : "))
            break
        except ValueError:
            print("Invalid input , enter a valid number")
    
    if choice == 1:
        add_book()
    elif choice == 2:
        remove_book()
    elif choice == 3:
        search_books()
    elif choice == 4:
        view_all_books()
    elif choice == 5:
        borrow_book()
    elif choice == 6:
        return_book()
    elif choice == 0:
        break
    else:
        print("Enter a valid number")

