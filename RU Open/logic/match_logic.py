

class Match_logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        
    def get_all_matches(self):
        return self.data_wrapper.get_all_matches()

    def create_match(self, match):
        return self.data_wrapper.create_match(match)
    
    def update_match(self, match):
        return self.data_wrapper.update_match(match)  

    def generate_matches(self, tournament):
        pass


    