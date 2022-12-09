from data.player_data import Player_Data
from data.tournaments_data import Tournaments_Data
from data.associations_data import Associations_Data
from data.teams_data import Teams_Data
# from data.rounds_data import Rounds_Data
from data.moderator_data import Mod_password
from data.match_data import Match_Data
from data.teams_in_tourneys_data import Teams_In_Tourneys_Data

class Data_Wrapper():
    def __init__(self):
        '''Constructor for the Data_Wrapper class'''
        self.player_data = Player_Data()
        self.tournament_data = Tournaments_Data()
        self.association_data = Associations_Data()
        self.team_data = Teams_Data()
        # self.rounds_data = Rounds_Data()
        self.mod_password_data = Mod_password()
        self.match_data = Match_Data
        self.teams_in_tourneys_data = Teams_In_Tourneys_Data()


#------------------Get---------------------------------------------#

    def get_moderator_password(self):
        return self.mod_password_data.read_password()

    def get_all_players(self):
        '''Gets all players'''
        return self.player_data.read_all_players()

    def get_all_tournaments(self):
        '''Gets all tournaments'''
        return self.tournament_data.read_all_tournaments()

    def get_all_associations(self):
        '''Gets all associations'''
        return self.association_data.read_all_associations()

    def get_all_teams(self):
        '''Gets all teams'''
        return self.team_data.read_all_teams()
    
    def get_all_matches(self):
        return self.match_data.read_all_matches()
    
    def get_all_teams_in_tourneys(self):
        return self.teams_in_tourneys_data.read_all_teams_in_tourneys()


#------------------Create------------------------------------------#
    def create_player(self, player):
        '''Creates a new player'''
        return self.player_data.create_player(player)

    def create_tournament(self, tournament):
        '''Creates a new tournament'''
        return self.tournament_data.create_tournament(tournament)

    def create_association(self,association):
        '''Creates a new association'''
        return self.association_data.create_association(association)

    def create_team(self, team):
        '''Creates a new team'''
        return self.team_data.create_team(team)
    
    def create_match(self, match):
        return self.match_data.create_match(match)

    def add_team_to_tournament(self, tournament_name, team_id):
        '''Creates a connection between a team and a tournament essentially adding the team to a tournament'''
        return self.teams_in_tourneys_data.create_team_in_tourney(tournament_name, team_id)


#------------------Update------------------------------------------#
    def update_team_captain(self, team_to_edit):
        '''Updates team captain'''
        #Team to edit er með nýjan captain
        return self.team_data.update_team_captain(team_to_edit)

    def update_team_name(self, team_to_edit):
        '''Updates team name'''
        #Team to edit er með breytt nafn
        return self.team_data.update_team_name(team_to_edit)
    
    def update_team_association(self, team_to_edit):
        '''Updates team association'''
        #Team to edit er með breytt association nafn og association id
        return self.team_data.update_team_association(team_to_edit)
    
    def edit_player(self, player):
        '''Edit player'''
        return self.player_data.update_player_name(player)
    
    def update_rounds(self, rounds):
        '''Updates rounds'''
        return self.update_rounds(rounds)
    
    def update_password(self, password):
        '''Updates password'''
        return self.mod_password_data.update_password(password)
    
    def update_match(self, match):
        return self.match_data.update_match(match)
        
    def update_association_name(self, association_to_update):
        return self.association_data.update_association_name(association_to_update)
    
    def update_association_phone(self, association_to_update):
        return self.association_data.update_association_phone(association_to_update)

    def update_association_address(self, association_to_update):
        return self.association_data.update_association_address(association_to_update)







# #------------------Main--------------------------------------------#
# def main_data():
#     '''Main function for the data wrapper in data layer'''
#     data_class_user = User_Data()
#     res_user = data_class_user.read_all_users()

#     data_class_player = Player_Data()
#     res_player = data_class_player.read_all_players()

#     data_class_tournament = Tournaments_Data()
#     res_tournament = data_class_tournament.read_all_tournaments()

#     data_class_association = Associations_Data()
#     res_association = data_class_association.read_all_associations()

#     data_class_teams = Teams_Data()
#     res_teams = data_class_teams.read_all_teams()

#     data_class_rounds = Rounds_Data()
#     res_rounds = data_class_rounds.read_all_rounds()
    
# if main_data() == '__main__':
#     main_data()
