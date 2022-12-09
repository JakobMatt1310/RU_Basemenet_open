# import os
import csv
from model.tournament import Tournament
from model.team import Team

class Tournaments_Data():

    def __init__(self):
        '''Constructor for the Tournaments_Data class'''
        self.file_name = "RU Open/files/tournaments.csv"
        self.connection_file = "RU Open/files/teams_in_tourneys.csv"

    def read_all_tournaments(self):
        '''Reads all tournaments from the file'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tournament(row["id"], 
                                           row["name"], 
                                           row["address"], 
                                           row["start_date"],
                                           row["end_date"], 
                                           row["organizer"], 
                                           row["organizer_number"]))
        return ret_list

    def create_tournament(self, tournament: Tournament):
        '''Creates a new tournament in the file'''
        tournament.id = len(self.read_all_tournaments()) + 1
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "name",
                          "address",
                          "start_date",
                          "end_date",
                          "organizer",
                          "organizer_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': tournament.id,
                             'name': tournament.name,
                             'address': tournament.address,
                             'start_date': tournament.start_date,
                             'end_date': tournament.end_date,
                             'organizer': tournament.organizer,
                             'organizer_number': tournament.organizer_number})
    
    def read_tourney_connections(self):
        '''Reads every team connected to a tournament'''
        ret_list = []
        with open(self.connection_file, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tournament(row["tournament_name"], 
                                           row["team_id"]))
            return ret_list
     
    def create_tourney_team_connection(self, tournament_name, team_id):
        '''Creates a connection between a team and a tournament to keep track of which teams are in which tournaments'''
        with open(self.connection_file, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["tournament_name",
                          "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'tournament_name': tournament_name,
                             'team_id': team_id})