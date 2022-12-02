class Player:
    player_counter = 1
    def __init__(self, name="", ssn="", phone="", email="", address="", team_id=""):
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.address = address
        self.team_id = team_id
        self.player_id = self.player_counter
        Player.player_counter += 1


    
    def __str__(self):
        return "Name:{:>5}, SSN:{:>5}, Phone:{:>5}, Email: {:>5}, Address:{:>5}".format(self.name, self.ssn, self.phone, self.email, self.address)