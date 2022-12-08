class Tournament():
    def __init__(self, id="", tournament_name="", tournament_address="", start_date="", end_date="", organizer="", organizer_number=""):
        '''Constructor for the Tournament class'''
        self.id = id
        self.tournament_name = tournament_name          # Name of the tournament
        self.tournament_address = tournament_address    # Address of the tournament
        self.start_date = start_date                    # Starting date of the tournament
        self.end_date = end_date                        # End date of the tournament
        self.organizer = organizer
        self.organizer_number = organizer_number

    def __str__(self):
        '''Returns a string representation of the tournament object'''
        return f"Tournament ID: {self.id}, Tournament name: {self.tournament_name:>5}, Address: {self.tournament_address:>5}, Starting date: {self.start_date:>5}, End date: {self.end_date:>5}, Organizer: {self.organizer:>5}, Organizer number: {self.organizer_number:>5}"
