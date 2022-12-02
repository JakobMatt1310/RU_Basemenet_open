from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import print_current_menu
from model.team_model_dummy import Team
from input_validators import *

class Teams_UI:
    Menu_selection = {"Current Menu": "Team Menu", 
                    "Create Team": ">>> Create a team within a chosen association", 
                    "Edit Team": ">>> Gives the user options to make changes to the team", 
                    "View Teams": ">>> Shows the list of every team below their respected associations"}    
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

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
                team = Team()
                while True:
                    team.team_name = input("Enter the name of the player: ")
                    try:
                        validate_team_name(team.name)
                        break
                    except TeamNameLengthException:
                        print("name was too long")
                    except:
                        print("some error")
                team.association_name = input("Enter the association this team should belong to: ")
                team.captain_name = input("Enter the name of the teams captain: ")
                team.team_players = input("Enter the players email address: ")
                self.logic_wrapper.create_team(team)
                
            elif command == "2":
                
                
                    return "q"
            else:
                print("invalid input, try again")
                