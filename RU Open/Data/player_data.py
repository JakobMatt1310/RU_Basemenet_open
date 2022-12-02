
#import os
import csv
from player import Player
#_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Player_Data():

    def __init__(self):
        '''Constructor for the Player_Data class'''

        self.file_name = "RU_Basemenet_open/RU_Open_tests/data_files/data_players.csv"
        print("Player_Data init")
        

    def read_all_players(self):
        '''Reads all players from the file'''
        #_location_ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row["name"], row["ssn"], row["phone"], row["email"], row["address"]))
        return ret_list


    def create_player(self, player):
        '''Creates a new player in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "ssn", "phone", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': player.player_name, 'ssn': player.ssn, 'phone': player.phone, 'email': player.email, 'address': player.address})
            

