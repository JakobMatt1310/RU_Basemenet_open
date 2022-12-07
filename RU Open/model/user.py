class User():
    def __init__(self, 
                 user_name="", 
                 user_ssn="", 
                 user_phone="", 
                 user_email="", 
                 user_address=""):
        '''Constructor for the User class'''
        self.user_name = user_name
        self.user_ssn = user_ssn
        self.user_phone = user_phone
        self.user_email = user_email
        self.user_address = user_address

    def __str__(self):
        '''Returns a string representation of the User object'''
        return f"Name: {self.user_name:>5}, SSN: {self.user_ssn:>5}, Phone: {self.user_phone:>5}, Email: {self.user_email:>5}, Address: {self.user_address:>5}"
