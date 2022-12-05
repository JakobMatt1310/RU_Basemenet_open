
class Player():

    def __init__(self, player_name="", player_ssn="", player_phone="", player_email="", player_address=""):
        '''Constructor for the Player class'''

        self.player_name = player_name
        self.player_ssn = player_ssn
        self.player_phone = player_phone
        self.player_email = player_email
        self.player_address = player_address

    
    def __str__(self):
        '''Returns a string representation of the Player object'''

        return f"Name: {self.player_name:>5}, SSN: {self.player_ssn:>5}, Phone: {self.player_phone:>5}, Email: {self.player_email:>5}, Address: {self.player_address:>5}"