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
        '''Cycles through the list of all teams to find our team 
        and checks if our team is home or away for this match'''
        teams = self.logic_wrapper.get_all_teams()
        for team in teams:
            if match.home_team_id == team.id:
                captains_team = team
            if match.away_team_id == team.id:
                captains_team = team
        count = 1
        self.register_round_1(self, count,  match)
        count += 1
        self.register_round_1(self, match)


        # round 1
        while True:
            round = Round()
            round.match_id = match.id
            players_in_team = self.print_players_in_team(captains_team)
            selection = input("Please select the player who played in the first round (501 single): ")
            if selection == "b":
                return
            if selection.isdigit() == True:
                selection = int(selection) - 1
                if selection <= len(players_in_team):
                    round.home_player1 = players_in_team[selection].name
            legs_won = int(input(f"How many legs did {round.home_player1} win? (0-2)"))
            if legs_won in range(0, 3):
                if legs_won == 0:
                    round.home_leg1 == '0'
                    round.home_leg2 == '0'
                elif legs_won == 1:
                    round.home_leg1 == '1'
                    round.home_leg2 == '0'
                elif legs_won == 2:
                    round.home_leg1 == '1'
                    round.home_leg2 == '1'
            else:
                print("Invalid input, must be 0, 1 or 2 legs won.")
            
            
    def print_players_in_team(self, team):
        players_in_team = self.logic_wrapper.get_all_players_of_team(team)
        print()
        for i, player in enumerate(players_in_team, 1):
            print(f"{i}. {player.name}")
        print()
        return players_in_team

            

            

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