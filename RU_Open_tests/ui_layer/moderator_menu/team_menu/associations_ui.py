from model.association_model_dummy import Association
from model.team_model_dummy import Team
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import *


class Associations_UI:
    Menu_selection = {"Current Menu": "Associations", 
                    "View Associations": ">>> Shows statistics of all players",
                    "Create Association": ">>> Shows statistics of all players",
                    "Edit Association": ">>> Shows statistics of all players",
                    "Remove Association": ">>> Shows statistics of all players"}    
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
            elif command == "1":
                print("Listi af öllum associations hérna")
                input()
                return
            elif command == "1":
                self.logic_wrapper.get_all_associations()
                return
            elif command == "2":
                association = Association()
                
                self.logic_wrapper.create_association(association)
                
            else:
                print("invalid input, try again")