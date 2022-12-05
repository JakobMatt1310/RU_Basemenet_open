import os
import time
from Front_page import print_frontpage

menu_list = ["Main menu", "Player", "Teams", "Associations", "Statistics", "Tournaments"]
player_list = ["Players menu", "Add player", "Edit player", "Delete player", "Assign as captain"]
teams_list = ["Team menu", "Add team", "Edit team", "Delete team"]
Assiciations_list = ["Associations menu", "Add association", "Edit association", "Assign team to association"]
Statistics = ["Statistics menu", "Top 50 players", "Current games", "Top 50 teams"]
Tournaments = ["Tournament menu", "Create a new tournament", "Edit a tournament", "View finished tournaments"]
player = ["Ólafur Finnbogi Ólafsson", "Sigurður Atli", "Jói berg", "Gunnar Sigga"]
add_player = ["Add player", "Name", "Ssn", "Address", "Landline number", "Telephone number", "Email"]
add_team = ["Add team", "Name", "Captain"]
add_association = ["Add association", "Name", "Address", "Telephone number"]
dummy_player = []
dummy_association = []
dummy_team = []
TEXT = "Please input the number of selection you'd like to choose and press enter"

WIDTH = 90
HALF_WIDTH = int(WIDTH/2)
MAIN_MENU = "Back to main menu"
X = 'x'
def print_logo():
    print(print_border())
    print(print_empty_line())    
    logo_text = "RU Basement Open"
    logo_padding = int(len(logo_text)/2)
    print(f"{X:<{int(WIDTH/2-logo_padding)}}{logo_text}{X:>{int(WIDTH/2-logo_padding)}}")
    print(print_empty_line())    
    print(print_border())
    print()
    pass

def print_empty_line():
    return f"{X:<{int(HALF_WIDTH)}}{X:>{int(HALF_WIDTH)}}"
    
def print_border():
    return ('x'*WIDTH)

def print_Main_Menu():
    clear_screen()
    print_logo()
    first_padding = 15
    menu_padding = 70-first_padding
    print(print_border())
    print(f"x{menu_list[0]:^{WIDTH-2}}x")
    for i, selection in enumerate(menu_list[1:], 1):
        end_line = WIDTH - (first_padding + menu_padding)
        print(f"{X:<{first_padding}}{i}: {selection:<{menu_padding}}{X:>{end_line-3}}")
    print(print_border())
    text = "Please input the number of selection you'd like to choose and press enter"
    print(print_empty_line())    
    print(f"x{text:^{WIDTH-2}}x")
    print(print_empty_line())    
    print(print_border())
    next = input("Selection: ")
    while next != "3":
        print("Please select 3 for testing purpose")
        next = input("Selection: ")
    return next

def clear_screen():
    os.system('cls')
    
def print_menu(Current_menu):
    
    print_logo()
    first_padding = 15
    menu_padding = 70-first_padding
    print(print_border())
    print(f"x{Current_menu[0]:^{WIDTH-2}}x")
    for i, selection in enumerate(Current_menu[1:], 1):
        end_line = WIDTH - (first_padding + menu_padding)
        print(f"{X:<{first_padding}}{i}: {selection:<{menu_padding}}{X:>{end_line-3}}")
    print(print_empty_line())
    print(print_empty_line())
    print(f"{X:<{first_padding}}b: {MAIN_MENU:<{menu_padding}}{X:>{end_line-3}}")
    print(print_border())
    text = "Please input the number of selection you'd like to choose and press enter"
    print(print_empty_line())    
    print(f"x{text:^{WIDTH-2}}x")
    print(print_empty_line())    
    print(print_border())
    next = input("Selection: ")
    while next != "1":
        print("Please select 1 for testing purpose")
        next = input("Selection: ")
    return next
    
def dumme_menu_adding(Current_menu, text=TEXT):
    
    print_logo()
    first_padding = 15
    menu_padding = 70-first_padding
    print(print_border())
    print(f"x{Current_menu[0]:^{WIDTH-2}}x")
    for i, selection in enumerate(Current_menu[1:], 1):
        end_line = WIDTH - (first_padding + menu_padding)
        print(f"{X:<{first_padding}}{i}: {selection:<{menu_padding}}{X:>{end_line-3}}")
    print(print_empty_line())
    print(print_empty_line())
    print(f"{X:<{first_padding}}b: {MAIN_MENU:<{menu_padding}}{X:>{end_line-3}}")
    print(print_border())
    print(print_empty_line())    
    print(f"x{text:^{WIDTH-2}}x")
    print(print_empty_line())    
    print(print_border())

def add_player_func(Current_menu):
    for i, element in enumerate(Current_menu[1:], 1):
        tmp = input(f"Please enter {element}: ")
        Current_menu[i] = element + " : " + tmp  
        dummy_player.append(tmp)
        clear_screen()
        dumme_menu_adding(Current_menu)
    clear_screen()
    dumme_menu_adding(Current_menu, "######  Association added successfully  ######")
    time.sleep(3)
    
def adding_association_func():
    clear_screen()
    print_Main_Menu()
    clear_screen()
    print_menu(Assiciations_list)
    clear_screen()
    dumme_menu_adding(add_association)
    add_player_func(add_association)
    clear_screen()


# clear_screen()
# print_menu(Assiciations_list)
# clear_screen()
# print_menu(Statistics)
# clear_screen()
# print_menu(Tournaments)
