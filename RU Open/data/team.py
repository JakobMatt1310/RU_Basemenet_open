
class Team():

    def __init__(self, team_name=str, team_association_name=str, team_captain_name=str, team_players=list):
        '''Constructor for the Team class'''

        self.team_name = team_name
        self.team_association_name = team_association_name
        self.team_captain_name = team_captain_name
        self.team_players = team_players

    def __str__(self):
        '''Returns a string representation of the Team object'''
        # team_str = ""
        team_str = "".join(i for i in self.team_players[:])
        # for player in self.team_players[:]:
        #     return_team_list += f'{str(player)}'

        return f"Team: {self.team_name:>5}, Association: {self.team_association_name:>5}, Captain: {self.team_captain_name:>5}, Team members: {team_str:>5}"