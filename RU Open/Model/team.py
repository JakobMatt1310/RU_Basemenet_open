
class Team:

    def __init__(self, id="",team_name="", association_name="", association_id="", captain_name=""):
        '''Constructor for the Team class'''

        self.id = id
        self.team_name = team_name
        self.association_name = association_name
        self.association_id = association_id
        self.captain_name = captain_name


    def __str__(self):
        '''Returns a string representation of the Team object'''

        return f"ID: {self.id:>5}, Team: {self.team_name:>5}, Association: {self.association_name:>5}, Association ID: {self.association_id:>5}, Captain: {self.captain_name:>5}"