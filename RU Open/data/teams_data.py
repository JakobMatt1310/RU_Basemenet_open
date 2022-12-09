# import os
import csv
from model.team import Team
class Teams_Data():
    def __init__(self):
        '''Constructor for the Teams_Data class'''
        self.file_name = "RU Open/files/teams.csv"

    def read_all_teams(self):
        '''Reads all teams from the file'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(row["id"],
                                     row["name"], 
                                     row["association"], 
                                     row["captain"], 
                                     row["association_id"]))
        return ret_list

    def create_team(self, team):
        '''Creates a new team in the file'''
        team.id = str(len(self.read_all_teams()) + 1)
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "name", 
                          "association", 
                          "captain", 
                          "association_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': team.id, 
                            'name': team.name, 
                            'association': team.association, 
                            'captain': team.captain, 
                            'association_id': team.association_id})

    def update_team_name(self, team_to_edit):
        '''Updates team name'''
        new_team_name = team_to_edit.name
        read_all_teams = self.read_all_teams()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "association", 
                          "captain", 
                          "association_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for team in read_all_teams:
                if team.id == team_to_edit.id:
                    team.name = new_team_name
                writer.writerow({'id': team.id,
                                'name': team.name,
                                'association': team.association,
                                'captain': team.captain,
                                'association_id': team.association_id})

            return True

    def update_team_association(self, team_to_edit):
        '''Updates team association'''
        new_association = team_to_edit.association
        read_all_teams = self.read_all_teams()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "association", 
                          "captain", 
                          "association_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for team in read_all_teams:
                if team.id == team_to_edit.id:
                    team.association = new_association
                writer.writerow({'id': team.id,
                                'name': team.name,
                                'association': team.association,
                                'captain': team.captain,
                                'association_id': team.association_id})

            return True

    def update_team_captain(self, team_to_edit):
        '''Updates team captain'''
        new_captain = team_to_edit.captain
        read_all_teams = self.read_all_teams()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "association", 
                          "captain", 
                          "association_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for team in read_all_teams:
                if team.id == team_to_edit.id:
                    team.captain = new_captain
                writer.writerow({'id': team.id,
                                'name': team.name,
                                'association': team.association,
                                'captain': team.captain,
                                'association_id': team.association_id})

            return True