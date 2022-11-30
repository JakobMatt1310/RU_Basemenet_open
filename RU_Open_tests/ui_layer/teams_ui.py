from player_model_dummy import Player
from print_layouts import *


class Teams_View_UI:
    Menu_selection = {"Current Menu": "Team Menu", 
                    "View Teams": ">>> Shows the list of every team in our database"}    
    
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection()

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
            if command == "b":
                print("Going back")
                break
            elif command == "1":
                result = self.logic_wrapper.get_all_teams()
                view_teams(result)
                    
            else:
                print("invalid input, try again")
                