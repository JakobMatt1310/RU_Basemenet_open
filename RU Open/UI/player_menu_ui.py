from logic.player_logic import Player_Logic
from model.player import Player
from input_validators import *


class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("{}".format("Player Menu"))
        print("{}{}".format("1.", "Create player"))
        print("{}{}".format("2.", "List all players"))
        print("{}".format("b. to go back"))
    
    def input_prompt(self):
        while True:
            self.menu_output()
            command= input("Enter your command: ")
            command = command.lower()
            if command == "b":
                print("going back")
                return "b"
            elif command == "q":
                print("quitting")
            elif command == "1":
                c = Player()
                while True:
                    c.name = input("Enter the name of the player: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("name was too long")
                    except:
                        print("some error")
                c.ssn = input("Enter the social security number of the player: ")
                c.phone = input("Enter the players phone number: ")
                c.email = input("Enter the players email address: ")
                c.address = input("Enter the players home address: ")
                self.logic_wrapper.create_player(c)
            elif command == "2":
                result = self.logic_wrapper.get_all_players()
                for elem in result:
                    print(f"Name: {elem.name}, SSN: {elem.ssn}, Phone number: {elem.phone}, Email: {elem.email}, Home address: {elem.address}")
            else:
                print("invalid input, try again")