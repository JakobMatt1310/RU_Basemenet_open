
class Tournament():

    def __init__(self, tour_name="", tour_address="", start_date="", end_date="", game_count="", teams_submitted="", game_id="", player_nr="", game_type="", leg_nr="", player_id=""):
        '''Constructor for the Tournament class'''

        self.tour_name = tour_name              # Name of the tournament
        self.tour_address = tour_address        # Address of the tournament
        self.start_date = start_date            # Starting date of the tournament
        self.end_date = end_date                # End date of the tournament
        self.game_count = game_count            # Number of games played in the tournament
        self.teams_submitted = teams_submitted  # Number of teams submitted to the tournament
        self.game_id = game_id                  # Game ID
        self.game_type = game_type              # Game type (7 games in whole), 501 1vs1 4 games, 301 2vs2 1 game, Cricket 2vs2 1 game, 501 4vs4 1 game ==== 7 games in whole
        self.leg_nr = leg_nr                    # Leg number is "round" in each game, there is always 3 legs in each game and winner is the one who wins 2 legs or best of 3
        self.player_id = player_id              # Player ID is the ID of the player in the tournament

    
    def __str__(self):
        '''Returns a string representation of the tournament object'''

        return f"Tournament name: {self.tour_name:>5}, Address: {self.tour_address:>5}, Starting date: {self.start_date:>5}, End_date: {self.end_date:>5}, Number of games played: {self.game_count:>5}, Number of teams submitted to tournament: {self.teams_submitted:>5}, Game ID: {self.game_id:>5}, Player number: {self.player_nr:>5}, Game type: {self.game_type:>5}, Leg number: {self.leg_nr:>5}, Player ID: {self.player_id:>5}"