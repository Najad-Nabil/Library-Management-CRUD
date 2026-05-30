import json

class Car:

    def __init__(self, model, year, color, is_driving):
        self.model = model
        self.year = year
        self.color = color
        self.is_driving = is_driving


    def to_dict(self):
        return {
            "model" : self.model,
            "year" : self.year,
            "color" : self.color,
            "is_driving" : self.is_driving
        }

    def drive(self):
        print(f"You are driving a {self.model}")
        self.is_driving = True
        self.save_data()

    def stop(self):
        self.is_driving = False
        self.save_data()
        print(f"You have stopped the {self.model}")

    def save_data(self):
        with open("car-data.json" , "w") as file:
            json.dump(self.to_dict() , file)



car1 = Car('bmw' , 2024 , 'red' , False)
car1.stop()
