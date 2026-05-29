import json

def load_data():
    try:
        with open("data.json" , "r") as file:
            return json.load(file)
    except:
        return {
            "book_id" : 0,
            "book_info" : []
        }

def save_data(data):
    with open("data.json" , "w") as file:
        json.dump(data , file)
