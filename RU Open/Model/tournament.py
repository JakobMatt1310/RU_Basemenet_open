
class Tournament():

    def __init__(self, tour_name="", tour_address="", start_date="", end_date="", game_count="", teams_submitted="", game_id="", player_nr="", game_type="", leg_nr=""):
        '''Constructor for the Tournament class'''

        self.tour_name = tour_name
        self.tour_address = tour_address
        self.start_date = start_date
        self.end_date = end_date
        self.game_count = game_count
        self.teams_submitted = teams_submitted
        self.game_id = game_id
        self.player_nr = player_nr
        self.game_type = game_type
        self.leg_nr = leg_nr


    def __str__(self):
        '''Returns a string representation of the tournament object'''

        return f"Tournament name: {self.tour_name:>5}, Address: {self.tour_address:>5}, Starting date: {self.start_date:>5}, End_date: {self.end_date:>5}, Number of games played: {self.game_count:>5}, Number of teams submitted to tournament: {self.teams_submitted:>5}, Game ID: {self.game_id:>5}, Player number: {self.player_nr:>5}, Game type: {self.game_type:>5}, Leg number: {self.leg_nr:>5}"