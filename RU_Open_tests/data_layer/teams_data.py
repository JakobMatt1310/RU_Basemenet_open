
# import os
import csv
from team import Team


class Teams_Data():

    def __init__(self):
        '''Constructor for the Teams_Data class'''

        self.file_name = "teams.csv"
        print("Teams_Data init")
        

    def read_all_teams(self):
        '''Reads all teams from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row["team_name"], row["assocition_name"], row["captain_name"], [row["player_names"], row["player_names"], row["player_names"]]))
        return ret_list


    def create_team(self, team):
        '''Creates a new team in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["team", "assocition", "captain_name", ["player_names", "player_names", "player_names"]]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'team': team.team_name, 'association': team.assocition_name, 'captain': team.captain_name, 'player_list': team.list})
            



