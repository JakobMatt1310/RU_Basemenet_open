class Association:
    def __init__(self, association_name="", association_phone_number="", association_address="", association_teams=None):
        if association_teams == None:
            association_teams = []
        self.association_name = association_name
        self.association_phone_number = association_phone_number
        self.association_address = association_address