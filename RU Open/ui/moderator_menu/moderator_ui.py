# from logic.player_logic import Player_Logic
from ui.moderator_menu.team_menu.teams_ui import Teams_UI
from model.player import Player
from ui.input_validators import *
from ui.print_layouts import print_current_menu

class Moderator_UI:
    Moderator_menu = {"Current Menu": "Moderator Menu", 
                    "Tournament Options": ">>> Register or edit tournaments",
                      "Teams options": ">>> Register or edit teams ",
                      "Associations option":">>> Register or edit associations",
                      "Player options": ">>> Edit players"}
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.Moderator_menu)
    
    def input_prompt(self):
        while True:
            self.menu_output()
            command= input("Enter your command: ").lower()
            if command == "b":
                return
            elif command == "q":
                print("quitting")
                return "q"
            elif command == "1":
                pass
            elif command == "2":
                menu = Teams_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "3":
                pass
            elif command == "4":
                pass
            else:
                print("invalid input, try again")