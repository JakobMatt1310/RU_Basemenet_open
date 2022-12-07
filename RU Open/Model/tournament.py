class Tournament():
    def __init__(self, tournament_name="", tournament_address="", organizer="", organizer_number="", start_date="", end_date=""):
        '''Constructor for the Tournament class'''
        self.tournament_name = tournament_name          # Name of the tournament
        self.tournament_address = tournament_address    # Address of the tournament
        self.organizer = organizer
        self.organizer_number = organizer_number
        self.start_date = start_date                    # Starting date of the tournament
        self.end_date = end_date                        # End date of the tournament

    def function(self):
        print(f"{self.tournament_name}, {self.tournament_address}, {self.organizer}, {self.organizer_number}, {self.start_date}, {self.end_date}")
