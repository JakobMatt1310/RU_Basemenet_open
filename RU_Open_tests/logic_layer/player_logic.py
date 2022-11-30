from data_layer.player_data import Player_data
from model.player import Player

class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)

    def get_all_players(self):
        return self.data_wrapper.get_all_players()

    def update_player(self):
        self.data_wrapper.update_player()
    
    def validate_player_entry(self):
        return self.data_wrapper.validate_player_entry()

    def edit_player(self):
        self.data_wrapper.edit_player()

    def assign_captain(self):
        self.data_wrapper.assign_captain()

    def view_player(self):
        return self.data_wrapper.view_player()

    def view_player_stats(self):
        return self.data_wrapper.view_player_stats()
    
    def delete_player(self):
        self.data_wrapper.delete_player()