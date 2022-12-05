from data_layer.associations_data import Associations_Data
from model.associations import Associations

class Association_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_association(self, association):
        self.data_wrapper.create_association(association)
    
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

    def get_all_associations(self, associations):
            
        return self.data_wrapper.get_all_associations()

    def get_association(self, association):
        get_association = self.get_association()
        association = []
        for p in get_association:
            if p.association_id == association.id:
                association.append(p)
        return association
    
    def edit_association(self):
        self.data_wrapper.edit_association()
