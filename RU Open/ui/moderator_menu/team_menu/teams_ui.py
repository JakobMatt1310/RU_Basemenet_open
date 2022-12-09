from model.player import Player
import time
from ui.print_layouts import (  print_current_menu, 
                                print_current_team_player_list, 
                                view_teams, 
                                print_edit_menu_team )
from model.team import Team
from ui.input_validators import *

class Teams_UI:
    Menu_selection = {"Current Menu": "Team Menu", 
                    "Create Team": ">>> Create a team within a chosen association", 
                    "Edit Team": ">>> Select to edit team", 
                    "View Teams": ">>> Lists all teams"}    
                    # "View Teams": ">>> Shows the list of every team below their respected associations"}    
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

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
                self.create_new_team()
            elif command == "2":
                self.edit_a_team()
            elif command == "3":
                teams_all = self.logic_wrapper.get_all_teams()
                view_teams(teams_all)
            elif command == "q":
                return "q"
            else:
                print("invalid input, try again")

    def edit_a_team(self):
        return_command = ""
        while True:
            if return_command != "back":
                team_to_edit = input("Please enter the name of the team you want to edit: ")
                team_to_edit = self.logic_wrapper.get_team(team_to_edit)
            else:
                return_command = ""
            if team_to_edit != None:
                print_edit_menu_team(team_to_edit)
                edit_info = input("Enter option to edit: ")
                if edit_info == 'b':
                    print("Going back")
                    return
                elif edit_info == '1':
                    return_command = self.change_team_name(team_to_edit)
                elif edit_info == '2':
                    return_command = self.change_team_association(team_to_edit)
                elif edit_info == '3':
                    return_command = self.edit_team_captain(team_to_edit)
            else:
                print("Team doesn't exist, try again.")
                
    def change_team_name(self, team_to_edit):    
        new_team_name = self.new_team_name(1)
        confirm_name = input(f"The team will be renamed {new_team_name}. Would you like to confirm (yes/no)?  ").lower()
        while True:
            if confirm_name == 'yes':
                team_to_edit.team_name = new_team_name
                success = self.logic_wrapper.update_team_name(team_to_edit)
                if success == True:
                    print(f"Team name has successfully been updated to {new_team_name}")
                    input("Press enter to return: ")
                    return "back"
                else:
                    print("Team name failed to update, try again or go back")
            elif confirm_name =='no':
                return self.back_command()
            else:
                print('Invalid input, please answer with "yes" or "no"')
    
          
    def change_team_association(self, team_to_edit):
        while True:
            all_associations = self.logic_wrapper.get_all_associations()
            for i, association in enumerate(all_associations, 1):
                print(f"{i}. {association.association_name}")
            while True:
                selection = input("Please enter the number of the new association: ")
                if selection.isdigit() == False:
                    if new_association == 'b':
                        print("---------------------------------------------")
                        print("No changes made, returning to editing menu.")
                        print("---------------------------------------------")
                        time.sleep(2.0)
                        return "cancel"
                    else:
                        print(f"Invalid input, please enter a number within 1 to {len(all_associations)} or c to cancel")
                else:
                    if 0 < int(selection) <= len(all_associations):
                        new_association = all_associations[int(selection) - 1]
                        confirm_association = input(f"Change team association to -> {new_association.association_name}. Confirm (yes/no): ").lower()
                        if confirm_association == 'yes':
                            team_to_edit.association_id, team_to_edit.association_name = new_association.id, new_association.association_name
                            self.logic_wrapper.update_team_association(team_to_edit)
                            return "back"
                        elif confirm_association =='no':
                            return self.back_command()
                    else:
                        print(f"Invalid input, please enter a number within 1 to {len(all_associations)} or c to cancel")
                
    def edit_team_captain(self, team_to_edit):
        players_in_team = self.logic_wrapper.get_all_players_of_team(team_to_edit)
        for i, player in enumerate(players_in_team, 1):
            print(f"{i}. {player.name}")
        while True:
            new_captain = input("Please enter the player number for new captain role. ")
            if new_captain.isdigit() == False:
                if new_captain == 'b':
                    return self.back_command()
                else:
                    print(f"Invalid input, please enter a number within 1 to {len(players_in_team)} or c to cancel")
            else:
                if 0 < int(new_captain) <= len(players_in_team):
                    new_captain = players_in_team[int(new_captain)-1].name
                    team_to_edit.captain_name = new_captain
                    success = self.logic_wrapper.update_team_captain(team_to_edit)
                    if success == True:
                        print(f"Team captain has successfully been updated to {new_captain}")
                        input("Press enter to return: ")
                        return "back"
                    else:
                        print("Team name failed to update, try again. ")
                
                else:
                    print(f"Invalid input, please enter a number within 1 to {len(players_in_team)} or c to cancel")
                

    def create_new_team(self):
        """Creates a new team, when selected Moderator HAS to create a team, with all four players and a captain.
        """
        team = Team()
        team.team_name = self.new_team_name()
        team.association_name = self.association_name()
        
        self.logic_wrapper.create_team(team)
        print_current_team_player_list([" "], team.team_name)
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
            print_current_team_player_list(player_list, team.team_name)
            
        while True:
            selection = input("Select player to be captain for team: ")
            if selection == "1" or selection == "2" or selection == "3" or selection == "4":
                team.captain_name = player_list[int(selection)-1]
                success = self.logic_wrapper.update_team_captain(team)
                if success == True:
                    return "back"
                else:
                    print("Team not found, an error has occoured")
                    return
            else:
                print("Invalid input, please try again (A captain must be chosen)")

    def new_team_name(self, rename=0):
        while True:
            if rename == 0:            
                team_name = input("Enter the name of the team (max 30 char): ")
            else:
                team_name = input("Enter the desired new name for the team (max 30 char): ")
            try:
                validate_team_name(team_name)
                break
            except TeamNameLengthException:
                print("Name was too long or to short")
            except:
                print("Something went wrong, please try again.")
        return team_name
                
    def association_name(self):
        while True:
            association_name = input("Enter the association this team should belong to (max 30 char): ")
            try:
                validate_association_name(association_name)
                test = self.logic_wrapper.validate_association_name_with_all(association_name)
                if test == True:
                    break
                else:
                    print("Name already exists, please choose another name")
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return association_name


#---------------Player validation-------------------#


    def new_player_name(self):
        """Asks for player name until it's valid

        Returns:
            str: name of player
        """
        while True:
            player_name = input("Enter the name of the player(max 30 char): ")
            try:
                validate_name(player_name)
                break
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return player_name
    
    def new_player_ssn(self):
        """Asks for player social security number until it's valid

        Returns:
            str: Social security number for player
        """
        while True:
            ssn = input("Enter the social security number of the player: ")
            try:
                validate_ssn(ssn)
                check = self.logic_wrapper.check_if_player_exists(ssn)
                if check == False:
                    break
                else:
                    print(f"Player {check.name} already exists, try again")
            except SsnLengthException:
                print("Input incorrect, please try again.")
            # except:
            #     print("Something went wrong, please try again.")
        return ssn
    
    def new_player_phone(self):
        """Asks for player phonenumber until it's a valid phone number

        Returns:
            str: Players phonenumber
        """
        while True:
            phone_number = input("Enter the players phone number: ")
            try:
                validate_phonenumber(phone_number)
                break
            except TeamNameLengthException:
                print("Input incorrect, please try again.")
            except:
                print("Something went wrong, please try again.")
        return phone_number
    
    def new_player_email(self):
        """Asks for player email address, asks until it's valid

        Returns:
            str: Players email address
        """
        while True:
            email = input("Enter the players email address: ")
            try: 
                validate_email(email)
                break
            except InvalidEmailException:
                print("Invalid input, please try again")
            except:
                print("Something went wrong, please try again.")
        return email
    
    def new_player_address(self):
        """Asks for a valid home address, requirements are atleast 1 digit at end of address
        If it has a letter for ending, checks if second last is digit, example Street 2B

        Returns:
            str: Players streed address
        """
        while True:
            address = input("Enter the players home address: ")
            try: 
                validate_home_address(address)
                break
            except HomeAddressException:
                print("Invalid input, Please try again")
            except:
                print("Something went wrong, please try again.")
        return address           

#---------------------------------------------------#

    def back_command(self):
        print("---------------------------------------------")
        print("No changes made, returning to editing menu.")
        print("---------------------------------------------")
        time.sleep(2.0)
        return "back"
      


