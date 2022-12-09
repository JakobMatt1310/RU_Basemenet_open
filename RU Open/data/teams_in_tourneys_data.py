# import os
import csv
from model.teams_in_tourneys import Teams_In_Tourneys

class Teams_In_Tourneys_Data():
    def __init__(self):
        '''Constructor for the Teams_In_Tourney_Data class'''
        self.file_name = "RU Open/files/teams_in_tourneys.csv"

    def read_all_teams_in_tourneys(self):
        '''Reads all teams in tournaments from the file and returns a list of teams in tournaments'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Teams_In_Tourneys(row["tournament_name"],row["team_id"]))
        return ret_list

    def create_team_in_tourney(self, tournament: classmethod, team: classmethod):
        '''Add team to tournament in the file teams_in_tourneys.csv, one team at a time'''
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["torunament_name", "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Tournament name': tournament.__name__, 'Team ID': team.id})