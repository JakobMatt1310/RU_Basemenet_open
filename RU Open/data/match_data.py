import csv
from model.match import Match

class Match_Data():

    def __init__(self):
        '''Constructor for the Tournaments_Data class'''
        self.file_name = "RU Open/files/match.csv"

    def read_all_matches(self):
        '''Reads all tournaments from the file'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Match(row["id"], 
                                        row["tournament_id"], 
                                        row["home_team_id"], 
                                        row["away_team_id"],
                                        row["date"], 
                                        row["time"]))
        return ret_list

    def create_match(self, match: classmethod):
        '''Creates a new tournament in the file'''
        match.id = len(self.read_all_matches()) + 1
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "tournament_id",
                          "home_team_id",
                          "away_team_id",
                          "date",
                          "time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': match.id,
                             'tournament_id': match.tournament_id,
                             'home_team_id': match.home_team_id,
                             'away_team_id': match.away_team_id,
                             'date': match.date,
                             'time': match.time})
    
    def update_match(self, match: classmethod, match_to_update):
        '''Creates a new tournament in the file'''
        matches = self.read_all_matches()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "tournament_id",
                          "home_team_id",
                          "away_team_id",
                          "date",
                          "time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for match in matches:
                if match.id == match_to_update.id:
                    match.tournament_id = match_to_update.tournament_id
                    match.home_team_id = match_to_update.home_team_id
                    match.away_team_id = match_to_update.away_team_id
                    match.date = match_to_update.date
                    match.time = match_to_update.time
                    
                writer.writerow({'id': match.id,
                                'tournament_id': match.tournament_id,
                                'home_team_id': match.home_team_id,
                                'away_team_id': match.away_team_id,
                                'date': match.date,
                                'time': match.time})