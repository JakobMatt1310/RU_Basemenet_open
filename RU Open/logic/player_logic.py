# from data.player_data import Player_Data
# from model.player import Player
from logic.team_logic import Team_Logic


class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)
        
    def team_id_for_player(self):
        """creates a dictionary that has keys as team_id and values as teamname"""
        all_teams = Team_Logic.get_all_teams(self)
        team_id_dict = {}

        for id in all_teams:
            tmp_dict = {id.id: id.team_name}
            team_id_dict.update(tmp_dict)
        return team_id_dict

    def get_all_players(self):
        all_players = self.data_wrapper.get_all_players()
        player_list = []
        for player in all_players:
            if player.name != "":
                player_list.append(player)
        return player_list
    
    def update_player(self):
        self.data_wrapper.update_player()

    def edit_player(self):
        self.data_wrapper.edit_player()

    def check_if_player_exists(self, ssn):
        all_players = self.get_all_players()
        for player in all_players:
            if ssn == player.ssn:
                return player
        return False

    def get_player(self,player_name):
        all_player = self.data_wrapper.get_all_players()
        players = []
        for player in all_player:
            if player.name == player_name:
                players.append(player)
        return players


    def view_player_stats(self):
        return self.data_wrapper.view_player_stats()
    
    def delete_player(self):
        self.data_wrapper.delete_player()
    
    def get_all_players_of_team(self, team):
        all_players = self.get_all_players()
        players_of_team = []
        for p in all_players:
            if p.team_id == team.id:
                players_of_team.append(p)
        return players_of_team
    
    def all_captains(self):
        #líklega virkar ekki
        all_teams = self.data_wrapper.read_all_teams(self)
        all_players = self.get_all_players()
        captain_list = []
        captain_list_all = []
        for captains in all_teams:
            if captains.id != "":
                captain_list.append(captains)

        for c in captain_list:
            if c in all_players:
                captain_list_all.append(c)
        return captain_list_all
                
        

            
