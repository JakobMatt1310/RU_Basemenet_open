from data_layer.teams_data import Team_Data
from model.team import Team

class Team_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_team(self, team):
        self.data_wrapper.create_team(team)

    def get_all_teams(self, teams):
        return self.data_wrapper .get_all_teams()
        
    def get_team_stats(self):
        return self.data_wrapper.get_team_stast()

    def get_team(self):
        return self.data_wrapper.get_team()

    def update_team(self):
        self.data_wrapper.update_team()
    
    def edit_team(self):
        self.data_wrapper.edit_team()

    def view_team(self):
        return self.data_wrapper.view_team()

    def view_team_players(self):
        return self.data_wrapper.view_team_players()

    def delete_team(self):
            self.data_wrapper.delete_team()