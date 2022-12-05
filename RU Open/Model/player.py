class Player:

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

        return "Name:{:>5}, SSN:{:>5}, Phone:{:>5}, Email: {:>5}, Address:{:>5}".format(self.name, self.ssn, self.phone, self.email, self.address)