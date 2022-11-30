from data_layer.data_wrapper import Data_Wrapper
from logic_layer.player_logic import Player_Logic
from logic_layer.association_logic import Association_Logic
from logic_layer.statistic_logic import Statistic_Logic 

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.association_logic = Association_Logic(self.data_wrapper)
        self.statistic_logic = Statistic_Logic()

#------------------Player_Logic------------------------------------#
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def validate_player_entry(self):
        return self.player_logic.validate_player_entry()

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
        pass

    def validate_association_entry(self):
        pass
    
    def update_association(self):
        pass

    def view_association(self):
        pass

    def delete_association(self):
        pass

    def get_all_associations(self):
        pass

    def get_association(self):
        pass
    
    def edit_association(self):
        pass

#------------------statistic_Logic------------------------------------#
    def get_win_percentage(self):
        pass

    def get_quality_points(self):
        pass

    def get_games_played(self):
        pass

    def view_stats_for_everything(self):
        pass

    def view_player_stats():
        pass

    def view_team_stats():
        pass

#------------------Team_Logic------------------------------------#
    def __init__(self):
        pass

    def validate_team_entry(self):
        pass
    
    def get_all_teams(self):
        pass

    def get_team_stats(self):
        pass

    def get_team(self):
        pass

    def update_team(self):
        pass

    def create_team(self):
        pass
    
    def edit_team(self):
        pass

    def view_team(self):
        pass

    def view_team_players(self):
        pass

    def delete_team(self):
        pass

#------------------Tournament_Logic------------------------------------#
    def update_tournament(self):
        pass

    def validate_tournament_entry(self):
        pass

    def delete_tournament(self):
        pass

    def get_all_tournaments(self):
        pass

    def get_tournament(self):
        pass
    
    def create_tournament(self):
        pass