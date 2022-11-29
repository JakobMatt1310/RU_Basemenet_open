import csv
from model.player import Player

class Player_Data:
    def __init__(self):
        self.file_name = "files/players.csv"

    def read_all_players(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(row["name"], row["ssn"], row["phone"], row["email"], row["address"]))
        return ret_list

    def create_player(self, player):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "ssn", "phone", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': player.name, 'ssn': player.ssn, 'phone': player.phone, 'email': player.email, 'address': player.address})