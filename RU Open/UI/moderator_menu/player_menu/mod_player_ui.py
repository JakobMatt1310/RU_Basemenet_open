from logic.player_logic import Player_Logic
from model.player import Player
from ui.input_validators import *
from print_layouts import *


class Mod_Player_UI:
    Menu_selection = {"Current Menu": "Player Menu", 
                    "View Players": ">>> Shows a list of all the players", 
                    "Edit Player": ">>> Gives options to edit a players details"
                    }   
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.Menu_selection)
    
    def input_prompt(self):
        while True:
            self.menu_output()
            command= input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("going back")
                return "b"
            elif command == "q":
                print("quitting")
            elif command == "1":
                self.logic_wrapper.get_all_players()
            else:
                print("invalid input, try again")

    def edit_player(self):
        return_command = ""
        while True:
            if return_command != "back":
                player_to_edit = input("Please enter the name of the player you want to edit: ")
                players_with_name = self.logic_wrapper.get_players_by_name(player_to_edit)
                count = 1
                id_list = []
                print("{:<18}{:<20}{}".format("Player ID", "Player Name", "SSN"))
                for player in players_with_name:
                    print("{}. {:<15}{:<17}{}".format(count, player.id, player.name, player.ssn))
                    id_list.append(player.id)
                    count+=1
                selection = input("Select player by id: ")
                if selection == 'b':
                    print("Going back")
                    return
                elif selection in id_list:
                    player_to_edit = self.logic_wrapper.get_player(selection)
                    break
                else:
                    ("The player id you entered is invalid, please try again.")
                
                
            else:
                return_command = ""
            if player_to_edit != None:
        #-----------------Vantar Print Menu-----------------#
                #print_player_edit_menu(player_to_edit)
                edit_info = input("Enter option to edit: ")
                if edit_info == 'b':
                    print("Going back")
                    return
                elif edit_info == '1':
                    player_to_edit.name = self.change_player_name(player_to_edit)
                    print(f"Player name changed to {player_to_edit.name}.")
                    return_command = "back"
                elif edit_info == '2':
                    player_to_edit.ssn = self.change_player_ssn(player_to_edit)
                    print(f"Player name changed to {player_to_edit.ssn}.")
                    return_command = "back"
                elif edit_info == '3':
                    player_to_edit.phone = self.change_player_phone(player_to_edit)
                    print(f"Player phone number changed to {player_to_edit.phone}.")
                    return_command = "back"
                elif edit_info == '4':
                    player_to_edit.email = self.change_player_email(player_to_edit)
                    print(f"Player email changed to {player_to_edit.email}")
                    return_command = "back"
                elif edit_info == '5':
                    player_to_edit.address = self.change_player_address(player_to_edit)
                    print(f"Player address changed to {player_to_edit.address}")
                    return_command = "back"
            else:
                print("Player doesn't exist, try again.")
    
    def change_player_name(self, player_to_edit):
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
    
    def change_player_ssn(self):
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

    def change_player_phone(self):
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
                print("Invalid length of name, must be 3-30 characters long. Please try again.")
            except:
                print("Something went wrong, please try again.")
        return phone_number
    
    def change_player_email(self):
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
    
    def change_player_address(self):
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
