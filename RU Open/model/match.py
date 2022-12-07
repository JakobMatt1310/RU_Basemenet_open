class Match:
    def __init__(self, 
                 match_id, 
                 tournament_id, 
                 home_team_id, 
                 away_team_id):

        self.match_id = match_id
        self.tournament_id = tournament_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id

    def function(self):
        print(f"Tournament id: {self.tournament_id}\nMatch id: {self.match_id}\n{'':<20}Home Team {self.home_team_id:>14} - {self.away_team_id:<14} Away Team")
    

oli = Match('1', '18', 'Stjarnan', 'Selfoss')
oli.function() 
