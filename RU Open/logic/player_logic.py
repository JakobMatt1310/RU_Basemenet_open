

class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)
        
    def team_id_for_player(self):
        """creates a dictionary that has keys as team_id and values as teamname"""
        all_teams = self.data_wrapper.get_all_teams()
        team_id_dict = {}

        for id in all_teams:
            tmp_dict = {id.id: id.name}
            team_id_dict.update(tmp_dict)
        return team_id_dict

    def get_all_players(self):
        all_players = self.data_wrapper.get_all_players()
        player_list = []
        for player in all_players:
            if player.name != "":
                player_list.append(player)
        return player_list

    def edit_player(self, player):
        self.data_wrapper.edit_player(player)

    def check_if_player_exists(self, ssn):
        all_players = self.get_all_players()
        for player in all_players:
            if ssn == player.ssn:
                return player
        return False

    def get_player_by_name(self, name):
        all_player = self.get_all_players()
        players = []
        for player in all_player:
            if player.name[:3] == name[:3]:
                players.append(player)
        return players
    
    def get_player(self, player_id):
        all_players = self.get_all_players()
        for player in all_players:
            if player.id == player_id:
                return player


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
    
    def all_captains(self, ssn):
        #líklega virkar ekki
        all_teams = self.data_wrapper.get_all_teams()
        all_players = self.get_all_players()
        for player in all_players:
            if ssn == player.ssn:
                for team in all_teams:
                    if player.name == team.captain and player.team_id == team.id:
                        return team
        return False
        

            
