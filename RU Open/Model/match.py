class Match:
    def __init__(self, match_id="", tournament_id="", home_team_id="", away_team_id="", date="", time=""):
        self.match_id = match_id
        self.tournament_id = tournament_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.date = date
        self.time = time

    def function(self):
        print("Tournament id: {}\nMatch id: {}\n{}{} \n{:<20}Home Team {:>14} - {:<14} Away Team".format(self.tournament_id, self.match_id,"",self.date, self.time, self.home_team_id, self.away_team_id))
    

oli = Match('1', '18', 'Stjarnan', 'Selfoss', '28.12.2022', '17:10')
oli.function() 