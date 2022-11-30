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
                #Here we could ask for teams playing in match as home / guest team
                #Then have a simple point register, as when filling in points for home team
                #You do not have to enter entire name, but only the number of the player.
                #That is, the list of names would appear
                #So input could be 
                #select player: 2 ----- nr. 2 would be f.x. Helgi Jóns
                #
                print("Enter name of match")
                print("A function has to be created for this to work ")
                
                # self.logic_wrapper.register_points(c)
                # self.logic_wrapper.get_points()
            
            else:
                print("invalid input, try again")