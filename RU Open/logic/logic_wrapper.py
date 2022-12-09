from logic.association_logic import Association_Logic
from logic.player_logic import Player_Logic 
from logic.team_logic import Team_Logic
from logic.round_logic import Round_Logic
# from logic.statistic_logic import Statistic_Logic
from logic.tournament_logic import Tournament_Logic
from data.data_wrapper import Data_Wrapper
from logic.mod_pass_logic import Mod_Pass_Logic
from logic.match_logic import Match_logic

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.association_logic = Association_Logic(self.data_wrapper)
        # self.statistic_logic = Statistic_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.tournament_logic = Tournament_Logic(self.data_wrapper)
        self.mod_pass_logic = Mod_Pass_Logic(self.data_wrapper)
        self.match_logic = Match_logic(self.data_wrapper)
        self.round_logic = Round_Logic(self.data_wrapper)
        
#------------------mod_pass_Logic----------------------------------#
    def get_moderator_password(self):
        return self.mod_pass_logic.get_moderator_password()    
    
    def update_password(self, password):
        return self.mod_pass_logic.update_password(password)    

#------------------match_Logic-------------------------------------#
    def create_match(self, match):
        return self.match_logic.create_match(match)    
    
    def update_match(self, password):
        return self.match_logic.update_match(password)    
    
    def get_all_matches(self):
        return self.match_logic.get_all_matches()

#------------------Player_Logic------------------------------------#
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def edit_player(self, player):
        return self.player_logic.edit_player(player)

    def check_if_player_exists(self, ssn):
        return self.player_logic.check_if_player_exists(ssn)

    def view_player(self):
        return self.player_logic.view_player()

    def view_player_stats(self):
        return self.player_logic.view_player_stats()
    
    def get_player_by_name(self, name):
        return self.player_logic.get_player_by_name(name)
    
    def delete_player(self):
        return self.player_logic.delete_player()
    
    def all_captains(self, ssn):
        return self.player_logic.all_captains(ssn)

    def get_all_players_of_team(self, team):
        return self.player_logic.get_all_players_of_team(team)
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
        return self.association_logic.get_all_associations()
    
    def validate_association_name_with_all(self, name):
        return self.association_logic.validate_association_name_with_all(name)

    def get_association(self, association_to_edit):
        return self.association_logic.get_association(association_to_edit)
    
    def edit_association(self):
        return self.association_logic.edit_association()
    
    def update_association_name(self, association_to_edit):
        return self.association_logic.update_association_name(association_to_edit)

    def update_association_phone(self, association_to_edit):
        return self.association_logic.update_association_phone(association_to_edit)

    def update_association_address(self, association_to_edit):
        return self.association_logic.update_association_address(association_to_edit)

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
    
    def get_team_by_id(self, team_id):
        return self.team_logic.get_team_by_id(team_id)

    def get_team(self, team_to_edit):
        return self.team_logic.get_team(team_to_edit)

    def update_team_captain(self, team_to_edit):
        return self.team_logic.update_team_captain(team_to_edit)
    
    def update_team_name(self, team_to_edit):
        return self.team_logic.update_team_name(team_to_edit)
    
    def update_team_association(self, team_to_edit):
        return self.team_logic.update_team_association(team_to_edit)
    
    def view_team(self):
        return self.team_logic.view_team()

    def get_team_players(self):
        return self.team_logic.get_team_players()
    
    def teams_in_association(self):
        return self.team_logic.teams_in_association()

    def delete_team(self):
        return self.team_logic.delete_team()
    
    def teams_in_tourney(self, tournament):
        return self.team_logic.teams_in_tourney(tournament)
    
    def teams_not_in_tourney(self, tournament):
        return self.team_logic.teams_not_in_tourney(tournament)

#------------------Tournament_Logic------------------------------------#
    def create_tournament(self, tournament):
        return self.tournament_logic.create_tournament(tournament)

    def update_tournament(self):
        return self.tournament_logic.update_tournament()

    def delete_tournament(self):
        return self.tournament_logic.delete_tournament()

    def get_all_tournaments(self):
        return self.tournament_logic.get_all_tournaments()

    def get_tournament(self, tournament):
        return self.tournament_logic.get_tournament(tournament)
    
    def create_player(self, player):
        return self.player_logic.create_player(player)

    def team_id_for_player(self):
        return self.player_logic.team_id_for_player()

    def get_all_players(self):
        return self.player_logic.get_all_players()

    def add_team_to_tourney(self, tournament_name, team_id):
        return self.tournament_logic.add_team_to_tourney(tournament_name, team_id)

#------------------------Round Logic------------------------------------#

    def create_round(self, round):
        return self.round_logic.create_round(round)
