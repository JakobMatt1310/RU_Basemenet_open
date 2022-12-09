import csv
from model.round import Round

class Rounds_Data():
    round_count = 0

    def __init__(self):
        self.file_name = "RU Open/files/rounds.csv"
        


    def read_all_rounds(self):
        '''Reads all rounds from file'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Round(row['match_id'],
                                       row["round_nr"],
                                       row["gamemode"],
                                       row["home_leg1"],
                                       row["home_leg2"], 
                                       row["away_leg1"], 
                                       row['away_leg2'],
                                       row["home_player1"],
                                       row["home_player2"],
                                       row["home_player3"],
                                       row["home_player4"],
                                       row["away_player1"],
                                       row["away_player2"],
                                       row["away_player3"],
                                       row["away_player4"]))
        return ret_list
    
    def create_round(self, round):
        '''Adds each round numbered 1-7 to the file'''
             
        if self.round_count in range(1,8):
            round.round_nr = str(self.round_count)

            with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                fieldnames = ["match_id",
                                "round_nr",
                                "gamemode",
                                "home_leg1",
                                "home_leg2",
                                "away_leg1",
                                "away_leg2",
                                "home_player1",
                                "home_player2",
                                "home_player3",
                                "home_player4",
                                "away_player1",
                                "away_player2",
                                "away_player3",
                                "away_player4"]

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({'match_id': round.match_id,
                                'round_nr': round.round_nr,
                                'gamemode': round.gamemode,
                                'home_player1': round.home_player1,
                                'home_player2': round.home_player2,
                                'home_player3': round.home_player3,
                                'home_player4': round.home_player4,
                                'home_leg1': round.home_leg1,
                                'home_leg2': round.home_leg2,
                                'away_leg1': round.away_leg1,
                                'away_leg2': round.away_leg2,
                                'away_player1': round.away_player1,
                                'away_player2': round.away_player2,
                                'away_player3': round.away_player3,
                                'away_player4': round.away_player4})
        else:
            self.round_count = 0

    def updte_round(self, round_info_update):
        '''Udates round information'''
        pass