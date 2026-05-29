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


data = load_data()    
add_book()
remove_book()