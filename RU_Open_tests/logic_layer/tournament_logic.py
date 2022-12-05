from data_layer.tournaments_data import Tournaments_Data
from model.tournaments import Tournaments

class Tournament_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
    
    def create_tournament(self, tournament):
        self.data_wrapper.create_tournament(tournament)
    
    def update_tournament(self):
        self.data_wrapper.update_tournament()

    def delete_tournament(self):
        self.data_wrapper.delete_tournament()

    def get_all_tournaments(self):
        return self.data_wrapper.get_all_tournaments()

    def get_tournament(self):
        return self.data_wrapper.get_tournament()
