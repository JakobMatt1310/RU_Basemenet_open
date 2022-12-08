class Tournament():
    def __init__(self, id="", name="", address="", start_date="", end_date="", organizer="", organizer_nr=""):
        '''Constructor for the Tournament class'''
        self.id = id
        self.name = name
        self.address = address
        self.start_date = start_date
        self.end_date = end_date
        self.organizer = organizer
        self.organizer_nr = organizer_nr

    def __str__(self):
        '''Returns a string representation of the tournament object'''
        return f"Tournament ID: {self.id}, Tournament name: {self.name:>5}, Address: {self.address:>5}, Starting date: {self.start_date:>5}, End date: {self.end_date:>5}, Organizer: {self.organizer:>5}, Organizer number: {self.organizer_nr:>5}"
