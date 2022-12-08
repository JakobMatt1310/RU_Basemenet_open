# import os
import csv

class Mod_password():
    def __init__(self):
        ''''''
        self.file_name = "RU Open/files/moderator_password.csv"

    def read_password(self):
        '''Reads moderators password'''
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                password = row["password"]
        return password
                

    def update_password(self, password):
        '''updates Moderators password '''
        with open(self.file_name, '', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["password"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'password': password})


                                  

