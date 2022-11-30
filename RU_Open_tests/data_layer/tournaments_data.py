
# import os
import csv
from tournaments import Tournaments


class Tournaments_Data():

    def __init__(self):
        '''Constructor for the Tournaments_Data class'''

        self.file_name = "tournaments.csv"
        print("Tournaments_Data init")


    def read_all_tournaments(self):
        '''Reads all tournaments from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tournaments(row["name"], row["ssn"], row["phone"], row["email"], row["address"]))
        return ret_list


    def create_tournament(self, tournament):
        '''Creates a new tournament in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "ssn", "phone", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': tournament.name, 'address': tournament.address})
