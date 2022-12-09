

class Round_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_round(self, round):
        self.data_wrapper.create_round(round)