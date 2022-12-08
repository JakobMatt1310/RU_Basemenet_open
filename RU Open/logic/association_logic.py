from model.association import Association

class Association_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_association(self, association):
        associations = self.data_wrapper.get_all_associations()
        association_input = association
        if association_input in associations:
            return ValueError
        else:
            self.data_wrapper.create_association(association)
            return True

    def team_in_association(self):
        get_all_associations = self.get_all_associations()
        ret_dict = {}
        for ass in get_all_associations:
            tmp_dict = {ass.id: ass.association_name}
            ret_dict.update(tmp_dict)
        return ret_dict

    def update_association(self):
        self.data_wrapper.update_association()

    def view_association(self):
        return self.data_wrapper.view_association()

    def delete_association(self):
        self.data_wrapper.delete_association()
        
    def get_all_associations(self):
        return self.data_wrapper.get_all_associations()
    
    def validate_association_name_with_all(self, name):
        all_associations = self.get_all_associations()
        for association in all_associations:
            if name == association.association_name:
                return True
        return None

    def get_association(self, association_to_edit):
        all_associations = self.get_all_associations()
        for association in all_associations:
            if association_to_edit == association.association_name:
                return association
        return None
    
    def edit_association(self):
        self.data_wrapper.edit_association()

    def update_association_name(self, association_to_edit):
        return self.data_wrapper.update_association_name(association_to_edit)
    
    def update_association_phone(self, association_to_edit):
        return self.data_wrapper.update_association_phone(association_to_edit)

    def update_association_address(self, association_to_edit):
        return self.data_wrapper.update_association_address(association_to_edit)
