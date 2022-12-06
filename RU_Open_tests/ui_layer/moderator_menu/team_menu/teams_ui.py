from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import print_current_menu
from model.team_model_dummy import Team
from input_validators import *

class Teams_UI:
    Menu_selection = {"Current Menu": "Team Menu", 
                    "Create Team": ">>> Create a team within a chosen association", 
                    "Edit Team": ">>> Gives the user options to make changes to the team", 
                    "View Teams": ">>> Shows the list of every team below their respected associations",
                    "Delete Team": ">>> Removes a team and it's players"}    
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
                list_of_teams = self.logic_wrapper.get_all_teams()
                team_to_edit = input("Please enter the name of the team you want to edit: ")
                if team_to_edit in list_of_teams:
                    edit_info = input("What details would you like to make changes to? (1. Edit Team Name // 2. Change Association // 3. Change Captains): ").islower()
                    if edit_info == '1':
                        new_team_name = input("Please enter a new name for the team: ")
                        confirm_name = input(f"The team will be renamed {new_team_name}. Confirm (yes/no): ").islower()
                        while True:
                            if confirm_name == 'yes':
                                team_to_edit.team_name = new_team_name
                                break
                            elif confirm_name =='no':
                                print("No changes made, returning to editing menu.")
                                break
                            else:
                                print('Invalid input, please answer with "yes" or "no"')
                    elif edit_info == '2':
                        while True:
                            new_association_name = input("Please enter the association you would like to transfer this team to: ")
                            association_list = self.logic_wrapper.get_all_associations()
                            if new_association_name in association_list:
                                confirm_association = input(f"The name of the association the team should transfer to is {new_association_name}. Confirm (yes/no): ").islower()
                                while True:
                                    if confirm_association == 'yes':
                                        new_association = get_association(new_association_name)
                                        team_to_edit.association_id = new_association.id
                                        break
                                    elif confirm_association =='no':
                                        print("No changes made, returning to editing menu.")
                                        break
                                    else:
                                        print('Invalid input, please answer with "yes" or "no"')
                            else:
                                print("Association does not exist, please enter the name of an existing association.")
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
                    print("Team does not exist, please enter the name of a team that exists.")
                
            elif command == "q":
                return "q"
            else:
                print("invalid input, try again")
                