class Association():
    def __init__(self, id="",
                 name="",
                 phone="",
                 address=""):
        '''Constructor for the Associations class'''
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address


    def __str__(self):
        '''Returns a string representation of the Association object'''
        return f"ID: {self.id:>5}, Name: {self.name:>5}, Phone: {self.phone:>5}, Address: {self.address:>5}"
