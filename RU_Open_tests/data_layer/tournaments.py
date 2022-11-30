
class Tournaments():

    def __init__(self, name="", address=""):
        '''Constructor for the Tournaments class'''

        self.name = name
        self.address = address

    
    def __str__(self):
        '''Returns a string representation of the tournaments object'''

        return f"Name:{self.name:>5}, Address:{self.address:>5}"