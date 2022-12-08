from logic.player_logic import Player_Logic
from model.player import Player
from ui.input_validators import *
from print_layouts import *


class Player_UI:
    Menu_selection = {"Current Menu": "Player Menu", 
                    "View Players": ">>> Shows a list of all the players", 
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
                players_with_name = self.logic_wrapper.get_player(player_to_edit)
                for player in players_with_name:
                    print(player.name, player.id)
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
                    return_command = self.change_player_name(player_to_edit)
                    player_to_edit.name = self.new_player_name()
                elif edit_info == '2':
                    return_command = self.change_player_ssn(player_to_edit)
                elif edit_info == '3':
                    return_command = self.change_player_phone(player_to_edit)
                elif edit_info == '4':
                    return_command = self.change_player_email(player_to_edit)
                elif edit_info == '5':
                    return_command = self.change_player_address(player_to_edit)
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
    
