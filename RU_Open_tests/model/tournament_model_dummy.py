class Tournament:
    def __init__(self, tournament_name, competing_teams=None):
        if competing_teams == None:
            competing_teams = []
        self.tournament_name = tournament_name
        self.competing_teams = competing_teams