class Game:
    def __init__(self, home_team_player="", away_team_player="", home_player_legs=[0,0], away_player_legs=[0,0], match_score=None, gamemode=""):
        self.home_team_player = home_team_player
        self.away_team_player = away_team_player
        self.gamemode = gamemode
        self.home_player_legs = home_player_legs
        self.away_player_legs = away_player_legs
        if match_score == None:
            match_score = [[0,0][0,0]]
        self.match_score = match_score

    def __get_match_score__(self, home_player_legs_won="", away_player_legs_won=""):
        #Please enter how many legs 
        if home_player_legs_won == 0:
            self.home_player_legs == [0,0]
        elif home_player_legs_won == 1:
            self.home_player_legs == [1,0]
        elif home_player_legs_won == 2:
            self.home_player_legs == [1,1]
        if away_player_legs_won == 0:
            self.away_player_legs == [0,0]
        elif away_player_legs_won == 1:
            self.away_player_legs == [1,0]
        elif away_player_legs_won == 2:
            self.away_player_legs == [1,1]

        self.match_score == [self.home_player_legs, self.away_player_legs]
    
    #
        



        