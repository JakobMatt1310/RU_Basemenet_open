from model.player_model_dummy import Player
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import *


class Statistics_UI:
    Menu_selection = {"Current Menu": "Statistics", 
                    "View Players Statistics": ">>> Shows statistics of all players", 
                    "View Team Statistics": ">>> Shows wins and total QP's within the team"}    
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
                print("Statistics hérna um leikmenn")
                input()
                return
                # players_result = self.logic_wrapper.get_player_statistics()
                # view_player_stats(players_result)
            elif command == "2":
                print("Statistics hérna um lið")
                input()
                return
                # team_result = self.logic_wrapper.get_team_statistics()
                # view_team_stats(team_result)
                
            else:
                print("invalid input, try again")