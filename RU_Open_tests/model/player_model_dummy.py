class Player:
    def __init__(self, name="", ssn="", phone="", email="", address="", team=""):
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.address = address

    
    def __str__(self):
        return "Name:{:>5}, SSN:{:>5}, Phone:{:>5}, Email: {:>5}, Address:{:>5}".format(self.name, self.ssn, self.phone, self.email, self.address)