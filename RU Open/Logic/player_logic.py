from data.player_data import Player_Data
from model.player import Player
from logic.team_logic import Team_Logic


class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player):
        self.data_wrapper.create_player(player)

    def get_all_players(self):
        all_teams = Team_Logic.get_all_teams(self)
        team_id_dict = {}

        for id in all_teams:
            tmp_dict = {id.id: id.team_name}
            team_id_dict.update(tmp_dict)

        return self.data_wrapper.get_all_players(), team_id_dict