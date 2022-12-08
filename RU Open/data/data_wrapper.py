from data.user_data import User_Data
from data.player_data import Player_Data
from data.tournaments_data import Tournaments_Data
from data.associations_data import Associations_Data
from data.teams_data import Teams_Data
from data.moderator_data import Mod_password

class Data_Wrapper():
    def __init__(self):
        '''Constructor for the Data_Wrapper class'''
        self.user_data = User_Data()
        self.player_data = Player_Data()
        self.tournament_data = Tournaments_Data()
        self.association_data = Associations_Data()
        self.team_data = Teams_Data()
        self.mod_password = Mod_password()
        

#------------------Get---------------------------------------------#

    def get_moderator_password(self):
        return self.mod_password.read_password()

    def get_all_users(self):
        '''Gets all users'''
        return self.user_data.read_all_users()

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

#------------------Create------------------------------------------#
    def create_user(self, user):
        '''Creates a new user'''
        return self.user_data.create_user(user)

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

#------------------Update------------------------------------------#
    def update_team_captain(self, team_to_edit):
        '''Updates team captain'''
        #Team to edit er með nýjan captain
        return self.team_data.update_team_captain(team_to_edit)

    def update_team_name(self, team_to_edit):
        #Team to edit er með breytt nafn
        return self.team_data.update_team_name(team_to_edit)
    
    def update_team_association(self, team_to_edit):
        #Team to edit er með breytt association nafn og association id
        return self.team_data.update_team_association(team_to_edit)
    
    def edit_player(self, player):
        return self.player_data.update_player_name(player)
    
    def update_password(self, password):
        return self.mod_password.update_password(password)










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


# if main_data() == '__main__':
#     main_data()
