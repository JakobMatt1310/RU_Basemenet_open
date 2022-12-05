
class Team:

    def __init__(self, id="", association_id="", team_name="", association_name="", captain_name=""):
        '''Constructor for the Team class'''

        self.id = id
        self.association_id = association_id
        self.team_name = team_name
        self.association_name = association_name
        self.captain_name = captain_name


    def __str__(self):
        '''Returns a string representation of the Team object'''

        return f"Team: {self.team_name:>5}, Association: {self.association_name:>5}, Captain: {self.captain_name:>5}"