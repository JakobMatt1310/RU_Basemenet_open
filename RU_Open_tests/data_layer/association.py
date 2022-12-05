
class Association():

    def __init__(self, association_name="", association_phone="", association_address=""):
        '''Constructor for the Associations class'''

        self.association_name = association_name
        # self.association_ssn = association_ssn
        self.association_phone = association_phone
        # self.association_email = association_email
        self.association_address = association_address

    
    def __str__(self):
        '''Returns a string representation of the Association object'''

        return f"Name: {self.association_name:>5}, Phone: {self.association_phone:>5}, Address: {self.association_address:>5}"