from datetime import datetime, timedelta
from logic_wrapper_dummy import Logic_Wrapper
from model.tournament_model_dummy import Tournament
from print_layouts import *
class Tournament_UI:
    Menu_selection = {"Current Menu": "Team Menu", 
                    "View Tournaments": ">>> Lists all teams in our database",
                    "View Tournament": ">>> Lists all teams in our database",
                    "Create Tournament": ">>> Lists all teams in our database",
                    "Edit Tournament": ">>> Lists all teams in our database",
                    "Delete Tournament": ">>> Lists all teams in our database"}    

    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def get_start_date(start_date):
        day, month, year = start_date.split('.')
        date = datetime(day, month, year)


    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
            if command == "b":
                print("Going back")
                break
            if command == "q":
                print("Quitting")
                return "q"
            elif command == "1":
                #(self, tournament_name, competing_teams=None, first_day_of_tourney="", last_day_of_tourney="", organizer="", oranizer_phone_number=""):
                tournament = Tournament()
                tournament.tour_name = input("Please enter a name for the tournament: ")
                tournament.tour_address = input("Please enter the address where the tournament will take place: ")
                start_date_to_convert = input("Please enter the date for the starting day of the tournament (dd.mm.yyyy = 09.12.2022): ")
                how_many_days = int(input("How many days should the tournament last?: "))
                tournament.end_date = datetime + timedelta(days=how_many_days)

                
                
        #self.tour_name = tour_name              # Name of the tournament
        #self.tour_address = tour_address        # Address of the tournament
        #self.start_date = start_date            # Starting date of the tournament
        #self.end_date = end_date                # End date of the tournament
        #self.game_count = game_count            # Number of games played in the tournament
        #self.teams_submitted = teams_submitted  # Number of teams submitted to the tournament
        #self.game_id = game_id                  # Game ID
        #self.game_type = game_type              # Game type (7 games in whole), 501 1vs1 4 games, 301 2vs2 1 game, Cricket 2vs2 1 game, 501 4vs4 1 game ==== 7 games in whole
        #self.leg_nr = leg_nr                    # Leg number is "round" in each game, there is always 3 legs in each game and winner is the one who wins 2 legs or best of 3
        #self.player_id = player_id              # Player ID is the ID of the player in the tournament        
                list_of_competing_teams = []        
                teams = self.logic_wrapper.get_all_teams()
                name, address, tournament_id
                teams_in_tourneys.csv
                tournament1, 
