
# import os
import csv
from association import Association


class Associations_Data():

    def __init__(self):
        '''Constructor for the Associations_Data class'''

        self.file_name = "RU_Basemenet_open/RU_Open_tests/data_files/data_associations.csv"
        print("Associations_Data init")


    def read_all_associations(self):
        '''Reads all associations from the file'''

        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Association(row["name"], row["phone"], row["address"]))
        return ret_list


    def create_association(self, association):
        '''Creates a new association in the file'''

        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "phone", "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': association.name, 'phone': association.phone, 'address': association.address})
