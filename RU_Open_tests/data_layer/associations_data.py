
# import os
import csv
from associations import Associations


class Associations_Data():

    def __init__(self):
        '''Constructor for the Associations_Data class'''

        self.file_name = "associations.csv"
        print("Associations_Data init")


    def read_all_associations(self):
        '''Reads all associations from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Associations(row["name"], row["ssn"], row["phone"], row["email"], row["address"]))
        return ret_list


    def create_association(self, association):
        '''Creates a new association in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "ssn", "phone", "email", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': association.name, 'ssn': association.ssn, 'phone': association.phone, 'email': association.email, 'address': association.address})
