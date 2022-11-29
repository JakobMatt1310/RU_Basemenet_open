from player_model_dummy import Player 

class Logic_Wrapper:
    def __init__(self):
        pass
        # self.data_wrapper = Data_Wrapper()
        # self.player_logic = Player_Logic(self.data_wrapper)

    # def create_player(self, player):
    #     return self.player_logic.create_player(player)

    def get_all_players(self):
        return [Player("Ólafur Finnbogi", "1234567890", "6969696", "Yamz@hotmale.com", "Áleggsoð 34"),
                Player("Runólfur Bjargarson", "1548592654", "5554444", "runo@gmail.com", "Kristalbó 3"),
                Player("Hákarl Ofsaveður", "9181827846", "4545454", "Hammi@yamz.com", "Absírtú 6"),
                Player("Siðferði Þingi", "6497135689", "4567891", "Siiidd@jolajapl.is", "Kárlhög 49"),
                Player("Málmundur Árbjarg", "0528598945", "4569873", "Malli@halli.is", "Kringum 11"),]
        # return self.player_logic.get_all_players()
        
        # self, name="", ssn="", phone="", email="", address=""