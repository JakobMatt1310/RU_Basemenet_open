

class Team_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_team(self, team):
        teams = self.data_wrapper.create_team(self, team)
        team_input = team
        if team_input in teams:
            return ValueError
        else:
            self.data_wrapper.create_team(self, team)
            return True

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
            if team_to_edit == team.name:
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
        
    def teams_in_tourney(self, team, tournament):
        """Gets all the teams that are registered to the tournament"""
        teams_tourney = self.data_wrapper.get_all_teams_in_tourneys()
        teams_id = []
        for tourney in teams_tourney:
            if tournament.name == tourney.tournament_name:
                teams_id.append(tourney.team_id)
        ret_list = self.get_teams_by_id(teams_id)
        return ret_list
    
    def teams_not_in_tourney(self, tournament):
        """Gets all teams that are not registered to the tournament"""
        teams_tourney = self.data_wrapper.get_all_teams_in_tourneys()
        teams_id = []
        for tourney in teams_tourney:
            if tournament.name == tourney.tournament_name:
                teams_id.append(tourney.team_id)
        ret_list = self.get_teams_not_in_id_list(teams_id)
        return ret_list
        
        

    def get_teams_by_name(self, team_to_add):
        all_teams = self.get_all_teams()
        teams_list = []
        for team in all_teams:
            if team_to_add == team.team_name:
                teams_list.append(team)
        return teams_list
    
    def get_teams_by_id(self, team_ids: list):
        """Gets allt teams in id_list"""
        all_teams = self.get_all_teams()
        teams_list = []
        for team in all_teams:
            for id in team_ids:
                if id == team.id:
                    teams_list.append(team)
                    break
        return teams_list
    
    def get_teams_not_in_id_list(self, team_ids: list):
        """Gets all teams that are not on the id list"""
        all_teams = self.get_all_teams()
        teams_list = []
        for team in all_teams:
            team_found = False
            if len(team_ids) == 0:
                teams_list.append(team)
            else:
                for id in team_ids:
                    if id == team.id:
                        team_found = True
                        break
                        
                if team_found == False:
                    teams_list.append(team)
        return teams_list
   