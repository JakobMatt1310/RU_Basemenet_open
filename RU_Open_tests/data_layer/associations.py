
class Associations():

    def __init__(self, name="", ssn="", phone="", email="", address=""):
        '''Constructor for the Associations class'''

        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.address = address

    
    def __str__(self):
        '''Returns a string representation of the Association object'''

        return f"Name:{self.name:>5}, SSN:{self.ssn:>5}, Phone:{self.phone:>5}, Email: {self.email:>5}, Address:{self.address:>5}"