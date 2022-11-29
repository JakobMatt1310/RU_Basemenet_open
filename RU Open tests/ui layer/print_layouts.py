WIDTH = 140 # Default width of the program
HALF_WIDTH = int(WIDTH/2)
MAIN_MENU = "Back to main menu"
X = 'x' #letter representing seperation in program, header, main, etc..



def print_header_logo():
    print(print_border())
    print(print_empty_line())    
    logo_text = "RU Basement Open"
    print(f"{X}{logo_text:^{WIDTH-2}}{X}")
    print(print_empty_line())    
    print(print_border())
    print()

def print_empty_line():
    """Prints and empty line with symbols at each end of witdh
    """
    return f"{X:<{WIDTH-1}}{X}"
    
def print_border():
    return (X*WIDTH)

print_header_logo()
print_empty_line()