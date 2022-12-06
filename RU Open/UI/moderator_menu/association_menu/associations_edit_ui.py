from association import Association
from model.team import Team
from model.player import Player
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *
from ui.input_validators import *


class Associations_editing_UI:
    Menu_selection = {"Current Menu": "Associations", 
                    "Add team": ">>> Creates a team within the association",
                    "Remove team": ">>> Removes a team from the association",
                    "Edit Association Details": ">>> Make changes to details in the association"}    
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
            elif command == '2':
                list_of_teams = self.logic_wrapper.get_all_teams()
                team_to_delete = input("Please enter the name of the team that you want to remove: ")
                if team_to_delete in list_of_teams:
                    print("Removing this team will delete all players within the association.")
                    confirm = input("Are you sure you want to remove this team? (yes/no)").islower()
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
                edit_info = input("What details would you like to make changes to? (1. Association Name // 2. Phone Number // 3. Address): ").islower()
                if edit_info == '1':
                    new_association_name = input("Please enter a new name for the association: ")
                    confirm_name = input(f"The association will be renamed {new_association_name}. Confirm (yes/no): ").islower()
                    while True:
                        if confirm_name == 'yes':
                            association_to_change.association_name = new_association_name
                            break
                        elif confirm_name =='no':
                            print("No changes made, returning to editing menu.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no"')
                elif edit_info == '2':
                    new_association_number = input("Please enter a new phone number for the association: ")
                    confirm_number = input(f"The new phone number of the association will be {new_association_number}. Confirm (yes/no): ").islower()
                    while True:
                        if confirm_number == 'yes':
                            association_to_change.association_phone = new_association_number
                            break
                        elif confirm_number =='no':
                            print("No changes made, returning to editing menu.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no"')
                elif edit_info == '3':
                    while True:
                        new_association_address = input("Please enter a new address for the association: ")
                        confirm_address = input(f"The new association address will be {new_association_address}. Confirm (yes/no): ").islower()
                        if confirm_address == 'yes':
                            association_to_change.association_address = new_association_address
                            break
                        elif confirm_address =='no':
                            print("No changes made, returning to editing menu.")
                            break
                        else:
                            print('Invalid input, please answer with "yes" or "no"')

            else:
                print("Invalid input, please try again.")
