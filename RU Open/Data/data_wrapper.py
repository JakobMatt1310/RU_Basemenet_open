# from data.user_data import User_Data
from data.player_data import Player_Data
from data.teams_data import Teams_Data
# from data.tournaments_data import Tournaments_Data
# from data.associations_data import Associations_Data
# from data.teams_data import Teams_Data

class Data_Wrapper():

    def __init__(self):
        '''Constructor for the Data_Wrapper class'''

        # self.user_data = User_Data()
        self.player_data = Player_Data()
        self.team_data = Teams_Data()
        # self.tournament_data = Tournaments_Data()
        # self.association_data = Associations_Data()
        # self.team_data = Teams_Data()

#------------------Get---------------------------------------------#
    # def get_all_users(self):
    #     '''Gets all users'''
    #     print(self.user_data.read_all_users())
    #     return self.user_data.read_all_users()

    def get_all_players(self):
        '''Gets all players'''
        return self.player_data.read_all_players()

    # def get_all_tournaments(self):
    #     '''Gets all tournaments'''
    #     print(self.tournament_data.read_all_tournaments())
    #     return self.tournament_data.read_all_tournaments()

    # def get_all_associations(self):
    #     '''Gets all associations'''
    #     print(self.association_data.read_all_associations())
    #     return self.association_data.read_all_associations()

    # def get_all_teams(self):
    #     '''Gets all teams'''
    #     print(self.team_data.read_all_teams())
    #     return self.team_data.read_all_teams()

#------------------Create------------------------------------------#
    # def create_user(self, user):
    #     '''Creates a new user'''
    #     print(self.user_data.create_user(user))
    #     return self.user_data.create_user(user)

    def create_player(self, player):
        '''Creates a new player'''
        return self.player_data.create_player(player)

    # def create_tournament(self, tournament):
    #     '''Creates a new tournament'''
    #     print(self.tournament_data.create_tournament(tournament))
    #     return self.tournament_data.create_tournament(tournament)

    # def create_association(self,association):
    #     '''Creates a new association'''
    #     print(self.association_data.create_association(association))
    #     return self.association_data.create_association(association)

    def create_team(self, team):
        '''Creates a new team'''
        return self.team_data.create_team(team)


#------------------Main--------------------------------------------#
def main_data():
    '''Main function for the data wrapper in data layer'''
    # data_class_user = User_Data()
    # res_user = data_class_user.read_all_users()
    # for us in res_user:
    #     print(us)

    data_class_player = Player_Data()
    res_player = data_class_player.read_all_players()
    for py in res_player:
        print(py)

    # data_class_tournament = Tournaments_Data()
    # res_tournament = data_class_tournament.read_all_tournaments()
    # for tur in res_tournament:
    #     print(tur)

    # data_class_association = Associations_Data()
    # res_association = data_class_association.read_all_associations()
    # for ass in res_association:
    #     print(ass)

    # data_class_teams = Teams_Data()
    # res_teams = data_class_teams.read_all_teams()
    # for tea in res_teams:
    #     print(tea)


if main_data() == '__main__':
    main_data()