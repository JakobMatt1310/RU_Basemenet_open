from model.tournament import Tournament
from model.team import Team
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import print_current_menu
from ui.input_validators import *


class Tournament_UI:
    Menu_selection = {"Current Menu": "Tournament",
                    "View Tournaments": ">>> Lists all tournaments",
                    "Create Tournament": ">>> Creates a tournament",
                    "Edit Tournament": ">>> Modify menu for a tournament"}
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
                return self.logic_wrapper.get_all_tournaments()
                
            elif command == "2":
                tournament = Tournament()
                while True:
                    tournament.tournament_name = input("Enter the name of the tournament: ")
                    tournament.tournament_address = input("Enter the address of the tournament: ")
                    try:
                        validate_tournament_name(tournament.tournament_name)
                        validate_home_address(tournament.tournament_address)
                        break
                    except TournamentNameLengthException:
                        print("name was too long, try again")
                    except HomeAddressException:
                        print("The address is invalid, try again")
                    except:
                        print("Something went wrong, please try again")
                
                self.logic_wrapper.create_tournament(tournament)
            elif command == "3":
                print("edit the tournament")
                pass
            elif command == "4":
                self.logic_wrapper.remove_tournament(tournament)
                
            else:
                print("invalid input, try again")