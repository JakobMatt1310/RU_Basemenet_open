from data_layer.associations_data import Associations_Data
from model.association_model_dummy import Associations

class Association_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_association(self, association):
        associations = self.data_wrapper.create_association(self, association)
        association_input = association
        if association_input in associations:
            return ValueError
        else:
            self.data_wrapper.create_association(self, association)
            return True
    
    def update_association(self):
        self.data_wrapper.update_association()

    def view_association(self):
        return self.data_wrapper.view_association()

    def delete_association(self):
        self.data_wrapper.delete_association()
        
    def team_in_association(self):
        get_all_associations = self.get_all_associations()
        ret_dict = {}
        for ass in get_all_associations:
            tmp_dict = {ass.id: ass.association_name}
            ret_dict.update(tmp_dict)
        return ret_dict

    def get_all_associations(self):
        return self.data_wrapper.get_all_associations()

    def validate_association_name_with_all(self, name):
        all_associations = self.get_all_associations()
        for association in all_associations:
            if name == association.association_name:
                return True
        return None

    def get_association(self):
        get_association = self.data_wrapper.get_all_associations()
        association_input = ???????
        if association_input in get_association:
            return association_input
        else:
            return ValueError
    
    def edit_association(self):
        self.data_wrapper.edit_association()