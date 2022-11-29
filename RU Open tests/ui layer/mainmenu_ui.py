

from logic.player_logic import Player_Logic
from model.player import Player
from uilayer import Player_UI
from logic.logic_wrapper import Logic_Wrapper



class MainMenu_UI:
    Menu_selection = {"Current Menu": "Main Menu", 
                    "Moderator": ">>> Select Moderator to create and/or edit", 
                    "Player": ">>> Select player to register new points", 
                    "Teams": ">>> Select teams to view all registered teams", 
                    "Association": ">>> View all registered associations", 
                    "Statistics": ">>> View statistics for teams and players", 
                    "Tournaments": ">>> View all registered yournaments"}    
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("{}".format("Main Menu"))
        print("{}".format("1. Player Menu"))
        print("{}".format("2. Associations Menu"))
        print("{}".format("q. to exit"))

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                menu = Player_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                pass
            else:
                print("invalid input, try again")
                
