class Player():
    def __init__(self,id="", name="", ssn="", phone="", email="", address="", team_id=""):
        '''Constructor for the Player class'''
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.address = address
        self.team_id = team_id
        self.id = id
    
    def __str__(self):
        '''Returns a string representation of the Player object'''
        return f"ID: {self.id:>5}, Name: {self.name:>5}, SSN: {self.ssn:>5}, Phone: {self.phone:>5}, Email: {self.email:>5}, Address: {self.address:>5}, Team ID: {self.team_id:>5}"
