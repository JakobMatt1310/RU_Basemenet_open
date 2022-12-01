from user_data import User_Data
from player_data import Player_Data
from tournaments_data import Tournaments_Data
from associations_data import Associations_Data
from teams_data import Teams_Data

class Data_Wrapper():

    def __init__(self):
        '''Constructor for the Data_Wrapper class'''

        self.user_data = User_Data()
        self.player_data = Player_Data()
        self.tournament_data = Tournaments_Data()
        self.association_data = Associations_Data()
        self.team_data = Teams_Data()

#------------------Get---------------------------------------------#
    def get_all_users(self):
        '''Gets all users'''
        data_class_user = User_Data()
        result = data_class_user.read_all_users()

        for elem in result:
            print(elem)

        print(self.user_data.read_all_users())
        res = self.user_data.read_all_users()

        return self.user_data.read_all_users()

    def get_all_players(self):
        '''Gets all players'''
        data_class_player = Player_Data()
        result = data_class_player.read_all_players()

        for elem in result:
            print(elem)

        print(self.player_data.read_all_players())
        res = self.player_data.read_all_players()

        return self.player_data.read_all_players()

    def get_all_tournaments(self):
        '''Gets all tournaments'''
        data_class_tournament = Tournaments_Data()
        result = data_class_tournament.read_all_tournaments()

        for elem in result:
            print(elem)

        print(self.player_data.read_all_players())
        res = self.player_data.read_all_players()

        return self.player_data.read_all_players()

    def get_all_association(self):
        '''Gets all associations'''

        data_class_association = Associations_Data()
        result = data_class_association.read_all_associations()

        for elem in result:
            print(elem)
        pass

    def get_all_teams(self):
        '''Gets all teams'''

        data_class_teams = Teams_Data()
        result = data_class_teams.read_all_teams()

        for elem in result:
            print(elem)
        pass


#------------------Create------------------------------------------#
    def create_user(self, user):
        '''Creates a new user'''
        print(self.user_data.create_user(user))
        res2 = self.user_data.create_user(user)
        return self.user_data.create_user(user)

    def create_player(self, player):
        '''Creates a new player'''
        print(self.player_data.create_player(player))
        res2 = self.player_data.create_player(player)
        return self.player_data.create_player(player)

    def create_tournament(self, tournament):
        '''Creates a new tournament'''
        print(self.tournament_data.create_tournament(tournament))
        res2 = self.tournament_data.create_tournament(tournament)
        return self.tournament_data.create_tournament(tournament)

    def create_association(self,association):
        '''Creates a new association'''
        print(self.association_data.create_association(association))
        res2 = self.association_data.create_association(association)
        return self.association_data.create_association(association)

    def create_team(self, team):
        '''Creates a new team'''
        print(self.team_data.create_team(team))
        res2 = self.team_data.create_team(team)
        return self.team_data.create_team(team)