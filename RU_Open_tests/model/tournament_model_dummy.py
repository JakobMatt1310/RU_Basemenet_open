class Tournament:
    def __init__(self, tournament_name, competing_teams=None, first_day_of_tourney="", last_day_of_tourney="", organizer="", oranizer_phone_number=""):
        if competing_teams == None:
            competing_teams = []
        self.tournament_name = tournament_name
        self.competing_teams = competing_teams
        self.first_day_of_tourney = first_day_of_tourney
        self.last_day_of_tourney = last_day_of_tourney
        self.organizer = organizer
        self.organizer_phone_number = oranizer_phone_number