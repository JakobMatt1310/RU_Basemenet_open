from model.association import Association

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
        
    def get_all_associations(self):
        return self.data_wrapper.get_all_associations()
    
    def validate_association_name_with_all(self, name):
        all_associations = self.get_all_associations()
        for association in all_associations:
            if name == association.association_name:
                return True
        return None

    def get_association(self, association):
        get_association = self.get_association()
        association = []
        for p in get_association:
            if p.association_id == association.id:
                association.append(p)
        return association
    
    def edit_association(self):
        self.data_wrapper.edit_association()
