from tournament_ui import Tournament
from model.team import Team
from model.player import Player
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *
from ui.input_validators import *


class Tournament_editing_UI:
    Menu_selection = {"Current Menu": "Tournament", 
                    "Add team": ">>> Creates a team within the tournament",
                    "Remove team": ">>> Removes a team from the tournament",
                    "Edit Tournament Details": ">>> Make changes to details in the tournament"}    
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
            
