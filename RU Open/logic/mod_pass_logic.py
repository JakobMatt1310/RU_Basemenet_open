

class Mod_Pass_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def get_moderator_password(self):
        return self.data_wrapper.get_moderator_password()
        
    def update_password(self, password):
        return self.data_wrapper.update_password(self, password)