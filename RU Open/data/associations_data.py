# import os
import csv
from model.association import Association

class Associations_Data():
    def __init__(self):
        '''Constructor for the Associations_Data class'''
        self.file_name = "RU Open/files/associations.csv"

    def read_all_associations(self):
        '''Reads all associations from the file'''
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Association(row["id"],
                                            row["name"],
                                            row["phone"],
                                            row["address"]))
        return ret_list

    def create_association(self, association: Association):
        '''Creates a new association in the file'''
        association.id = len(self.read_all_associations()) + 1    
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "name",
                          "phone",
                          "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'id': association.id,
                             'name': association.association_name,
                             'phone': association.association_phone,
                             'address': association.association_address})

    def overwrite_list(self, some_list):
        # open the CSV file in write mode
        with open("test.csv", "w", newline="") as file:
            # create a CSV writer object
            writer = csv.writer(file)

            # write the data to the CSV file
            for row in my_list:
                writer.writerow(row)