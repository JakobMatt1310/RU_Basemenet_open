from model.association import Association
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
                self.add_team_to_association()
            elif command == '2':
                self.delete_team_from_association()
            elif command == '3':
                association = input("Please enter the new name of the association you want to make changes to: ")
                association_to_change = self.logic_wrapper.get_association(association)
                edit_info = input("What details would you like to make changes to? (1. Association Name // 2. Phone Number // 3. Address): ").islower()
                if edit_info == '1':
                    self.change_association_name(association_to_change)
                elif edit_info == '2':
                    self.change_association_number(association_to_change)
                elif edit_info == '3':
                    self.change_association_address(association_to_change)
            else:
                print("Invalid input, please try again.")
    
    def add_team_to_association(self):
        team = Team()
        team.name = self.new_team_name()
        team.association = self.association_name()
        
        self.logic_wrapper.create_team(team)
        print_current_team_player_list([" "], team.name)
        player_list = []
        for i in range(4): # Moderator has to create 4 players and select a captain
            player = Player()
            player.ssn = self.new_player_ssn()
            player.name = self.new_player_name()
            player.phone = self.new_player_phone()
            player.email = self.new_player_email()
            player.address = self.new_player_address()
            player.team_id = team.id
                        
            self.logic_wrapper.create_player(player)
            player_list.append(player.name)
            print_current_team_player_list(player_list, team.name)
            
        while True:
            selection = input("Select player to be captain for team: ")
            if selection == "1" or selection == "2" or selection == "3" or selection == "4":
                team.captain = player_list[int(selection)-1]
                success = self.logic_wrapper.update_team_captain(team)
                if success == True:
                    return "back"
                else:
                    print("Team not found, an error has occoured")
                    return
            else:
                print("Invalid input, please try again (A captain must be chosen)")

    def new_team_name(self):
        while True:            
            team = input("Enter the name of the team (max 30 char): ")
            try:
                validate_team_name(team)
                break
            except TeamNameLengthException:
                print("Name was too long or to short")
            except:
                print("Something went wrong, please try again.")
        return team
    
    def association_name(self):
        while True:
            association = input("Enter the association this team should belong to (max 30 char): ")
            try:
                validate_association_name(association)
                test = self.logic_wrapper.validate_association_name_with_all(association)
                if test == True:
                    break
                else:
                    print("Name already exists, please choose another name")
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return association
            
    def delete_team_from_association(self):
        list_of_teams = self.logic_wrapper.get_all_teams()
        team_to_delete = input("Please enter the name of the team that you want to remove: ")
        if team_to_delete in list_of_teams:
            print("Removing this team will delete all players within the team.")
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
                    confirm = input("Are you sure you want to remove this team? (yes/no)").islower()

    def change_association_name(self, association_to_change):
        new_association = input("Please enter a new name for the association: ")
        confirm_name = input(f"The association will be renamed {new_association}. Confirm (yes/no): ").islower()
        while True:
            if confirm_name == 'yes':
                association_to_change.association_name = new_association
                self.logic_wrapper.update_association_name(association_to_change)
                break
            elif confirm_name =='no':
                print("No changes made, returning to editing menu.")
                break
            else:
                print('Invalid input, please answer with "yes" or "no"')
                confirm_name = input(f"The association will be renamed {new_association}. Confirm (yes/no): ").islower()
    
    def change_association_number(self, association_to_change):
        new_association_number = input("Please enter a new phone number for the association: ")
        confirm_number = input(f"The new phone number of the association will be {new_association_number}. Confirm (yes/no): ").islower()
        while True:
            if confirm_number == 'yes':
                association_to_change.association_phone = new_association_number
                self.logic_wrapper.update_association_phone(association_to_change)
                break
            elif confirm_number =='no':
                print("No changes made, returning to editing menu.")
                break
            else:
                print('Invalid input, please answer with "yes" or "no"')
                confirm_number = input(f"The new phone number of the association will be {new_association_number}. Confirm (yes/no): ").islower()
    
    def change_association_address(self, association_to_change):
        while True:
            new_association_address = input("Please enter a new address for the association: ")
            confirm_address = input(f"The new association address will be {new_association_address}. Confirm (yes/no): ").islower()
            if confirm_address == 'yes':
                association_to_change.association_address = new_association_address
                self.logic_wrapper.update_association_address(association_to_change)
                break
            elif confirm_address =='no':
                print("No changes made, returning to editing menu.")
                break
            else:
                print('Invalid input, please answer with "yes" or "no"')
                confirm_address = input(f"The new association address will be {new_association_address}. Confirm (yes/no): ").islower()
    
