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

    def create_association(self, association):
        '''Creates a new association in the file'''
        association.id = len(self.read_all_associations()) + 1    
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id",
                          "name",
                          "phone",
                          "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id': association.id,
                             'name': association.name,
                             'phone': association.phone,
                             'address': association.address})

    def update_association_name(self, association_to_edit):
        '''Updates association name'''
        get_all_associations = self.read_all_associations()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "phone",  
                          "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for association in get_all_associations:
                if association.id == association_to_edit.id:
                    association.name = association_to_edit.name
                writer.writerow({'id': association.id,
                                'name': association.name,
                                'phone': association.phone,
                                'address': association.address})
            return True

    def update_association_phone(self, association_to_edit):
        '''Updates association phone'''
        get_all_associations = self.read_all_associations()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "phone",  
                          "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for association in get_all_associations:
                if association.id == association_to_edit.id:
                    association.phone = association_to_edit.phone
                writer.writerow({'id': association.id,
                                'name': association.name,
                                'phone': association.phone,
                                'address': association.address})
            return True

    def update_association_address(self, association_to_edit):
        '''Updates association address'''
        get_all_associations = self.read_all_associations()
        with open(self.file_name, 'w', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", 
                          "name", 
                          "phone",  
                          "address"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for association in get_all_associations:
                if association.id == association_to_edit.id:
                    association.address = association_to_edit.address
                writer.writerow({'id': association.id,
                                'name': association.name,
                                'phone': association.phone,
                                'address': association.address})
            return True