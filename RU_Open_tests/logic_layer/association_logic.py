from data_layer.associations_data import Associations_Data
from model.associations import Associations

class Association_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_association(self, association):
        self.data_wrapper.create_association(association)

    def validate_association_entry(self):
        return self.data_wrapper.validate_association_entry()
    
    def update_association(self):
        self.data_wrapper.update_association()

    def view_association(self):
        return self.data_wrapper.view_association()

    def delete_association(self):
        self.data_wrapper.delete_association()

    def get_all_associations(self):
        return self.data_wrapper.get_all_associations()

    def get_association(self):
        return self.data_wrapper.get_association()
    
    def edit_association(self):
        self.data_wrapper.edit_association()
