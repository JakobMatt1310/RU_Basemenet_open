from model.tournament import Tournament
from model.team import Team
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *  # print_current_menu
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
                tournaments_all = self.logic_wrapper.get_all_tournaments()
                # teams_no = self.logic_wrapper.teams_in_association()
                view_tournaments(tournaments_all)

            elif command == "2":
                self.create_new_tournament()
            
            elif command == "3":
                print("edit the tournament")
                pass

            elif command == "4":
                # prenta lista af tournaments sem eru til en ekki búið að skrá neinar niðurstöður a.k.a. tournaments sem má eyða.
                self.logic_wrapper.remove_tournament(tournament)
                
            else:
                print("invalid input, try again")

    def create_new_tournament(self):
        tournament = Tournament()
        return_command = ""

        while True:
            tournament.tournament_name = input("Enter the name of the tournament: ")
            tournament.tournament_address = input("Enter the address of the tournament: ")
            tournament.start_date = input("Please enter the first day of the tournament (dd.mm.yyyy): ")
            tournament.end_date = input("Now enter the final day of the tournament (dd.mm.yyyy): ")
            tournament.organizer = input("Enter the name of the tournament organizer: ")
            tournament.organizer_number = input("Please enter a phone number where the organizer may be reached")
            try:
                validate_tournament_name(tournament.tournament_name)
                validate_home_address(tournament.tournament_address)
                validate_phonenumber(tournament.organizer_number)
                break
            except TournamentNameLengthException:
                print("name was too long, try again")
            except HomeAddressException:
                print("The address is invalid, try again")
            except PhoneNumberException:
                print("Invalid phonenumber (must be 7 digits long), please try again.")
            except:
                print("Something went wrong, please try again")
        
        self.logic_wrapper.create_tournament(tournament)
        ask_add_teams = input("Would you like to add teams to the tourney right away? (yes/no): ")
        if ask_add_teams == 'yes':
            self.add_teams(tournament.id)
        else:
            return
    
    def add_teams(self, tournament_id):
        add_another = 'yes'
        while add_another == 'yes':
            team_to_add = input("Please enter the name of the team you want to add to the tournament: ")
            teams_list = self.logic_wrapper.get_teams_by_name(team_to_add)
            
            id_list = []
            print("{:<18}{:<20}{}".format("Team ID", "Team Name"))
            for team in teams_list:
                print("{:<15}{:<17}".format(team.id, team.name))
                id_list.append(team.id)
            if len(id_list) == 1:
                selection = id_list[0]
                team_to_add = self.logic_wrapper.get_team(selection)
                self.logic_wrapper.add_team_to_tourney(tournament_id, team_to_add.id)
                add_another = ("Would you like to add another team? (yes/no): ")
            else:  
                selection = input("Select team by id: ")
                if selection == 'b':
                    print("Going back")
                    return
                elif selection in id_list:
                    team_to_add = self.logic_wrapper.get_team(selection)
                    break
                else:
                    ("The team id you entered is invalid, please try again.")

