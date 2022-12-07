class Match:
<<<<<<< HEAD
    def __init__(self, match_id="", tournament_id="", home_team_id="", away_team_id="", date="", time=""):
=======
    def __init__(self, 
                 match_id, 
                 tournament_id, 
                 home_team_id, 
                 away_team_id):

>>>>>>> 0ef3cd102ce705ac7b3a713a4f47af662d3beab7
        self.match_id = match_id
        self.tournament_id = tournament_id
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.date = date
        self.time = time

    def function(self):
<<<<<<< HEAD
        print("Tournament id: {}\nMatch id: {}\n{}{} \n{:<20}Home Team {:>14} - {:<14} Away Team".format(self.tournament_id, self.match_id,"",self.date, self.time, self.home_team_id, self.away_team_id))
=======
        print(f"Tournament id: {self.tournament_id}\nMatch id: {self.match_id}\n{'':<20}Home Team {self.home_team_id:>14} - {self.away_team_id:<14} Away Team")
>>>>>>> 0ef3cd102ce705ac7b3a713a4f47af662d3beab7
    

oli = Match('1', '18', 'Stjarnan', 'Selfoss', '28.12.2022', '17:10')
oli.function() 
oli = Match('1', '18', 'Stjarnan', 'Selfoss')
oli.function() 
