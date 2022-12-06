
class Fixture():

    def __init__(self, home_team="", home_team_score="", away_team="", away_team_score=""):
        '''Constructor for the Fixture class'''

        self.home_team = home_team
        self.home_team_score = home_team_score
       
        self.away_team = away_team
        self.away_team_score = away_team_score
       
    def function(self):
        print(f"{self.home_team} {self.home_team_score} - {self.away_team_score} {self.away_team}")
    
    #def __str__(self):
        '''Returns a string representation of the Fixture object'''

        #print(f"{self.home_team} {self.home_team_score} - {self.away_team_score} {self.away_team}")

oli = Fixture("A", 3, "B", 2)
oli.function()

        