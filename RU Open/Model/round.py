class Round:
    def __init__(self, match_id="",
                round_nr="",
                gamemode="",
                home_leg1="0",
                home_leg2="0",
                away_leg1="0",
                away_leg2="0",
                home_player1="none",
                home_player2="none",
                home_player3="none",
                home_player4="none", 
                away_player1="none", 
                away_player2="none", 
                away_player3="none", 
                away_player4="none"):
        self.round_nr = round_nr
        self.match_id = match_id
        self.home_leg1 = home_leg1
        self.home_leg2 = home_leg2
        self.away_leg1 = away_leg1
        self.away_leg2 = away_leg2
        self.home_player1 = home_player1
        self.home_player2 = home_player2
        self.home_player3 = home_player3
        self.home_player4 = home_player4
        self.away_player1 = away_player1
        self.away_player2 = away_player2
        self.away_player3 = away_player3
        self.away_player4 = away_player4
        gamemodes_501 = ["1", "2", "3", "4", "7"]
        if round_nr in gamemodes_501:
            gamemode = "501"
        elif round_nr == "5":
            gamemode = "301"
        elif round_nr == "6":
            gamemode = "C"
        self.gamemode = gamemode

        #round.csv
        #match_id, round_nr, gamemode, home_p1, home_p2, home_p3, home_p4, home_leg1, home_leg2, away_leg1, away_leg2, away_p1, away_p2, away_p3, away_p4
        
        
        

        
       
    def function(self):
        print("{} {:>5} {} {} {} {:<5} {}".format(self.home_player1, self.home_leg1, self.home_leg2, self.gamemode, self.away_leg1, self.away_leg2, self.away_player1))
    
    #def __str__(self):
        '''Returns a string representation of the Fixture object'''

        #print(f"{self.home_team} {self.home_team_score} - {self.away_team_score} {self.away_team}")

oli = Round('1', '3', "", '1', '0', '1', '1', 'Jonas',"","","",'Albert',"","","")
oli.function()

        