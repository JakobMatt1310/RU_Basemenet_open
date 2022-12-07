#import os
import csv
from model.player import Player
#_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Player_Data():
    def __init__(self):
        '''Constructor for the Player_Data class'''
        self.file_name = "RU Open/files/players.csv"

    def read_all_players(self):
        '''Reads all players from the file'''
        #_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row['id'],
                                       row["name"],
                                       row["ssn"], 
                                       row["phone"],
                                       row["email"], 
                                       row["address"], 
                                       row['team_id']))
        return ret_list

    def create_player(self, player):
        '''Creates a new player in the file'''
        player.id = len(self.read_all_players()) + 1
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "name",
                          "ssn", 
                          "phone", 
                          "email", 
                          "address", 
                          "team_id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': player.id, 
                            'name': player.name, 
                            'ssn': player.ssn, 
                            'phone': player.phone, 
                            'email': player.email, 
                            'address': player.address, 
                            'team_id': player.team_id})
