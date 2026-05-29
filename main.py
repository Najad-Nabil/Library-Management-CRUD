import json

def load_data():
    try:
        with open("data.json" , "r") as file:
            return json.load(file)
    except:
        return {
            "next_id" : 0,
            "book_info" : []
        }

def save_data(data):
    with open("data.json" , "w") as file:
        json.dump(data , file)

def add_book():
    book_title = input("Enter the name of the book : ")
    book_author = input("Enter the author of the book : ")

    data['next_id'] += 1
    new_id = data['next_id']

    book = {
        "book_title" : book_title,
        "book_author" : book_author,
        "book_id" : new_id,
        "available" : True
    }

    data['book_info'].append(book)
    save_data(data)

    print(f"New book created with ID = {new_id}")




data = load_data()    
add_book()