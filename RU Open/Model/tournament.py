
class Tournament():

    def __init__(self, tournament_name="", tournament_address=""):
        '''Constructor for the Tournament class'''

        self.tournament_name = tournament_name
        self.tournament_address = tournament_address

    
    def __str__(self):
        '''Returns a string representation of the tournament object'''

        return f"Name: {self.tournament_name:>5}, Address: {self.tournament_address:>5}"