from model.tournament import Tournament
from model.team import Team
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *  # print_current_menu
from ui.input_validators import *
from datetime import date
from model.datetime import DateTime


class Tournament_UI:
    Menu_selection = {"Current Menu": "Tournament",
                    "View Tournaments": ">>> Lists all tournaments",
                    "Create Tournament": ">>> Creates a tournament",
                    "Edit Tournament": ">>> Modify menu for a tournament"}
    def __init__(self, logic_connection):
        self.today = date.today()
        self.logic_wrapper = logic_connection
        self.logic_wrapper = Logic_Wrapper()
        self.date = DateTime(self.today.day, self.today.month, self.today.year)

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def input_prompt(self):
        
        today_formated = self.today.strftime("%d %B, %Y")
        print(today_formated)
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

    def tournament_name(self):
        all_names = self.logic_wrapper.get_all_tournaments()
        while True:
            name = input("Enter the name of the tournament: ")
            if name == "c":
                return True, "none"
            try:
                validate_tournament_name(name, all_names)
                return False, name
                
            except TournamentNameLengthException:
                print("Name to long, try again")
            except TournamentNameExists:
                print("Name already exists, try another name (different year f.x.)")
        
    
    def tournament_address(self):
        while True:
            address = input("Enter the address of the tournament: ")
            if address == "c":
                return True, "none"
            try:
                validate_home_address(address)
                return False, address
            except HomeAddressException:
                print("Street address invalid, please try again")
    
    def tournament_start_date(self):
        while True:
            date = input("Please enter the first day of the tournament (dd.mm.yyyy): ")
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
            
    def tournament_end_date(self, s_date):
        while True:
            date = input("Now enter the final day of the tournament (dd.mm.yyyy): ")
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
                    end_date = DateTime(int(date[0]),int(date[1]),int(date[2]))
                    start_date = DateTime(int(s_date[0]),int(s_date[1]),int(s_date[2]))
                    validate_end_date(start_date, end_date)
                    return False, date
                except EndDateException:
                    print("Invalid date, please try again")
                except :
                    print("An error occoured, please try again")
    
    def tournament_organizer(self):
        while True:
            name = input("Enter the name of the tournament organizer: ")
            if name == "c":
                return True, "none"
            try:
                validate_name(name)
                return False, name
            except NameLengthException:
                print("Name too short or too long, please try again(max 30 char)")
            except:
                print("An error occoured, please try again")
    
    def tournament_organizer_phonenumber(self):
        while True:
            number = input("Enter organizer phone number: ")
            if number == "c":
                return True, "none"
            try:
                validate_phonenumber(number)
                return False, number
            except PhoneNumberException:
                print("Phone-number invalid, please try again")
            except:
                print("An error occoured, please try again")

    def create_new_tournament(self):
        tournament = Tournament()
        print(f"{'c. Cancel creating new tournament': ^120}")
        

        while True:
            cancel, tournament.name = self.tournament_name()
            if cancel == True:
                return
            cancel, tournament.address = self.tournament_address()
            if cancel == True:
                return
            cancel, tournament.start_date = self.tournament_start_date()
            if cancel == True:
                return
            cancel, tournament.end_date = self.tournament_end_date(tournament.start_date)
            if cancel == True:
                return
            cancel, tournament.organizer = self.tournament_organizer()
            if cancel == True:
                return
            cancel, tournament.organizer_number = self.tournament_organizer_phonenumber()
            if cancel == True:
                return
            else:
                break
            
            
        
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

