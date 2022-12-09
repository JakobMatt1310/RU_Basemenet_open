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
        self.team = "blabla"
        team_name = "blabla"
        self.Menu_selection = { "Current Menu": "Captain Menu", 
                                "Register points for "+ team_name: ">>> Register points for a match"}   
    def menu_output(self):
        print_current_menu(self.Menu_selection)
                   
    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
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