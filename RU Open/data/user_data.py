
# import os
import csv
from model.user import User

class User_Data():

    def __init__(self):
        '''Constructor for the User_Data class'''

        self.file_name = "RU Open/files/users.csv"


    def read_all_users(self):
        '''Reads all users from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(User(row["name"], row["ssn"], row["phone"], row["email"], row["address"]))
        return ret_list


    def create_user(self, user):
        '''Creates a new user in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "ssn", "phone", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': user.name, 'ssn': user.ssn, 'phone': user.phone, 'email': user.email, 'address': user.address})
