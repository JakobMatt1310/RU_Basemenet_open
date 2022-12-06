from model.player import Player
from ui.print_layouts import print_current_menu, print_current_team_player_list, view_teams
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
        while True:
            team_to_edit = "Awful Tossers"#input("Please enter the name of the team you want to edit: ")
            team_to_edit = self.logic_wrapper.get_team(team_to_edit)
            if team_to_edit != None:
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
                                    new_association = self.logic_wrapper.get_association(new_association_name)
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
                        list_of_team_players = self.logic_wrapper.get_team_players(team_to_edit)
                        new_captain = input("Please enter the name of the player you would like to replace the current captain: ")
                        if new_captain in list_of_team_players:
                            team_to_edit.captain_name = new_captain
                            break
                        else:
                            print("Player not in team, please try again.")
                        

            else:
                print("Team doesn't exist, try again.")
    
    def create_new_team(self):
        team = Team()
        team.team_name = self.new_team_name()
        team.association_name = self.association_name()
        self.logic_wrapper.create_team(team)
        print_current_team_player_list([" "], team.team_name)
        for i in range(3): # moredator has to create 4 players and select a captain
            player_list = []
            player = Player()
            player.name = self.new_player_name()
            player.ssn = self.new_player_ssn()
            player.phone = self.new_player_phone()
            player.email = self.new_player_email()
            player.address = self.new_player_address()
            player.team_id = team.id
            
            self.logic_wrapper.create_player(player)
            player_list.append(player.name)
            print_current_team_player_list(player_list, team.team_name)
        while True:
            selection = input("Select player to be captain for team")
            if selection == "1" or selection == "2" or selection == "3" or selection == "4":
                team.captain_name = player_list[selection]
                break
            else:
                print("Invalid input, please try again (A captain must be chosen")

    def new_team_name(self):
        while True:
            team_name = input("Enter the name of the team (max 30 char): ")
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
                break
            except SsnLengthException:
                print("Input incorrect, please try again.")
            except:
                print("Something went wrong, please try again.")
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