from data.teams_data import Teams_Data
from model.team import Team

class Team_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_team(self, team):
        self.data_wrapper.create_team(team)

    def validate_team_entry(self):
        return self.data_wrapper.validate_team_entry()
    
    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()
    
    def teams_in_association(self):
        all_teams = self.get_all_teams()
        ret_dict = {}
        for element in all_teams:
            if element.association_id not in ret_dict:
                ret_dict[element.association_id] = 1
            else:
                ret_dict[element.association_id] += 1
        return ret_dict

    def get_team_stats(self):
        return self.data_wrapper.get_team_stast()

    def get_team(self, team_to_edit):
        all_teams = self.get_all_teams()
        for team in all_teams:
            if team_to_edit == team.team_name:
                return team
        return None

    def update_team_captain(self, team_to_edit):
        return self.data_wrapper.update_team_captain(team_to_edit)
    
    def update_team_name(self, team_to_edit):
        return self.data_wrapper.update_team_name(team_to_edit)
    
    def update_team_association(self, team_to_edit):
        return self.data_wrapper.update_team_association(team_to_edit)

    def view_team(self):
        return self.data_wrapper.view_team()

    def get_team_players(self):
        return self.data_wrapper.get_team_players()

    def delete_team(self):
        self.data_wrapper.delete_team()