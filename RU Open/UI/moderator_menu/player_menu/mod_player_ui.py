from logic.player_logic import Player_Logic
from model.player import Player
from ui.input_validators import *
from ui.print_layouts import *


class Player_UI:
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
                return
            elif command == "q":
                print("Goodbye")
                return "q"
            elif command == "1":
                players = self.logic_wrapper.get_all_players()
                teams = self.logic_wrapper.team_id_for_player()
                view_players(players, teams)
            elif command == "2":
                self.edit_player()
            else:
                print("invalid input, try again")


    def edit_player(self):
        return_command = ""
        player_selected_by_id = False
        while True:
            if return_command != "back":
                print_enter_name_to_edit()
                player_selected_by_id = False
                all_players = self.logic_wrapper.get_all_players()
                print_name_players(all_players)
                name = input("Please enter the name of the player you want to edit: ")
                player_name_list = self.logic_wrapper.get_player_by_name(name)
                if name == 'b':
                    print("Going back")
                    return
            else:
                return_command = ""
                
            if len(player_name_list) != 0 and player_selected_by_id == False:
                selection = self.print_players(player_name_list)

                try:
                    selection = int(selection)
                    if selection <= len(player_name_list):
                        player_to_edit = player_name_list[int(selection)-1]
                        player_selected_by_id = True
                except :
                    print("The player id you entered is invalid, please try again.")
                    return_command = "back"
            else:
                print("Name does not exist in our database, plase try again")
                
            if player_selected_by_id == True:
                print_player_edit_menu(player_to_edit)
                return_command, player_selected_by_id = self.edit_player_menu(player_to_edit, player_selected_by_id) 

    def print_players(self, player_name_list):
        print("{:<18}{:<20}{}".format("Player ID", "Player Name", "SSN"))
        for i, player in enumerate(player_name_list):
            print("{:<15}{:<17}{}".format(i+1, player.name, player.ssn))
        return input("Select player by id: ")        
    
            
                
                
    def edit_player_menu(self, player: classmethod, player_selected_by_id: bool) -> str:
        edit_info = input("Enter option to edit: ")
        if edit_info == 'b':
            print("Going back")
            player_selected_by_id = False
            return "b", player_selected_by_id 
        elif edit_info == '1':
            player.name = self.change_player_name()
            self.logic_wrapper.edit_player(player)
            return "back", player_selected_by_id 
        elif edit_info == '2':
            player.ssn = self.change_player_ssn()
            self.logic_wrapper.edit_player(player)
            return "back", player_selected_by_id     
        elif edit_info == '3':
            player.phone = self.change_player_phone()
            self.logic_wrapper.edit_player(player)
            return "back", player_selected_by_id     
        elif edit_info == '4':
            player.email = self.change_player_email()
            self.logic_wrapper.edit_player(player)
            return "back", player_selected_by_id     
        elif edit_info == '5':
            player.address = self.change_player_address()
            self.logic_wrapper.edit_player(player)
            return "back", player_selected_by_id     
            
    def change_player_name(self):
        """Asks for player name until it's valid

        Returns:
            str: name of player
        """
        while True:
            player_name = input("Enter the name of the player(max 30 char): ")
            try:
                validate_name(player_name)
                break
            except NameLengthException:
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
