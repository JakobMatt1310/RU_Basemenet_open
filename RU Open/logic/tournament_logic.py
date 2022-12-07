from Data.tournaments_data import Tournaments_Data
from Model.tournament import Tournament

class Tournament_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
    
    def create_tournament(self, tournament):
        tournaments = self.data_wrapper.get_all_tournaments()
        tournament_input = tournament
        if tournament_input in tournaments:
            return ValueError
        else:
            self.data_wrapper.create_tournament(tournament)
            return True
    
    def update_tournament(self):
        self.data_wrapper.update_tournament()

    def delete_tournament(self):
        self.data_wrapper.delete_tournament()

    def get_all_tournaments(self):
        return self.data_wrapper.get_all_tournaments()

    def get_tournament(self):
        return self.data_wrapper.get_tournament()
    
     #def get_tournament(self):
    #    all_tournaments = self.data_wrapper.get_all_tournaments()

    #    if Tournament_intput in all_tournaments:
    #        return t
    #    return players_of_team
