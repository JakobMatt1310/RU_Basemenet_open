
# import os
import csv
from model.tournament import Tournament


class Tournaments_Data():

    def __init__(self):
        '''Constructor for the Tournaments_Data class'''

        self.file_name = "RU Open/files/tournaments.csv"
        print("Tournaments_Data init")


    def read_all_tournaments(self):
        '''Reads all tournaments from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tournament(row["name"], row["address"], row["start_date"], row["end_date"], row["game_count"], row["teams_submitted"], row["game_id"], row["player_nr"], row["game_type"], row["leg_nr"], row["player_id"], row["q_points"]))
        return ret_list


    def create_tournament(self, tournament):
        '''Creates a new tournament in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "address", "start_date", "end_date", "game_count", "teams_submitted", "game_id", "player_nr", "game_type", "leg_nr", "player_id", "q_points"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': tournament.name, 'address': tournament.address, 'start_date': tournament.start_date, 'end_date': tournament.end_date, 'game_count': tournament.game_count, 'teams_submitted': tournament.teams_submitted, 'game_id': tournament.game_id, 'player_nr': tournament.player_nr, 'game_type': tournament.game_type, 'leg_nr': tournament.leg_nr, 'player_id': tournament.player_id, 'q_points': tournament.q_points})
