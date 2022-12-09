from model.player import Player
from model.round import Round
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
            command = input("Enter your command: ").lower()
            command = command.lower()
            if command == "b":
                print("Going back")
                return
            elif command == "q":
                return "q"
            elif command == "1":
                # player.team_id á að vera captain id
                # team_id = 1
                while True:
                    available_matches = self.print_matches(self.team)
                    selection = input("Please select the match you want register points to: ")
                    if selection == "b":
                        return
                    if selection.isdigit() == True:
                        selection = int(selection) - 1
                        if selection <= len(available_matches):
                            match_to_fill_out = available_matches[selection]
                            self.register_points(self, match_to_fill_out)
                            break
                        else:
                            print("Invalid input")
                    else:
                        print("Invalid input")
            else:
                print("invalid input, try again")

            

    def register_points(self, match):
        teams = self.logic_wrapper.get_all_teams()
        for team in teams:
            if match.home_team_id == team.id:
                self.home_team = team
            if match.awat_team_id == team.id:
                self.away_team = team

        while True:
            round = Round()

            

        return
    
    def print_matches(self, team):
        available_matches = self.logic_wrapper.get_matches_by_team_id(team.id)
        print()
        for i, match in enumerate(available_matches, 1):
            home_team = self.logic_wrapper.get_team_by_id(match.home_team_id)
            away_team = self.logic_wrapper.get_team_by_id(match.away_team_id)
            print(f"{i}. {home_team.name} VS {away_team.name}")
        print()
        return available_matches
        #Fixa hvernig stig eru skráð
      
        # home_team = Team("1","Victorious Secret","ÍBV","Isiah Oliver","6")
        # away_team = Team("8","Kiss My Ace","Fram","Amya Graves","4")