
# import os
import csv
from team import Team

class Teams_Data():
    
    def __init__(self):
        '''Constructor for the Teams_Data class'''

        self.file_name = "RU_Basemenet_open/RU_Open_tests/data_files/data_teams.csv"
        print("Teams_Data init")
        

    def read_all_teams(self):
        '''Reads all teams from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row["name"], row["assocition"], row["captain"], row["members"]))
        return ret_list


    def create_team(self, team):
        '''Creates a new team in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "assocition", "captain", "members"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': team.name, 'association': team.assocition, 'captain': team.captain, 'member list': team.members})
            



