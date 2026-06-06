class Member:

    def __init__(self , member_name , member_id):
        self.member_name = member_name
        self.member_id = member_id
        self.borrowed_books = []

    def to_dict(self):
        return {
            "member_name" : self.member_name,
            "member_id" : self.member_id,
            "borrowed_books" : self.borrowed_books
        }
    
    @classmethod
    def from_dict(cls , data):
        member = cls(
            data["member_name"],
            data["member_id"]
        )
        member.borrowed_books = data["borrowed_books"]

        return member
    
    def __str__(self):
        return f"Name : {self.member_name}\nID : {self.member_id}"
    

