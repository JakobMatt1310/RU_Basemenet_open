from data.player_data import Player_Data

class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()

    def get_all_players(self):
        return self.player_data.read_all_players()

    def create_player(self, player):
        return self.player_data.create_player(player)