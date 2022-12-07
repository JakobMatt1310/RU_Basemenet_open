class Tournament():
<<<<<<< HEAD
    def __init__(self, tournament_name="", tournament_address="", organizer="", organizer_number="", start_date="", end_date=""):
=======
    def __init__(self, 
                 tournament_name="", 
                 tournament_address="", 
                 start_date="", 
                 end_date="", 
                 game_count="", 
                 teams_submitted="", 
                 game_id="", 
                 game_type="", 
                 leg_nr="", 
                 player_id=""):
>>>>>>> 0ef3cd102ce705ac7b3a713a4f47af662d3beab7
        '''Constructor for the Tournament class'''
        self.tournament_name = tournament_name          # Name of the tournament
        self.tournament_address = tournament_address    # Address of the tournament
        self.organizer = organizer
        self.organizer_number = organizer_number
        self.start_date = start_date                    # Starting date of the tournament
        self.end_date = end_date                        # End date of the tournament

    def function(self):
        print(f"{self.tournament_name}, {self.tournament_address}, {self.organizer}, {self.organizer_number}, {self.start_date}, {self.end_date}")
    def __str__(self):
        '''Returns a string representation of the tournament object'''
        return f"Tournament name: {self.tournament_name:>5}, Address: {self.tournament_address:>5}, Starting date: {self.start_date:>5}, End_date: {self.end_date:>5}, Number of games played: {self.game_count:>5}, Number of teams submitted to tournament: {self.teams_submitted:>5}, Game ID: {self.game_id:>5}, Game type: {self.game_type:>5}, Leg number: {self.leg_nr:>5}, Player ID: {self.player_id:>5}"
