from tournament_ui import Tournament
from Model.team import Team
from Model.player import Player
from Logic.logic_wrapper import Logic_Wrapper
from UI.print_layouts import *
from UI.input_validators import *


class Tournament_editing_UI:
    Menu_selection = {"Current Menu": "Tournament", 
                    "Add team": ">>> Creates a team within the tournament",
                    "Remove team": ">>> Removes a team from the tournament",
                    "Edit Tournament Details": ">>> Make changes to details in the tournament"}    
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
                team.tournament_name = input("Enter the name of the tournament this team should belong to: ")
                team.captain_name = input("Enter the name of the teams captain: ")
                self.logic_wrapper.create_team(team)
                print("You must now add 4 players to the team to make it valid, otherwise the team will be deleted.")
                continue_or_no = input("Would you like to continue? (yes/no): ").lower()
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
            elif command == '2':
                list_of_teams = self.logic_wrapper.get_all_teams()
                team_to_delete = input("Please enter the name of the team that you want to remove: ")
                if team_to_delete in list_of_teams:
                    print("Removing this team will delete all players within the association.")
                    confirm = input("Are you sure you want to remove this team? (yes/no)").lower()
                    while True:
                        if confirm == 'yes':
                            self.logic_wrapper.remove_team(team_to_delete)
                            break
                        elif confirm == 'no':
                            print("No action was performed, the team will stay active.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no" ')
            elif command == '3':
                association_name = input("Please enter the new name of the association you want to make changes to: ")
                association_to_change = self.logic_wrapper.get_association(association_name)
                edit_info = input("What details would you like to make changes to? (1. Tournament Name // 2. Address): ").lower()
                if edit_info == '1':
                    new_tournament_name = input("Please enter a new name for the tournament: ")
                    confirm_name = input(f"The association will be renamed {new_tournament_name}. Confirm (yes/no): ").lower()
                    while True:
                        if confirm_name == 'yes':
                            tournament_to_change.tournament_name = new_tournament_name
                            break
                        elif confirm_name =='no':
                            print("No changes made, returning to editing menu.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no"')
                elif edit_info == '2':
                    new_tournament_number = input("Please enter a new phone number for the tournament: ")
                    confirm_number = input(f"The new phone number of the tournament will be {new_tournament_number}. Confirm (yes/no): ").lower()
                    while True:
                        if confirm_number == 'yes':
                            tournament_to_change.tournament_phone = new_tournament_number
                            break
                        elif confirm_number =='no':
                            print("No changes made, returning to editing menu.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no"')
                elif edit_info == '3':
                    while True:
                        new_tournament_address = input("Please enter a new address for the tournament: ")
                        confirm_address = input(f"The new tournament address will be {new_tournament_address}. Confirm (yes/no): ").lower()
                        if confirm_address == 'yes':
                            tournament_to_change.tournament_address = new_tournament_address
                            break
                        elif confirm_address =='no':
                            print("No changes made, returning to editing menu.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no"')

            else:
                print("Invalid input, please try again.")
