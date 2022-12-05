
class Tournament():

    def __init__(self, tour_name="", tour_address="", start_date="", end_date="", game_count="", teams_submitted=""):
        '''Constructor for the Tournament class'''

        self.tour_name = tour_name
        self.tour_address = tour_address
        self.start_date = start_date
        self.end_date = end_date
        self.game_count = game_count
        self.teams_submitted = teams_submitted
    
    def __str__(self):
        '''Returns a string representation of the tournament object'''

        return f"Tournament name: {self.tour_name:>5}, Address: {self.tour_address:>5}, Starting date: {self.start_date:>5}, End_date: {self.end_date:>5}, Number of games played: {self.game_count:>5}, Number of teams submitted to tournament: {self.teams_submitted:>5}"