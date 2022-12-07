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
