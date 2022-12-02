from model.player_model_dummy import Player
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import print_current_menu
from model.team_model_dummy import Team
from logic_layer.player_logic import Player_Logic
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
                    team.team_name = input("Enter the name of the team: ")
                    try:
                        validate_team_name(team.team_name)
                        break
                    except TeamNameLengthException:
                        print("name was too long")
                    except:
                        print("some error")
                team.association_name = input("Enter the name of the association this team should belong to: ")
                team.captain_name = input("Enter the name of the teams captain: ")
                self.logic_wrapper.create_team(team)
                ask_to_create_players = input("Would you like to add players to this team(yes/no)?: ")
                if ask_to_create_players == 'yes':
                    add_another = 'yes'
                    while add_another == 'yes':
                        new_or_existing = input("Would you like create a new player or add an existing player (new/ex)?: ")
                        if new_or_existing == 'new':
                            player = Player()
                            while True:
                                player.name = input("Enter the name of the player: ")
                                try:
                                    validate_name(player.name)
                                    break
                                except NameLengthException:
                                    print("name was too long")
                                except:
                                    print("some error")
                            player.ssn = input("Enter the social security number of the player: ")
                            player.phone = input("Enter the players phone number: ")
                            player.email = input("Enter the players email address: ")
                            player.address = input("Enter the players home address: ")
                            player.team_id = input("Enter the id of the team this player should play for: ")
                            self.logic_wrapper.create_player(player)
                        else:
                            pass
                            #list players with no team id
                            #existing_player = input("the id of the player you would like to add to the team: ")
            elif command == "2":
                
                
                    return "q"
            else:
                print("invalid input, try again")
                