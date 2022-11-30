import os

WIDTH = 120 # Default width of the program
HALF_WIDTH = int(WIDTH/2)
THIRD_WIDTH = int(WIDTH/3)
MENU_LEN = 47 # How long the menu is
MENU_PAD = HALF_WIDTH-MENU_LEN # How much is padded from left to right
X = 'x' #letter representing seperation in program, header, main, etc..




def print_header_logo():
    """Prints the header with title printed"""
    print_border()
    print_empty_line()   
    logo_text = "RU Basement Open"
    print(f"{X}{logo_text:^{WIDTH-2}}{X}")
    print_empty_line()   
    print_border()
    print()

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

def create_menu(list_to_print):
    pass

def edit_menu(list_to_edit):
    pass


# print_current_menu(Menu_selection)
