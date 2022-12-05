# import os
import csv
from model.team import Team

class Teams_Data():
    
    def __init__(self):
        '''Constructor for the Teams_Data class'''

        self.file_name = "RU Open/files/teams.csv"
        print("Teams_Data init")

    def read_all_teams(self):
        '''Reads all teams from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row["id"], row["name"], row["assocition"], row["captain"], row["association_id"]))
        return ret_list

    def create_team(self, team):
        '''Creates a new team in the file'''
        team.id = len(self.read_all_teams()) + 1
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "association", "captain", "association_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': team.id, 
                            'name': team.team_name, 
                            'association': team.association_name, 
                            'captain': team.captain_name, 
                            'association_id': team.association_id})