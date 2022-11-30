


class MainMenu_UI:
    Menu_selection = {"Current Menu": "Main Menu", 
                    "View Players Statistics": ">>> Enter a players full name ", 
                    "View Team Statistics": ">>> ", 
                    "": ">>> "}    
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print_current_menu(self.Menu_selection)

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                menu = Moderator_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                menu = Player_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            else:
                print("invalid input, try again")
                

test = MainMenu_UI()
test.input_prompt()