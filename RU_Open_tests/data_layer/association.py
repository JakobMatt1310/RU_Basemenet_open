
class Association():

    def __init__(self, association_name="", association_phone="", association_address=""):
        '''Constructor for the Associations class'''

        self.name = association_name
        self.phone = association_phone
        self.address = association_address

    
    def __str__(self):
        '''Returns a string representation of the Association object'''

        return f"Name: {self.name:>5}, Phone: {self.phone:>5}, Address: {self.address:>5}"