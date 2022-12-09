import time
# from player_model_dummy import Player
from ui.moderator_menu.moderator_ui import Moderator_UI
from ui.moderator_menu.captain.captain_ui import Captain_UI
# from teams_ui import Teams_View_UI
# from statistics_ui import Statistics_UI
from ui.moderator_menu.tournament_menu.tournament_ui import Tournament_UI
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import print_current_menu, view_association, view_players, view_teams, print_access_denied

class MainMenu_UI:
    Menu_selection = {"Current Menu": "Main Menu", 
                    "Moderator": ">>> Select Moderator to create and/or edit", 
                    "Captain": ">>> Select player to register new points",
                    "Player": ">>> View all players registered", 
                    "Teams": ">>> Select teams to view all registered teams", 
                    "Association": ">>> View all registered associations", 
                    "Statistics": ">>> View statistics for teams and players", 
                    "Tournaments": ">>> View all registered Tournaments"}    
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print_current_menu(self.Menu_selection)
  
    def ask_for_mod_password(self):
        password = input("Please enter password: ")
        mod_password = self.logic_wrapper.get_moderator_password()
        if password == mod_password:
            return True
        return False
  
    def ask_for_captain_password(self):
        ssn = '0402781920' # input("Enter captains social security number ") <<<<<------ MUNA A AD LAGA FYRIR SKIL
        captains_team = self.logic_wrapper.all_captains(ssn)
        if captains_team != False:
            return captains_team
        return False    
  
    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()

            if command == "q":
                print("Goodbye")
                break

            elif command == "1":
                valid = True#self.ask_for_mod_password()
                if valid == True:
                    menu = Moderator_UI(self.logic_wrapper)
                    back_method = menu.input_prompt()
                    if back_method == "q":
                        return "q"
                else:
                    print_access_denied()
                    time.sleep(2.0)

            elif command == "2":
                valid = self.ask_for_captain_password()
                if valid != False:
                    #menu = Captain_UI(self.logic_wrapper)
                    menu = Captain_UI(self.logic_wrapper, valid) #-- ÞETTA Á AÐ VERA FINAL, VALID ER FYURIR KENNITÖLU
                    back_method = menu.input_prompt()
                    if back_method == "q":
                        return "q"
                else:
                    print_access_denied()
                    time.sleep(2.0)

            elif command == "3":
                players = self.logic_wrapper.get_all_players()
                teams = self.logic_wrapper.team_id_for_player()
                view_players(players, teams)

            elif command == "4":
                teams_all = self.logic_wrapper.get_all_teams()
                view_teams(teams_all)

            elif command == "5":
                associations_all = self.logic_wrapper.get_all_associations()
                teams_no = self.logic_wrapper.teams_in_association()
                view_association(associations_all, teams_no)

            # elif command == "6":
            #     menu = Statistics_UI(self.logic_wrapper)
            #     back_method = menu.input_prompt()
            #     if back_method == "q":
            #         return "q"

            elif command == "7":
                menu = Tournament_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"

            else:
                print("invalid input, try again")
                
