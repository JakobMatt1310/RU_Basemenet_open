from tournament_ui import Tournament
from model.team import Team
from model.player import Player
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *
from ui.input_validators import *


class Tournament_editing_UI:
    Menu_selection = {"Current Menu": "Tournament", 
                    "Add team": ">>> Choose a team to compete in the tournament",
                    "Remove team": ">>> Removes a team from the tournament",
                    "Edit Tournament Details": ">>> Make changes to details in the tournament"}    
    #Create a tournament
    #
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
                add_to_tournament = input("Please enter the name of the tournament you would like to add teams to: ")
                tournament_to_update = self.logic_wrapper.get_tournament(add_to_tournament)
                self.add_teams(tournament_to_update.id)
            elif command == "2":
                remove_from_tournament = input("Please enter the name of the tournament you would like to remove a team from: ")
                tournament_to_update = self.logic_wrapper.get_tournament(remove_from_tournament)
                self.remove_team(tournament_to_update.id)
            elif command == "3":
                self.edit_tournament()
    
    def edit_tournament(self):
        '''Brings up a mini menu to edit a tournaments details'''
        return_command = ""
        while True:
            if return_command != "back":
                tourney_to_edit = input("Please enter the name of the tournament you want to edit: ")
                tourney_to_edit = self.logic_wrapper.get_tourney(tourney_to_edit)
            else:
                return_command = ""
            if tourney_to_edit != None:
                print_edit_menu_team(tourney_to_edit)
                edit_info = input("Enter option to edit: ")
                if edit_info == 'b':
                    print("Going back")
                    return

                elif edit_info == '1':
                    tourney_to_edit.name = self.change_tourney_name(tourney_to_edit)
                    print(f"Player name changed to {tourney_to_edit.name}.")
                    return_command = "back"
                elif edit_info == '2':
                    tourney_to_edit.address = self.change_tourney_address(tourney_to_edit)
                    print(f"Player name changed to {tourney_to_edit.name}.")
                    return_command = "back"
                elif edit_info == '3':
                    tourney_to_edit.organizer = self.change_tourney_organizer(tourney_to_edit)
                    print(f"Player name changed to {tourney_to_edit.organizer}.")
                elif edit_info == '4':
                    return_command = self.change_tourney_organizer_number(tourney_to_edit)
            else:
                print("Tourney doesn't exist, try again.")

    def add_teams(self, tournament_id):
        '''Adds a team to the pool of teams competing in the chosen tournament'''
        add_another = 'yes'
        while add_another == 'yes':
            team_to_add = input("Please enter the name of the team you want to add to the tournament: ")
            teams_list = self.logic_wrapper.get_teams_by_name(team_to_add)
            
            id_list = []
            print("{:<18}{:<20}{}".format("Team ID", "Team Name"))
            for team in teams_list:
                print("{:<15}{:<17}".format(team.id, team.name))
                id_list.append(team.id)
            if len(id_list) == 1:
                selection = id_list[0]
                team_to_add = self.logic_wrapper.get_team(selection)
                self.logic_wrapper.add_team_to_tourney(tournament_id, team_to_add.id)
                add_another = ("Would you like to add another team? (yes/no): ")
            else:  
                selection = input("Select team by id: ")
                if selection == 'b':
                    print("Going back")
                    return
                elif selection in id_list:
                    team_to_add = self.logic_wrapper.get_team(selection)
                    break
                else:
                    ("The team id you entered is invalid, please try again.")

    def remove_team(self, tournament_id):
        '''Removes a team from the chosen tournament'''
        while True:
            team_to_remove = input("Please enter the name of the team you want to remove from the tournament: ")
            teams_list = self.logic_wrapper.get_teams_by_name(team_to_remove)
        
            id_list = []
            print("{:<18}{:<20}{}".format("Team ID", "Team Name"))
            for team in teams_list:
                print("{:<15}{:<17}".format(team.id, team.name))
                id_list.append(team.id)
            if len(id_list) == 1:
                selection = id_list[0]
                team_to_remove = self.logic_wrapper.get_team(selection)
                self.logic_wrapper.remove_team_from_tourney(tournament_id, team_to_remove.id)
                break
            else:  
                selection = input("Select team by id: ")
                if selection == 'b':
                    print("Going back")
                    return
                elif selection in id_list:
                    team_to_remove = self.logic_wrapper.get_team(selection)
                    break
                else:
                    ("The team id you entered is invalid, please try again.")

    def change_tourney_name(self):
        """Asks for tournament name until it's valid

        Returns:
            str: name of player
        """
        while True:
            tourney_name = input("Enter the name of the player(max 30 char): ")
            try:
                validate_name(tourney_name)
                break
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return tourney_name

    def change_tourney_address(self):
        """Asks for a valid tournament address, requirements are atleast 1 digit at end of address
        If it has a letter for ending, checks if second last is digit, example Street 2B

        Returns:
            str: Tournament address
        """
        while True:
            address = input("Enter the address where the tournament will take place: ")
            try: 
                validate_home_address(address)
                break
            except HomeAddressException:
                print("Invalid input, Please try again")
            except:
                print("Something went wrong, please try again.")
        return address

    def change_tourney_organizer(self):
        """Asks for organizer name until it's valid

        Returns:
            str: name of player
        """
        while True:
            organizer_name = input("Enter the name of the organizer(max 30 char): ")
            try:
                validate_name(organizer_name)
                break
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return organizer_name

    def change_organizer_number(self):
        """Asks for organizer phonenumber until it's a valid phone number

        Returns:
            str: Organizers phonenumber
        """
        while True:
            organizer_number = input("Enter the organizers new phone number: ")
            try:
                validate_phonenumber(organizer_number)
                break
            except PhoneNumberException:
                print("Input incorrect, please try again.")
            except:
                print("Something went wrong, please try again.")
        return organizer_number