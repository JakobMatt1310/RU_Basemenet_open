# from logic.player_logic import Player_Logic
from player_model_dummy import Player
from input_validators import *
from print_layouts import print_current_menu


class Captain_UI:
    
    player_menu = {"Current Menu": "Captain options", 
                   "Register points": ">>> Select to register points for finished game"}
    
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.player_menu)
    
    def input_prompt(self):
        while True:
            self.menu_output()
            command= input("Enter your command: ")
            command = command.lower()
            if command == "b":
                return
            elif command == "q":
                print("Quitting")
                return "q"
            elif command == "1":
                print("A function has to be created for this to work ")
                self.logic_wrapper.create_player(c)
            elif command == "2":
                result = self.logic_wrapper.get_all_players()
                for elem in result:
                    print(f"Name: {elem.name}, SSN: {elem.ssn}, Phone number: {elem.phone}, Email: {elem.email}, Home address: {elem.address}")
            else:
                print("invalid input, try again")