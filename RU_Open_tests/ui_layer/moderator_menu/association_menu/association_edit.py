from model.association_model_dummy import Association
from model.team_model_dummy import Team
from model.player_model_dummy import Player
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import *
from input_validators import *


class Associations_UI:
    Menu_selection = {"Current Menu": "Associations", 
                    "Add team": ">>> Shows statistics of all players",
                    "Remove team": ">>> Shows statistics of all players",
                    "Edit Association Details": ">>> Shows statistics of all players",
                    "Remove Association": ">>> Shows statistics of all players"}    
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
            if command == "b":
                return
            if command == "q":
                print("Goodbye")
                return "q"
            elif command == "1":
                team = Team()
                while True:
                    team.team_name = input("Enter the name of the team: ")
                    try:
                        validate_team_name(team.team_name)
                        break
                    except TeamNameLengthException:
                        print("name was too short or too long (Must be 3-35 characters long.")
                    except:
                        print("some error")
                team.association_name = input("Enter the name of the association this team should belong to: ")
                team.captain_name = input("Enter the name of the teams captain: ")
                self.logic_wrapper.create_team(team)
                print("You must now add 4 players to the team to make it valid, otherwise the team will be deleted.")
                continue_or_no = input("Would you like to continue? (yes/no): ").islower()
                if continue_or_no == 'yes':
                    list_of_team_players = []                
                    while len(list_of_team_players) != 4:
                        (f"Creating player {len(list_of_team_players)}:")
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
                        player.team_id = team.id
                        self.logic_wrapper.create_player(player)
                elif continue_or_no == 'no':
                    '''Delete all players in players.csv with the teams id and then deletes the team from the teams.csv file'''
                    self.logic_wrapper.delete_team(team)
                return

