class Member:

    def __init__(self , member_name , member_id):
        self.member_name = member_name
        self.member_id = member_id

    def to_dict(self):
        return {
            "member_name" : self.member_name,
            "member_id" : self.member_id
        }
    
    @classmethod
    def from_dict(cls , data):
        member = cls(
            data["member_name"],
            data["member_id"]
        )

        return member
    

