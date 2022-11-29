from data.player_data import Player_Data

class Data_Wrapper:
    def __init__(self):
        self.player_data = Player_Data()

    def get_all_players(self):
        print(self.player_data.read_all_players())
        res = self.player_data.read_all_players()
        #Hér erum við að returna clasa með eftirfarandi methods
        #address , email , name , phone , ssn
        return self.player_data.read_all_players()

    def create_player(self, player):
        print(self.player_data.create_player(player))
        res2 = self.player_data.create_player(player)
        return self.player_data.create_player(player)
        
        
