from player_model_dummy import Player
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import *


class Statistics_UI:
    Menu_selection = {"Current Menu": "Statistics", 
                    "View Teams": ">>> Shows the list of every team in our database"}    
    
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("Going back")
                break
            elif command == "1":
                result = self.logic_wrapper.get_all_teams()
                view_teams(result)
                    
            else:
                print("invalid input, try again")
                