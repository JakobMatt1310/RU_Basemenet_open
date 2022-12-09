class Team():
    def __init__(self,
                 id="",
                 name="", 
                 association="", 
                 captain="", 
                 association_id=""):
        '''Constructor for the Team class'''
        self.id = id
        self.name = name
        self.association = association
        self.captain = captain
        self.association_id = association_id

    def __str__(self):
        '''Returns a string representation of the Team object'''
        return f"ID: {self.id:>5}, Team: {self.name:>5}, Association: {self.association:>5}, Association ID: {self.association_id:>5}, Captain: {self.captain:>5}"
