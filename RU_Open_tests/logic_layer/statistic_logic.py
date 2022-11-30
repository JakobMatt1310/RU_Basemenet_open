from data_layer.statistics_data import Statistics_Data
from model.statistics import Statistics

class Statistic_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def get_win_percentage(self, stats):
        return self.data_wrapper.get_win_percentage(stats)

    def get_quality_points(self):
        return self.data_wrapper.get_quality_points()

    def get_games_played(self):
        return self.data_wrapper.get_games_played()

    def view_stats_for_everything(self):
        return self.data_wrapper.view_stats_for_everything()

    def view_player_stats(self):
        return self.data_wrapper.view_player_stats()

    def view_team_stats(self):
        return self.data_wrapper.view_team_stats()