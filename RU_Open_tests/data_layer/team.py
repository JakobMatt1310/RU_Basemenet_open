
class Team():

    def __init__(self, team_name, team_association_name, team_captain_name, team_players):
        '''Constructor for the Team class'''

        self.team_name = team_name
        self.team_association_name = team_association_name
        self.team_captain_name = team_captain_name
        self.team_players = team_players

    
    def __str__(self):
        '''Returns a string representation of the Team object'''

        return f"Team name: {self.team_name:>5}, association name: {self.team_association_name:>5}, Captain name: {self.team_captain_name:>5}, players in team: {self.team_players:>5}"