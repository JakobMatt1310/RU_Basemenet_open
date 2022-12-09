
class Teams_In_Tourneys():
    def __init__(self, tournament_name, team_id):
        '''Constructor for the teams in tournaments class'''
        self.tournament_name = tournament_name
        self.team_id = team_id

    def __str__(self):
        '''Returns a string representation of the teams in tournaments object'''
        return f"Tournament name: {self.tournament_name:>5}, Team ID: {self.team_id:>5}"