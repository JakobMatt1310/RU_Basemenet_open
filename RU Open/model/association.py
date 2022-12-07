class Association():
    def __init__(self, id="", association_name="", association_phone="", association_address=""):
        '''Constructor for the Associations class'''
        self.id = id
        self.association_name = association_name
        self.association_phone = association_phone
        self.association_address = association_address


    def __str__(self):
        '''Returns a string representation of the Association object'''
        return f"ID: {self.id:>5}, Name: {self.association_name:>5}, Phone: {self.association_phone:>5}, Address: {self.association_address:>5}"
