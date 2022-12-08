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



    def update_association_name(self, association_to_edit: Association):
        '''Updates association name'''
        found = False
        #new_association_name = association_to_edit.association_name
        get_all_associations = self.get_all_associations()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "phone",  
                          "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for association in get_all_associations:
                if association.id == association_to_edit.id:
                    association.association_name = association_to_edit.association_name
                    found = True
                writer.writerow({'id': association.id,
                                'name': association.association_name,
                                'phone': association.association_phone,
                                'address': association.association_address})
            if found == True:
                return found

