from model.player import Player
import time
from ui.print_layouts import (  print_current_menu, 
                                print_current_team_player_list, 
                                view_teams, 
                                print_edit_menu_team )
from model.team import Team
from ui.input_validators import *

class Captain_UI:

                    
    def __init__(self, logic_connection, team):
        self.logic_wrapper = logic_connection
        self.team = team
        team_name = team.name
        self.Menu_selection = { "Current Menu": "Captain Menu", 
                                "Register points for "+ team_name: ">>> Register points for a match"}   
    def menu_output(self):
        print_current_menu(self.Menu_selection)
                   
    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("Going back")
                return
            elif command == "1":
                self.register_points(self.team)
            elif command == "q":
                return "q"
            else:
                print("invalid input, try again")

    def register_points(self, team):
        print("YOU HAVE REGISTERED POINTS")
        print()
        print()
        print()
        input("Press enter to return")
        return
        #Fixa hvernig stig eru skráð
      
        
        # home_team = Team("1","Victorious Secret","ÍBV","Isiah Oliver","6")
        # away_team = Team("8","Kiss My Ace","Fram","Amya Graves","4")
        # players_home_team = self.logic_wrapper.get_all_players_of_team(home_team)
        # players_away_team = self.logic_wrapper.get_all_players_of_team(away_team)
        # match_result = []
        # for i in range(4):
        #     print(f"{'ID. Home team':<30} : ID. Away team")
        #     print()
        #     for k in range(4):
        #         print(f"{players_home_team[k].id}. {players_home_team[k].name:<30} : {players_away_team[k].id}. {players_away_team[k].name}")
        #     print()
        #     print("home_player_id;Leg1;Leg2;Leg2;Leg1;Away_player_id")
        #     print()
        #     print("45;0;1;1;1;23")
        #     results = input(f"Enter resulst for round {i+1} in 501 as shown in example above").split(";")
            
        #     match_result[i] = Round(results[0])
