from model.game_model_dummy import Game

class Match:
    def __init__(self, home_team="", away_team="", match_scheduled="", games=None):
        self.home_team = home_team
        self.away_team = away_team
        self.match_scheduled = match_scheduled

    def __get_games__():
        pass
'''    def read_all_players(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row["home_team"], row["away_team"], row["match_scheduled"], row["e"], row["address"]))
        return ret_list'''
