
class Team:

    def __init__(self, id="", association_id="", team_name="", association_name="", captain_name=""):
        self.id = id
        self.association_id = association_id
        self.team_name = team_name
        self.association_name = association_name
        self.captain_name = captain_name

    def __str__(self):
        '''Returns a string representation of the Team object'''
        # team_str = ""
        # team_str = "".join(i for i in self.team_players[:])
        # for player in self.team_players[:]:
        #     return_team_list += f'{str(player)}'

        return f"Team: {self.team_name:>5}, Association: {self.team_association_name:>5}, Captain: {self.team_captain_name:>5}, Team members: {team_str:>5}"