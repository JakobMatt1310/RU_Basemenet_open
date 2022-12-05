import os
import time

WIDTH = 120 # Default width of the program
HALF_WIDTH = int(WIDTH/2)
THIRD_WIDTH = int(WIDTH/3)
MENU_LEN = 47 # How long the menu is
MENU_PAD = HALF_WIDTH-MENU_LEN # How much is padded from left to right
X = 'x' #letter representing seperation in program, header, main, etc..
DASH = "-"




def print_header_logo():
    """Prints the header with title printed"""
    print("\033[1;32;40m", end="")
    print_border()
    print_empty_line()   
    logo_text = "RU Basement Open"
    print(f"{X}{logo_text:^{WIDTH-2}}{X}")
    print_empty_line()   
    print_border()
    print("\033[0m")

def print_empty_line():
    """Prints and empty line with symbols at each end of witdh
    """
    print(f"{X:<{WIDTH-1}}{X}")
    
def print_border():
    "Prints the border in correct length"
    print(X*WIDTH)

def clear_screen():
    """Clears the screen, prints header and 1 empty line"""
    os.system('cls')
    print_header_logo()
    
def print_current_menu(dict_to_print: dict):
    """Prints a listed menu, with numbering and explination
    argument needs to be dict"""
    

    clear_screen()
    print("\033[1;32;40m", end="")
    menu_name = dict_to_print['Current Menu']
    back = ["b. Go back", ">>> To go back to previous Menu"]
    quit_prog = ["q. Quit Program", ">>> Select if you want to quit program"]
    print_border()
    print_empty_line()
    print(f"{X}{menu_name:^{WIDTH-2}}{X}") # prints out name of current menu selected
    print_empty_line()
    keys = [key for key in dict_to_print.keys()]
    values = [value for value in dict_to_print.values()]
    for index, element in enumerate(keys[1:], 1): #element no 0 in all dicts are the same
        selection = str(index)+'. '+element
        text = values[index]
        print(f"{X:<{MENU_PAD}}{selection:<{MENU_LEN}}{text:<{MENU_LEN}}{X:>{MENU_PAD}}")
    
    print_empty_line()
    if values[0] != "Main Menu": # Do not display go back if current menu is main menu
        print(f"{X:<{MENU_PAD}}{back[0]:<{MENU_LEN}}{back[1]:<{MENU_LEN}}{X:>{MENU_PAD}}")
    print(f"{X:<{MENU_PAD}}{quit_prog[0]:<{MENU_LEN}}{quit_prog[1]:<{MENU_LEN}}{X:>{MENU_PAD}}")
    
    print_empty_line()
    print_border()
    print("\033[0m") 
    
def create_menu(list_to_print):
    pass

def edit_menu(list_to_edit):
    pass

def view_players(file_object):
    print("\033[1;32;40m", end="")
    print(f"{' ':30}{(X*60):<60}") 
    print(f"{' ':30}{X:<59}{X}") 
    print(f"{' ':30}{X}{'Viewing all players':^58}{X}")    
    print(f"{' ':30}{X:<59}{X}") 
    print(f"{' ':30}{(X*60):<60}")
    time.sleep(2.0) 
    print()
    print_border()
    print_empty_line()
    print(f"{X:<7}{'Name':<30}{'Team':<20}{'DoB (d/m/y)':<16}{'Tel. no.':<16}{'Email address':<30}{X}")
    file_object.sort(key = lambda x : x.name)
    for element in file_object:
        if element.ssn[4:6] <'22':
            year = '20' + element.ssn[4:6]
        else:
            year = '19' + element.ssn[4:6]
        date_of_birth = element.ssn[0:2] +'.'+ element.ssn[2:4] +'.'+ year
        phone_no = element.phone[0:3] +'-'+ element.phone[3:]
        print(f"{X:<7}{element.name:<30}{'element.team':<20}{date_of_birth:<16}{phone_no:<16}{element.email:<30}{X}")    
    
    print_empty_line()
    print_border() 

    input("\033[0m Press Enter to go back")

def view_teams(file_object: classmethod):
    pass

def edit_menu_selected_team(team: classmethod, players: list):
    """prints out the edit menu, for tournament, association, team and player"""
    
    clear_screen()
    print("\033[32m", end="")
    print_border()
    print_empty_line()
    print(f"{X}{team.association_name+' - '+team.team_name:^{WIDTH-2}}{X}")
    print_empty_line()
    print(f"{X:<{MENU_PAD}}1. {team.team_name:<20}{'//Edit name':<25}{'|':<3}--> {players[0].name:<{MENU_LEN}}{X:>{MENU_PAD-8}}")
    print(f"{X:<{MENU_PAD}}2. {team.association_name:<20}{'//Edit association':<25}{'|':<3}--> {players[1].name:<{MENU_LEN}}{X:>{MENU_PAD-8}}")
    print(f"{X:<{MENU_PAD}}3. {team.captain_name:<20}{'//Edit captain':<25}{'|':<3}--> {players[2].name:<{MENU_LEN}}{X:>{MENU_PAD-8}}")
    print(f"{X:<{MENU_PAD}}4. {'Players':<20}{'//Edit players ----------':<25}{'--':<3}--> {players[3].name:<{MENU_LEN}}{X:>{MENU_PAD-8}}")
    print_empty_line()
    print_border()
    return input("\033[0mEnter selection and press enter: ")    
    print("\033[1;32;40m", end="")
    print_border()
    
    #Example of the outcome below
# x   Team Number : 4           xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                             x
# x                             x               Association : Stjarnan                     x                             x
# x                             x                      Team : 123.flokkur                  x                             x
# x                             x         ----------------------------------------         x                             x
# x                             x               Name                         Role          x                             x
# x                             x            Máni Freyr                    Captain         x                             x
# x                             x            Jakob Matt                     Player         x                             x
# x                             x          Sigurður Tómas                   Player         x                             x
# x                             x           Hannes Aron                     Player         x                             x
# x                             xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                             x
    
    for i, el in enumerate(file_object, 1):
        print_empty_line()
    

        print(f"{X:4}{'Team Number : ':<5}{i:<12}{(X*60):<60}{X:>30}")                     #Border for box surrounding team information
        print(f"{X:<30}{X}{'Association : ':>29}{el.association_name:<29}{X:<30}{X}")
        print(f"{X:<30}{X}{'Team : ':>29}{el.team_name:<29}{X:<30}{X}")                 
        print(f"{X:<30}{X:<10}{(DASH*40):40}{X:>10}{X:>30}")                             #Seperation line with dashes --------
        print(f"{X:30}{X}{('Name'):^34}{'Role':^24}{X}{X:>30}")
        print(f"{X:30}{X}{(el.captain_name):^34}{'Captain':^24}{X}{X:>30}")
        players_list = el.team_players
        players_list.sort()
        for player in players_list:
            if player != el.captain_name:
                print(f"{X:30}{X}{(player):^34}{'Player':^24}{X}{X:>30}")
            
        print(f"{X:30}{(X*60):<60}{X:>30}")      
    
    print_empty_line()
    print_border() 
    print("\033[0m")
    ret = input("Press Enter to go back")


def view_association(file_object):
    pass



# print_current_menu(Menu_selection)
