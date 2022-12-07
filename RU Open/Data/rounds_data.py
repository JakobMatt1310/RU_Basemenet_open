import csv
from model.round import Round

class Rounds_Data:
    def create_round(self):
            '''Adds each round numbered 1-7 to the file'''
            
            with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
                fieldnames = ["match_id", "round_nr", "gamemode", "home_p1", "home_p2", "home_p3", "home_p4", "home_leg1", "home_leg2",
                "away_leg1", "away_leg2", "away_p1", "away_p2", "away_p3", "away_p4"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({'match_id': round.round_nr, 'gamemode': round.gamemode , home_p1, home_p2, home_p3, home_p4, home_leg1, home_leg2, away_leg1, away_leg2, away_p1, away_p2, away_p3, away_p4})