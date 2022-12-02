class Team:
    team_counter = 1
    def __init__(self, team_name="", association_name="", captain_name=""):
        self.id = self.team_counter
        self.team_name = team_name
        self.association_name = association_name
        self.captain_name = captain_name
        self.team_counter += 1