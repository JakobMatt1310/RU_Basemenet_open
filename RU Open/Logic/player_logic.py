from data.player_data import Player_Data
from model.player import Player

class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)

    def get_all_players(self):
        return self.data_wrapper.get_all_players