from data.player_data import Player_Data
from model.player import Player

class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)

    def get_all_players(self):
        return self.data_wrapper.get_all_players()

    def validate_player_entry(self):
        pass

    def edit_player(self):
        pass

    def assign_captain(self):
        pass

    def view_player(self):
        pass

    def view_player_stats(self):
        pass
    
    def delete_player(self):
        pass