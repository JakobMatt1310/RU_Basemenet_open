menu_list = ["Main menu", "Player", "Teams", "Associations", "Statistics", "Tournaments"]
BORDER = 'x'
WIDTH = 110
X = 'x'
def print_logo():
    print(print_border())
    print(f"{X:<{int(WIDTH/2)}}{X:>{int(WIDTH/2)}}")
    logo_text = "RU Basement Open"
    logo_padding = int(len(logo_text)/2)
    print(f"{X:<{int(WIDTH/2-logo_padding)}}{logo_text}{X:>{int(WIDTH/2-logo_padding)}}")
    print(f"{X:<{int(WIDTH/2)}}{X:>{int(WIDTH/2)}}")
    print(print_border())
    print()
    pass

def print_border():
    return ('x'*WIDTH)

def print_dart():
    print_logo()
    first_padding = 15
    menu_padding = 70-first_padding
    print(print_border())
    for i, selection in enumerate(menu_list):
        end_line = WIDTH - (first_padding + menu_padding)
        print(f"{X:<{first_padding}}{i+1}: {selection:<{menu_padding}}{X:>{end_line-3}}")
    print(print_border())
    text = "Please input the number of selection you'd like to choose and press enter"
    end_line = WIDTH-(first_padding+menu_padding)
    print(f"{X:<{(first_padding+menu_padding)}}{X:>{end_line}}")
    end_line = WIDTH-(first_padding+len(text))
    print(f"{X:<{(first_padding)}}{text}{X:>{end_line}}")
    end_line = WIDTH-(first_padding+menu_padding)
    print(f"{X:<{(first_padding+menu_padding)}}{X:>{end_line}}")
    print(print_border())
    # user_input = input("Enter input here")
    
    

    

print_dart()