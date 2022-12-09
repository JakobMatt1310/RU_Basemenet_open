import os
import time
from random import randint

WIDTH = 120 # Default width of the program
HALF_WIDTH = int(WIDTH/2)
THIRD_WIDTH = int(WIDTH/3)
MENU_LEN = 47 # How long the menu is
MENU_PAD = HALF_WIDTH-MENU_LEN # How much is padded from left to right
X = 'x' #letter representing seperation in program, header, main, etc..
DASH = "-"
BACK = ["b. Go back", ">>> To go back to previous Menu"]
QUIT_PROG = ["q. Quit Program", ">>> Select if you want to quit program"]



def print_header_logo():
    """Prints the header with title printed"""
    print("\033[1;32;40m", end="")
    print_border()
    print_empty_line()   
    logo_text = "RU Basement Open"
    print(f"{X}{logo_text:^{WIDTH-2}}{X}")
    print_empty_line()   
    print_border()
    print("\033[0m", end="")

def print_empty_line():
    """Prints and empty line with symbols at each end of witdh
    """
    print(f"{X:<{WIDTH-1}}{X}")
    
def print_empty_line_half():
    """Prints and empty line with symbols at each end of witdh
    """
    print(f"{' ':30}{X:<{HALF_WIDTH-1}}{X}")
    
def print_border():
    "Prints the border in correct length"
    print(X*WIDTH)

def print_border_half():
    "Prints the border in correct length"
    print(f"{' ':30}{X*HALF_WIDTH}")

def clear_screen():
    """Clears the screen, prints header and 1 empty line"""
    os.system('cls')
    print_header_logo()

def print_access_denied():
    text = ["    __ _  ___ ___ ___  ___ ___  ", 
            "   / _` |/ __/ __/ _ \/ __/ __| ", 
            '  | (_| | (_| (_|  __/\__ \__ \ ', 
            "   \__,_|\___\___\___||___/___/ ", 
            "    | |          (_)        | | ",
            "  __| | ___ _ __  _  ___  __| | ",
            " / _` |/ _ \ '_ \| |/ _ \/ _` | ",
            "| (_| |  __/ | | | |  __/ (_| | ",
            " \__,_|\___|_| |_|_|\___|\__,_| "]
    clear_screen()
    print("\033[1;32;40m", end="")
    print_border()
    print_empty_line()
    print_empty_line()
    for line in text:
        print(f"{X}", end="")
        print(f"\033[31m{line:^{WIDTH-2}}", end="")
        print(f"\033[32m{X}")
    print_empty_line()
    print_empty_line()
    print_border()

# def print_current_menu(dict_to_print: dict):
#     """Prints a listed menu, with numbering and explination
#     argument needs to be dict"""
    

#     clear_screen()
#     print("\033[1;32;40m", end="")
#     menu_name = dict_to_print['Current Menu']
#     start = define_start()
#     print_border()
#     print_empty_line()
#     print(f"{X}{menu_name:^{WIDTH-2}}{X}") # prints out name of current menu selected
#     print_empty_line()
#     keys = [key for key in dict_to_print.keys()]
#     values = [value for value in dict_to_print.values()]
#     for index, element in enumerate(keys[1:], start): #element no 0 in all dicts are the same
#         selection = str(index)+'. '+element
#         text = values[start]
#         print(f"{X:<{MENU_PAD}}{selection:<{MENU_LEN}}{text:<{MENU_LEN}}{X:>{MENU_PAD}}")
    
#     print_empty_line()
#     if values[0] != "Main Menu": # Do not display go back if current menu is main menu
#         print(f"{X:<{MENU_PAD}}{BACK[0]:<{MENU_LEN}}{BACK[1]:<{MENU_LEN}}{X:>{MENU_PAD}}")
#     print(f"{X:<{MENU_PAD}}{QUIT_PROG[0]:<{MENU_LEN}}{QUIT_PROG[1]:<{MENU_LEN}}{X:>{MENU_PAD}}")
    
#     print_empty_line()
#     print_border()
#     print("\033[0m") //////// BACKUP

def print_current_menu(dict_to_print: dict):
    """Prints a listed menu, with numbering and explination
    argument needs to be dict"""
    

    clear_screen()
    print("\033[1;32;40m", end="")
    menu_name = dict_to_print['Current Menu']
    start = define_start()
    print_border()
    print_empty_line()
    print(f"{X}{menu_name:^{WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line()
    keys = [key for key in dict_to_print.keys()]
    values = [value for value in dict_to_print.values()]
    for index, element in enumerate(keys[1:], start): #element no 0 in all dicts are the same
        selection = str(index)+'. '+element
        text = values[start]
        print(f"{X:<{MENU_PAD}}{selection:<{MENU_LEN}}{text:<{MENU_LEN}}{X:>{MENU_PAD}}")
    
    print_empty_line()
    if values[0] != "Main Menu": # Do not display go back if current menu is main menu
        print(f"{X:<{MENU_PAD}}{BACK[0]:<{MENU_LEN}}{BACK[1]:<{MENU_LEN}}{X:>{MENU_PAD}}")
    print(f"{X:<{MENU_PAD}}{QUIT_PROG[0]:<{MENU_LEN}}{QUIT_PROG[1]:<{MENU_LEN}}{X:>{MENU_PAD}}")
    
    print_empty_line()
    print_border()
    print("\033[0m") 

def print_name_players(players):
    count = 0
    print("\033[33m", end="")
    print_border()
    print_empty_line()
    space_left = 120
    for player in players:
        if count == 0:
            print(f"{X:<4}", end="")
            space_left -= 4
            count +=1
        elif count == 5:
            space_left = 120
            count = 0
            print(f"{X:>4}")
        else:
            print(f"{player.name:<28}", end="")
            space_left -=28
            count += 1
    print(f"{X:>{space_left}}")
    print_empty_line()
    print_border()
    print("\033[0m")


def view_players(player: list, teams: dict):
    clear_screen()
    time.sleep(0.5)
    print("\033[32m", end="")
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(0.1) 
    print(f"{' ':30}{X:<59}{X}")
    time.sleep(0.1)
    print(f"{' ':30}{X}{'Viewing all players':^58}{X}")    
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{(X*60):<60}\033[32m")
    time.sleep(0.5) 
    print_border()
    print_empty_line()
    print(f"{X:<7}{'Name':<22}{'Team':<24}{'DoB (d/m/y)':<16}{'Tel. no.':<16}{'Email address':<34}{X}")
    player.sort(key = lambda x : x.name)
        
    for element in player:
        if element.ssn[4:6] <'22':
            year = '20' + element.ssn[4:6]
        else:
            year = '19' + element.ssn[4:6]
        date_of_birth = element.ssn[0:2] +'.'+ element.ssn[2:4] +'.'+ year
        phone_no = element.phone[0:3] +'-'+ element.phone[3:]
        player_team = teams[element.team_id]
        print(f"{X:<7}{element.name:<22}{player_team:<24}{date_of_birth:<16}{phone_no:<16}{element.email:<34}{X}")    
        time.sleep(0.0001)    

   
    print_empty_line()
    print_border() 

    input("\033[0m Press Enter to go back: ")

def view_teams(teams_list: list):
    clear_screen()
    time.sleep(0.5)

    print("\033[1;32;40m", end="")
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(0.1) 
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1) 
    print(f"{' ':30}{X}{'Viewing all teams':^58}{X}")    
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(0.5)
    print_border()
    print(f"{X:<7}{'Team name':<{THIRD_WIDTH}}{'Team association':<{THIRD_WIDTH}}{'Team captain':<{THIRD_WIDTH-8}}{X}")
    print(f"{X:<30}{(DASH*60):60}{X:>30}")                             #Seperation line with dashes --------

    for el in teams_list:
    
        print(f"{X:<7}{el.name:<{THIRD_WIDTH}}{el.association:<{THIRD_WIDTH}}{el.captain:<{THIRD_WIDTH-8}}{X}")    

        time.sleep(0.01)    
    
    print_empty_line()
    print_border() 
    print("\033[0m")
    input("Press Enter to go back: ")

# def view_teams(teams_list: list):
#     clear_screen()
#     time.sleep(0.5)

#     print("\033[1;32;40m", end="")
#     print(f"{' ':30}{(X*60):<60}")
#     time.sleep(0.1) 
#     print(f"{' ':30}{X:<59}{X}") 
#     time.sleep(0.1) 
#     print(f"{' ':30}{X}{'Viewing all teams':^58}{X}")    
#     time.sleep(0.1)
#     print(f"{' ':30}{X:<59}{X}") 
#     time.sleep(0.1)
#     print(f"{' ':30}{(X*60):<60}")
#     time.sleep(0.5)
#     print_border()
#     print(f"{X:<7}{'Team name':<{THIRD_WIDTH}}{'Team association':<{THIRD_WIDTH}}{'Team captain':<{THIRD_WIDTH-8}}{X}")
#     print(f"{X:<30}{(DASH*60):60}{X:>30}")                             #Seperation line with dashes --------

#     for el in teams_list:
    
#         print(f"{X:<7}{el.name:<{THIRD_WIDTH}}{el.association:<{THIRD_WIDTH}}{el.captain:<{THIRD_WIDTH-8}}{X}")    

#         time.sleep(0.01)    
    
#     print_empty_line()
#     print_border() 
#     print("\033[0m")
#     input("Press Enter to go back: ") //////////// Backup
    
def edit_menu_selected_team(team: classmethod, ):
    """prints out the edit menu, for tournament, association, team and player"""
    back = ["b. Go back", ">>> To go back to previous Menu"]
    clear_screen()
    print("\033[32m", end="")
    print_border()
    print_empty_line()
    print(f"{X}{team.association+' - '+team.name:^{WIDTH-2}}{X}")
    print_empty_line()
    print(f"{X:<{35}}1. {team.name:<30}{'//Edit name':<25}{X:>27}")
    print(f"{X:<{35}}2. {team.association:<30}{'//Edit association':<25}{X:>27}")
    print(f"{X:<{35}}3. {team.captain:<30}{'//Edit captain':<25}{X:>27}")
    print(f"{X:<{35}}4. {'Players':<30}{'//Edit players ':<25}{X:>27}")
    print_empty_line()
    print(f"{X:<{35}}{back[0]:<{33}}{back[1]:<{25}}{X:>{21}}")
    print_border()
    return input("\033[0mEnter selection and press enter: ")

def view_association(associations: classmethod, teams_dict: dict):
    """Hér vil ég fá get all associations og get all teams"""
    clear_screen()
    print("\033[1;32;40m", end="")
    time.sleep(0.5)
    print(f"{' ':30}{(X*60):<60}") 
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{X}{'Viewing all associations':^58}{X}")    
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(0.5) 

    print_border()
    print_empty_line()
    print(f"{X:<13}{'Name':<30}{'Street address':<32}{'Tel. no.':<21}{'Number of teams':<19}{X:>5}")
    associations.sort(key = lambda x : x.name)
    for element in associations:
        phone_no = element.phone[0:3] +'-'+ element.phone[3:]
        home_address = element.address
        try:
            no_of_teams = teams_dict[element.id]
        except KeyError:
            no_of_teams = 0
            
        print(f"{X:<13}{element.name:<30}{home_address:<32}{phone_no:<21}{no_of_teams:<19}{X:>5}")    
        time.sleep(0.1)    

    
    print_empty_line()
    print_border() 
    input("\033[0m Press Enter to go back: ")

def edit_menu_selected_association(association: classmethod, teams: list):
    """prints out the edit menu, for tournament, association, team and player"""
    
    back = ["b. Go back", ">>> To go back to previous Menu"]
    clear_screen()
    print("\033[32m", end="")
    print_border()
    print_empty_line()
    print(f"{X}{association.name:^{WIDTH-2}}{X}")
    print_empty_line()
    print(f"{X:<{35}}1. {'Add team':<30}{'// Add teams to association':<25}{X:>25}")
    print(f"{X:<{35}}2. {'Remove team':<30}{'// Add teams to association':<25}{X:>25}")
    print(f"{X:<{35}}3. {association.name:<30}{'// Edit name':<25}{X:>27}")
    print(f"{X:<{35}}4. {association.phone:<30}{'// Edit phone number':<25}{X:>27}")
    print(f"{X:<{35}}5. {association.address:<30}{'// Edit address':<25}{X:>27}")
    print_empty_line()
    print(f"{X:<{35}}{back[0]:<{33}}{back[1]:<{25}}{X:>{21}}")

    print_border()
    return input("\033[0mEnter selection and press enter: ")

def edit_association_only_menu(association: classmethod):
    """prints out the edit menu for association"""
    
    
    clear_screen()
    print("\033[32m", end="")
    print_border()
    print_empty_line()
    print(f"{X}{association.name:^{WIDTH-2}}{X}")
    print_empty_line()
    print(f"{X:<{30}}1. {association.name:<30}{'// Edit name':<25}{X:>32}")
    print(f"{X:<{30}}2. {association.phone:<30}{'// Edit phone number':<25}{X:>32}")
    print(f"{X:<{30}}3. {association.address:<30}{'// Edit address':<25}{X:>32}")
    print_empty_line()
    print(f"{X:<{30}}{BACK[0]:<{33}}{BACK[1]:<{25}}{X:>{26}}")

    print_border()
    return input("\033[0mEnter selection and press enter: ")

def print_player_edit_menu(player: classmethod):
    """prints out the edit menu for a player"""
    
    
    clear_screen()
    print("\033[1;33;40m", end="")
    print_border_half()
    print_empty_line_half()
    print(f"{' ':30}{X}{'Editing player ->  ' + player.name:^{HALF_WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line_half()
    print(f"{' ':<30}{X:<8}{'   Options':<{25}}{'Current':<26}{X}")
    print(f"{' ':<30}{X:<8}{'1. Change name: ':<{25}}{player.name:<26}{X}")
    print(f"{' ':<30}{X:<8}{'2. Change ssn: ':<{25}}{player.ssn:<26}{X}")
    print(f"{' ':<30}{X:<8}{'3. Change phone number':<{25}}{player.phone:<26}{X}")
    print(f"{' ':<30}{X:<8}{'4. Change email':<{25}}{player.email:<26}{X}")
    print(f"{' ':<30}{X:<8}{'5. Change address':<{25}}{player.address:<26}{X}")
    print_empty_line_half()
    print(f"{' ':<30}{X:<12}{BACK[0]:<{47}}{X}")
    print_border_half()
    print("\033[0m")

def print_current_tournament_layout(tournament, teams_and_players):
    clear_screen()
    print("\033[32m", end="")
    time.sleep(0.5)
    print(f"{' ':30}{(X*60):<60}") 
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    viewing = 'Viewing ' + tournament.name
    print(f"{' ':30}{X}{viewing:^58}{X}")    
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(0.5) 
    if len(teams_and_players) == 0:
        print_border()
        print_empty_line()
        print(f"{X}", end="")
        print(f"\033[31m{'Tournament currently has no active matches':^118}", end="")
        print(f"\033[32m{X}")
    else:
        print_border()
        print_empty_line()
        for i, team in enumerate(teams_and_players, 1):
            print_empty_line()
            print_empty_line()
            print(f"{X:<6}{i}. Team name ~~>> ",end="")
            print(f"\033[33m{team[0].name:<40}", end="")
            print(f"\033[32m{X:>56}")
            print_empty_line()
            print(f"{X:<6}{'Name':<30}{'Phone':<10}{'SSN':<14}{'Address':<30}{'Role':<20}{X:>10}")
            player_list = []
            for player in team[1]:
                if player.name == team[0].captain:
                    player_list.insert(0, player)
                else:
                    player_list.append(player)
            for i, player in enumerate(player_list):
                if i == 0:
                    print(f"{X:<6}{player.name:<30}{player.phone:<10}{player.ssn:<14}{player.address:<30}{'Captain':<20}{X:>10}")
                else: 
                    print(f"{X:<6}{player.name:<30}{player.phone:<10}{player.ssn:<14}{player.address:<30}{'Player':<20}{X:>10}")
            time.sleep(0.01)    
        print_empty_line()
        print_empty_line()
        print_border()

    print_empty_line()
    print_border() 
    print("\033[0m")
def view_tournaments(tournaments: classmethod):
    clear_screen()
    print("\033[1;32;40m", end="")
    time.sleep(0.5)
    print(f"{' ':30}{(X*60):<60}") 
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{X}{'Viewing all tournaments':^58}{X}")    
    time.sleep(0.1)
    print(f"{' ':30}{X:<59}{X}") 
    time.sleep(0.1)
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(0.5) 
    
# "address","start_date","end_date","game_count","teams_submitted","game_id","game_type","leg_nr","player_id"
    #Sorta tournemnts eftir dagsetning vinstramegin og hægramegin
    #Vinstramegin verður "finished" hægtamegin verður"þ.að se er í gangi eða á eftir að byrja"
    print_border()
    print_empty_line()
    print(f"{X:<6}{'ID':<7}{'Tournament: ':<30}{'Address':<32}{'Start date':<21}{'End date':<19}{X:>5}")
    # tournaments.sort(key = lambda x : x.name)
    for i, element in enumerate(tournaments, 1):
        start_date = element.start_date[2:4]+'.'+element.start_date[8:10]+'.'+element.start_date[14:18]
        end_date = element.end_date[2:4]+'.'+element.end_date[8:10]+'.'+element.end_date[14:18]
        
        print(f"{X:<6}{i:<7}{element.name:<30}{element.address:<32}{start_date:<21}{end_date:<19}{X:>5}")    
        time.sleep(0.01)    

    print_empty_line()
    print_border() 
    print("\033[0m")
    
def print_current_team_player_list(players: list, team_name: str):
    """Previews the players that will be added to current team

    Args:
        players (list): contains names of players being added
        team_name (str): 
    """
    clear_screen()
    print("\033[1;33;40m", end="")
    print_border_half()
    print_empty_line_half()
    print(f"{' ':30}{X}{'Assigned players to team -> ' + team_name:^{HALF_WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line_half()
    if len(players) == 1:
        print(f"{' ':<30}{X:<15}{'1. ' + players[0]:<{44}}{X}")
        print_empty_line_half()
        print_empty_line_half()
        print_empty_line_half()
    elif len(players) == 2:
        print(f"{' ':<30}{X:<15}{'1. ' + players[0]:<{44}}{X}")
        print(f"{' ':<30}{X:<15}{'2. ' + players[1]:<{44}}{X}")
        print_empty_line_half()
        print_empty_line_half()
    elif len(players) == 3:
        print(f"{' ':<30}{X:<15}{'1. ' + players[0]:<{44}}{X}")
        print(f"{' ':<30}{X:<15}{'2. ' + players[1]:<{44}}{X}")
        print(f"{' ':<30}{X:<15}{'3. ' + players[2]:<{44}}{X}")
        print_empty_line_half()
    else:
        print(f"{' ':<30}{X:<15}{'1. ' + players[0]:<{44}}{X}")
        print(f"{' ':<30}{X:<15}{'2. ' + players[1]:<{44}}{X}")
        print(f"{' ':<30}{X:<15}{'3. ' + players[2]:<{44}}{X}")
        print(f"{' ':<30}{X:<15}{'4. ' + players[3]:<{44}}{X}")
    print_empty_line_half()
    print_border_half()
    print("\033[0m")

def print_edit_menu_team(team_to_edit: classmethod):
    clear_screen()
    print("\033[1;33;40m", end="")
    print_border_half()
    print_empty_line_half()
    print(f"{' ':30}{X}{'Editing team ->  ' + team_to_edit.name:^{HALF_WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line_half()
    print(f"{' ':<30}{X:<12}{'   Options':<{25}}{'Current':<22}{X}")
    print(f"{' ':<30}{X:<12}{'1. Edit team name':<{25}}{team_to_edit.name:<22}{X}")
    print(f"{' ':<30}{X:<12}{'2. Change association':<{25}}{team_to_edit.association:<22}{X}")
    print(f"{' ':<30}{X:<12}{'3. Change captain':<{25}}{team_to_edit.captain:<22}{X}")
    print_empty_line_half()
    print(f"{' ':<30}{X:<12}{BACK[0]:<{47}}{X}")
    print_border_half()
    print("\033[0m")

def print_edit_menu_association(association: classmethod):
    clear_screen()
    print("\033[1;33;40m", end="")
    print_border_half()
    print_empty_line_half()
    print(f"{' ':30}{X}{'Editing Association ->  ' + association.name:^{HALF_WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line_half()
    print(f"{' ':<30}{X:<12}{'   Options':<{25}}{'Current':<22}{X}")
    print(f"{' ':<30}{X:<12}{'1. Edit Association Name':<{25}}{association.name:<22}{X}")
    print(f"{' ':<30}{X:<12}{'2. Change Phone Number':<{25}}{association.phone:<22}{X}")
    print(f"{' ':<30}{X:<12}{'3. Change Address':<{25}}{association.address:<22}{X}")
    print_empty_line_half()
    print(f"{' ':<30}{X:<12}{BACK[0]:<{47}}{X}")
    print_border_half()
    print("\033[0m")

def print_enter_name_to_edit():
    clear_screen()
    print("\033[1;33;40m", end="")
    print_border_half()
    print_empty_line_half()
    print(f"{' ':30}{X}{'Enter a name to edit':^{HALF_WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line_half()
    print(f"{' ':<30}{X:<4}{BACK[0]:<{55}}{X}")
    print_border_half()
    print("\033[0m")

def define_start():
    return randint(1,4)

def small_menu_setup(team_to_edit: classmethod):
    clear_screen()
    print("\033[1;33;40m", end="")
    # print_border_half()
    # print_empty_line_half()
    # print(f"{' ':30}{X}{'Assigned players to team -> ' + team_to_edit.name:^{HALF_WIDTH-2}}{X}") # prints out name of current menu selected
    # print_empty_line_half()
    # print(f"{' ':<30}{X:<15}{'1. ' + players[0]:<{44}}{X}")
    # print_empty_line_half()
    # print_empty_line_half()
    # print_empty_line_half()
    # print_empty_line_half()
    # print_border_half()
    print("\033[0m")
# print_current_team_player_list(["joi joa",  "siggi sigg", "benni bull"], "eitthvað")

def print_tournament_info(tournament):
    organizer = tournament.organizer + ', '+tournament.organizer_number
    start_date = ".".join(tournament.start_date)
    end_date = ".".join(tournament.end_date)
    date = start_date + ' -> ' +end_date
    clear_screen()
    print("\033[32m", end="")
    print_border()
    print_empty_line()
    print(f"{X}{tournament.name:^118}{X}")
    print_empty_line()
    print(f"{X}{'Location':<30}{'Start date -> End date':<40}{'Organizer, phone no.':<30}{X}")
    print(f"{X:<10}{tournament.address:<30}{date:<40}{organizer:<30}{X:>10}")
    #id,name,address,[start_date],[end_date],organizer,organizer_number
    print_empty_line()
    print_border()
    print("\033[0m")

def print_teams_to_add_to_tourney(teams):

    print("\033[1;33;40m")
    print_border_half()
    print_empty_line_half()
    for i, team in enumerate(teams, 1):
        print(f"{' ':30}{X:<15}{i}. {team.name:<41}{X}")
    print_empty_line_half()
    print(f"{' ':30}{X:<15}{BACK[0]:<44}{X}")
    print_empty_line_half()
    print_border_half()
    print("\033[0m")
    
def print_teams_to_add_to_tourney_empty():

    print("\033[1;33;40m")
    print_border_half()
    print_empty_line_half()
    print(f"{' ':30}{X}{'No teams available':^58}{X}")
    print_empty_line_half()
    print_border_half()
    print("\033[0m")
    
    
    pass
   
def print_available_tournaments(tournaments):
    print("\033[1;33;40m")
    print_border_half()
    print_empty_line_half()
    for i, tourney in enumerate(tournaments, 1):
        print(f"{' ':30}{X:<15}{i}. {tourney.name:<41}{X}")
    print_empty_line_half()
    print(f"{' ':30}{X:<15}{BACK[0]:<44}{X}")
    print_empty_line_half()
    print_border_half()
    print("\033[0m")
                            
# def print_available_tournaments(tournaments):
#     print("\033[1;33;40m")
#     print_border_half()
#     print_empty_line_half()
#     for i, tourney in enumerate(tournaments, 1):
#         print(f"{' ':30}{X:<15}{i}. {tourney.name:<41}{X}")
#     print_empty_line_half()
#     print(f"{' ':30}{X:<15}{BACK[0]:<44}{X}")
#     print_empty_line_half()
#     print_border_half()
#     print("\033[0m")   //////// Backup
                            