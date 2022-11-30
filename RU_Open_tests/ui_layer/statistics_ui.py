from player_model_dummy import Player
from moderator_ui import Moderator_UI
from player_ui import Player_UI
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import print_current_menu


class Statistics_UI:
    Menu_selection = {"Current Menu": "Statistics", 
                    "View Players Statistics": ">>> Shows the statistics of the chosen player", 
                    "View Team Statistics": ">>> Shows the winrate and total quality points within the team", 
                    "": ">>> "}    
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                menu = Moderator_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                menu = Player_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            else:
                print("invalid input, try again")
                

test = MainMenu_UI()
test.input_prompt()