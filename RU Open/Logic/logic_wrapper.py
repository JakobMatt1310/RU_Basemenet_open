from logic.association_logic import Association_Logic
from logic.player_logic import Player_Logic 
from logic.team_logic import Team_Logic
# from logic.statistic_logic import Statistic_Logic
from logic.tournament_logic import Tournament_Logic
from data.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.association_logic = Association_Logic(self.data_wrapper)
        # self.statistic_logic = Statistic_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.tournament_logic = Tournament_Logic(self.data_wrapper)

#------------------Player_Logic------------------------------------#
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def edit_player(self):
        return self.player_logic.edit_player()

    def assign_captain(self):
        return self.player_logic.assign_captain()

    def view_player(self):
        return self.player_logic.view_player()

    def view_player_stats(self):
        return self.player_logic.view_player_stats()
    
    def delete_player(self):
        return self.player_logic.delete_player()

#------------------Association_Logic------------------------------------#
    def create_association(self, association):
        return self.association_logic.create_association(association)
    
    def update_association(self):
        return self.association_logic.update_association()

    def view_association(self):
        return self.association_logic.view_association()

    def delete_association(self):
        return self.association_logic.delete_association()

    def get_all_associations(self):
        return self.association_logic.get_all_associations(self)

    def get_association(self):
        return self.association_logic.get_association()
    
    def edit_association(self):
        return self.association_logic.edit_association()
    

#------------------statistic_Logic------------------------------------#
    # def get_win_percentage(self):
    #     return self.statistic_logic.get_win_percentage()

    # def get_quality_points(self):
    #     return self.statistic_logic.get_quality_points()

    # def get_games_played(self):
    #     return self.statistic_logic.get_games_played()

    # def view_stats_for_everything(self):
    #     return self.statistic_logic.view_stats_for_everything()

    # def view_player_stats(self):
    #     return self.statistic_logic.view_player_stats()

    # def view_team_stats(self):
    #     return self.statistic_logic.view_team_stats()

#------------------Team_Logic-------------------------------------
    def create_team(self, team):
        return self.team_logic.create_team(team)
    
    def get_all_teams(self):
        return self.team_logic.get_all_teams()

    def get_team_stats(self):
        return self.team_logic.get_team_stats()

    def get_team(self):
        return self.team_logic.get_team()

    def update_team(self):
        return self.team_logic.update_team()
    
    def edit_team(self):
        return self.team_logic.edit_team()

    def view_team(self):
        return self.team_logic.view_team()

    def get_team_players(self):
        return self.team_logic.get_team_players()
    
    def teams_in_association(self):
        return self.team_logic.teams_in_association()

    def delete_team(self):
        return self.team_logic.delete_team()

#------------------Tournament_Logic------------------------------------#
    def create_tournament(self, tournament):
        return self.tournament_logic.create_tournament(tournament)

    def update_tournament(self):
        return self.tournament_logic.update_tournament()

    def delete_tournament(self):
        return self.tournament_logic.delete_tournament()

    def get_all_tournaments(self):
        return self.tournament_logic.get_all_tournaments()

    def get_tournament(self):
        return self.tournament_logic.get_tournament()
    
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def team_id_for_player(self):
        return self.player_logic.team_id_for_player()

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def create_team(self, team):
        return self.team_logic.create_team(team)