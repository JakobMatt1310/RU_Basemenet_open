menu_list = ["Main menu", "Player", "Teams", "Associations", "Statistics", "Tournaments"]
player_list = ["PLayers menu", "Add player", "Edit player", "Delete player", "Assign as captain", "Back to Main Menu"]
teams_list = ["Team menu", "Add team", "Edit team", "Delete team", "Back to Main Menu"]
Assiciations_list = ["Associations menu", "Add association", "Edit association", "Assign team to association", "Back to Main Menu"]
Statistics = ["Statistics menu", "Top 50 players", "Current games", "Top 50 teams", "Back to Main Menu"]
Tournaments = ["Tournament menu", "Create a new tournament", "Edit a tournament", "View finished tournaments", "Back to Main Menu"]

all_menus = []

WIDTH = 90
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
    return f"{X:<{int(WIDTH/2)}}{X:>{int(WIDTH/2)}}"
    
def print_border():
    return ('x'*WIDTH)

def print_Main_Menu():
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
    return input("Enter input here")

def clear_screen():
    for i in range(20):
        print()
    
def print_menu(Current_menu):
    print_logo()
    first_padding = 15
    menu_padding = 70-first_padding
    print(print_border())
    print(f"x{Current_menu[0]:^{WIDTH-2}}x")
    for i, selection in enumerate(Current_menu[1:-1], 1):
        end_line = WIDTH - (first_padding + menu_padding)
        print(f"{X:<{first_padding}}{i}: {selection:<{menu_padding}}{X:>{end_line-3}}")
    print(print_empty_line())
    print(print_empty_line())
    print(f"{X:<{first_padding}}{len(Current_menu)}: {Current_menu[-1]:<{menu_padding}}{X:>{end_line-3}}")
    print(print_border())
    text = "Please input the number of selection you'd like to choose and press enter"
    print(print_empty_line())    
    print(f"x{text:^{WIDTH-2}}x")
    print(print_empty_line())    
    print(print_border())
    next = input("press enter")
    
    

    

next = print_Main_Menu()
clear_screen()
print_menu(player_list)
clear_screen()
print_menu(teams_list)
clear_screen()
print_menu(Assiciations_list)
clear_screen()
print_menu(Statistics)
clear_screen()
print_menu(Tournaments)
