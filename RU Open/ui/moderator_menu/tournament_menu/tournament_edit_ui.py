from model.tournament import Tournament
from model.team import Team
from model.player import Player
from model.match import Match
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *
from ui.input_validators import *
from datetime import date
from model.datetime import DateTime


class Tournament_editing_UI:
    Menu_selection = {"Current Menu": "Tournament", 
                    "Add team": ">>> Choose a team to compete in the tournament",
                    #"Remove team": ">>> Removes a team from the tournament",
                    # "Edit Tournament Details": ">>> Make changes to details in the tournament",
                    "Create Matches": ">>> Makes the user create matches in the tournament"}    
    #Create a tournament
    #
    def __init__(self, logic_connection):
        self.today = date.today()
        self.logic_wrapper = logic_connection
        self.date = DateTime(self.today.day, self.today.month, self.today.year)


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
                
                available_tournaments = self.logic_wrapper.get_all_tournaments()
                print_available_tournaments(available_tournaments)
                selection = input("Select a tournament to add teams to: ").lower()
                if selection == "b":
                    return 
                if selection.isdigit() == True:
                    selection = int(selection) - 1
                if selection <= len(available_tournaments):
                    tournament_to_update = available_tournaments[selection]
                else:
                    print("Invalid input")
                self.add_teams(tournament_to_update)
            #elif command == "2":
                # remove_from_tournament = input("Please enter the name of the tournament you would like to remove a team from: ")
                # tournament_to_update = self.logic_wrapper.get_tournament(remove_from_tournament)
                # self.remove_team(tournament_to_update.id)
            # elif command == "2":
            #     self.edit_tournament()
            elif command == "2":
                available_tournaments = self.logic_wrapper.get_all_tournaments()
                print_available_tournaments(available_tournaments)
                selection = input("Select a tournament to create matches in: ")
                if selection.isdigit() == True:
                    selection = int(selection) - 1
                if selection <= len(available_tournaments):
                    tournament_to_add_matches = self.logic_wrapper.get_tournament(available_tournaments[selection])
                else:
                    print("Invalid input")
                self.create_matches(tournament_to_add_matches)
            
    
#   #  def edit_tournament(self):
#         '''Brings up a mini menu to edit a tournaments details'''
#         return_command = ""
#         while True:
#             if return_command != "back":
#                 tourney_to_edit = input("Please enter the name of the tournament you want to edit: ")
#                 tourney_to_edit = self.logic_wrapper.get_tourney(tourney_to_edit)
#             else:
#                 return_command = ""
#             if tourney_to_edit != None:
#                 print_edit_menu_team(tourney_to_edit)
#                 edit_info = input("Enter option to edit: ")
#                 if edit_info == 'b':
#                     print("Going back")
#                     return

#                 elif edit_info == '1':
#                     tourney_to_edit.name = self.change_tourney_name(tourney_to_edit)
#                     print(f"Player name changed to {tourney_to_edit.name}.")
#                     return_command = "back"
#                 elif edit_info == '2':
#                     tourney_to_edit.address = self.change_tourney_address(tourney_to_edit)
#                     print(f"Player name changed to {tourney_to_edit.name}.")
#                     return_command = "back"
#                 elif edit_info == '3':
#                     tourney_to_edit.organizer = self.change_tourney_organizer(tourney_to_edit)
#                     print(f"Player name changed to {tourney_to_edit.organizer}.")
#                 elif edit_info == '4':
#                     return_command = self.change_tourney_organizer_number(tourney_to_edit)
#             else:
#                 print("Tourney doesn't exist, try again.")
    def create_matches(self, tournament):
        teamids_in_tourney = self.logic_wrapper.get_teams_in_tourney(tournament)
        teams_to_play = self.logic_wrapper.get_teams_by_id(teamids_in_tourney)
        for i in range(len(teams_to_play)):
            for j in range(i+1, len(teams_to_play)):
                match = Match
                match.tournament_id = tournament.id
                match.home_team_id = teams_to_play[i].id
                match.away_team_id = teams_to_play[j].id
                home_team = self.logic_wrapper.get_team_by_id(teams_to_play[i])
                away_team = self.logic_wrapper.get_team_by_id(teams_to_play[j])
                match.date = self.match_date(home_team, away_team)
                match.time = '0'


                self.logic_wrapper.create_match(match)
    
    def match_date(self, home_team, away_team):
        while True:
            date = input(f"Please enter the date for the {home_team.name} VS {away_team.name} match (dd.mm.yyyy): ")
            if date == "c":
                return True, "none"
            dots = 0
            valid = False
            for letter in date:
                if letter == ".":
                    dots += 1
            if dots == 2:
                if date[0:2].isdigit():
                    if date[3:5].isdigit():
                        if date[7:11].isdigit():
                            valid = True
                            date = date.strip().split(".")
            if valid == True:   
                try:
                    date_obj = DateTime(int(date[0]),int(date[1]),int(date[2]))
                    validate_start_date(date_obj, self.date)
                    return False, date
                except StartDateException:
                    print("Date entered is not valid, please try again")
                except :
                    print("An error occoured, please try again")
            else: 
                print("Invalid.")
    
    def add_teams(self, tournament):
        while True:
            available_teams = self.logic_wrapper.teams_not_in_tourney(tournament)
            if len(available_teams) != 0:
                print_teams_to_add_to_tourney(available_teams)
            else:
                print_teams_to_add_to_tourney_empty()
                input("Press enter to go back")
                break
            selection = input("Select a team to add: ")
            if selection == "b":
                break
            if selection.isdigit() == True:
                selection = int(selection) - 1
                if selection <= len(available_teams):
                    self.logic_wrapper.add_team_to_tourney(tournament, available_teams[selection])
                else:
                    print("Invalid input")
            else:
                print("Invalid input")

    # def remove_team(self, tournament_id):
    #     '''Removes a team from the chosen tournament'''
    #     while True:
    #         team_to_remove = input("Please enter the name of the team you want to remove from the tournament: ")
    #         teams_list = self.logic_wrapper.get_teams_by_name(team_to_remove)
        
    #         id_list = []
    #         print("{:<18}{:<20}{}".format("Team ID", "Team Name"))
    #         for team in teams_list:
    #             print("{:<15}{:<17}".format(team.id, team.name))
    #             id_list.append(team.id)
    #         if len(id_list) == 1:
    #             selection = id_list[0]
    #             team_to_remove = self.logic_wrapper.get_team(selection)
    #             self.logic_wrapper.remove_team_from_tourney(tournament_id, team_to_remove.id)
    #             break
    #         else:  
    #             selection = input("Select team by id: ")
    #             if selection == 'b':
    #                 print("Going back")
    #                 return
    #             elif selection in id_list:
    #                 team_to_remove = self.logic_wrapper.get_team(selection)
    #                 break
    #             else:
    #                 ("The team id you entered is invalid, please try again.")

    def change_tourney_name(self):
        """Asks for tournament name until it's valid

        Returns:
            str: name of player
        """
        while True:
            tourney_name = input("Enter the name of the player(max 30 char): ")
            try:
                validate_name(tourney_name)
                break
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return tourney_name

    def change_tourney_address(self):
        """Asks for a valid tournament address, requirements are atleast 1 digit at end of address
        If it has a letter for ending, checks if second last is digit, example Street 2B

        Returns:
            str: Tournament address
        """
        while True:
            address = input("Enter the address where the tournament will take place: ")
            try: 
                validate_home_address(address)
                break
            except HomeAddressException:
                print("Invalid input, Please try again")
            except:
                print("Something went wrong, please try again.")
        return address

    def change_tourney_organizer(self):
        """Asks for organizer name until it's valid

        Returns:
            str: name of player
        """
        while True:
            organizer_name = input("Enter the name of the organizer(max 30 char): ")
            try:
                validate_name(organizer_name)
                break
            except TeamNameLengthException:
                print("Name to long or to short")
            except:
                print("Something went wrong, please try again.")
        return organizer_name

    def change_organizer_number(self):
        """Asks for organizer phone number until it's a valid phone number

        Returns:
            str: Organizers phonenumber
        """
        while True:
            organizer_number = input("Enter the organizers new phone number: ")
            try:
                validate_phonenumber(organizer_number)
                break
            except PhoneNumberException:
                print("Input incorrect, please try again.")
            except:
                print("Something went wrong, please try again.")
        return organizer_number