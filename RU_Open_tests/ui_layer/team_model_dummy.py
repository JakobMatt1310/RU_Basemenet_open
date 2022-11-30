class Team:
    def __init__(self, team_name="", association_name="", captain_name="", team_players=None):
        if team_players == None:
            team_players = []
        self.team_name = team_name
        self.association_name = association_name
        self.captain_name = captain_name
        self.team_players = team_players
        