from model.association import Association
from model.team import Team
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *
from ui.input_validators import *


class Associations_UI:
    Menu_selection = {"Current Menu": "Associations", 
                    "Create Association": ">>> Creates an association",
                    "Edit Association": ">>> Select to edit association",
                    "View Associations": ">>> Lists every association",
                    "Remove Association": ">>> Deletes an association and the teams within"} 
       
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.Menu_selection)
    def create_association(self):
        pass
    def create_new_team(self):
        """Creates a new team, when selected Moderator HAS to create a team, with all four players and a captain.
        """
        team = Team()
        team.team_name = self.new_team_name()
        all_associations = self.logic_wrapper.get_all_associations()
        team.association_name, team.association_id = self.association_name(all_associations)
        
        self.logic_wrapper.create_team(team)
        print_current_team_player_list([" "], team)
        player_list = []
        for i in range(4): # Moderator has to create 4 players and select a captain
            player = Player()
            player.ssn = self.new_player_ssn()
            player.name = self.new_player_name()
            player.phone = self.new_player_phone()
            player.email = self.new_player_email()
            player.address = self.new_player_address()
            player.team_id = team.id
                        
            self.logic_wrapper.create_player(player)
            player_list.append(player.name)
            print_current_team_player_list(player_list, team)
            
        while True:
            selection = input("Select player to be captain for team: ")
            if selection == "1" or selection == "2" or selection == "3" or selection == "4":
                team.captain_name = player_list[int(selection)-1]
                self.logic_wrapper.update_team_captain(team)
                print("***************Team has been created****************")
                break
            else:
                print("Invalid input, please try again (A captain must be chosen")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command: ").lower()
            if command == "b":
                return
            if command == "q":
                print("Goodbye")
                return "q"
            elif command == "1":
                self.create_association()
                
            elif command == "2":
                association = Association()
                while True:
                    association.association_name = input("Enter the name of the association: ")
                    association.association_phone = input("Enter the phone number for the association: ")
                    association.association_address = input("Enter the address of the association: ")
                    try:
                        validate_association_name(association.association_name)
                        check_phone_length(association.association_phone)
                        check_phone_isdigit(association.association_phone)
                        
                        break
                    except AssociationNameLengthException:
                        print("name was too long")
                    except PhoneNumberCharacterException:
                        print("The phone number can only consist of NUMBERS and no other characters.")
                    except PhoneNumberLengthException:
                        print("Phone number length invalid, the phone number must be a 7 digit number.")
                    except:
                        print("some error")
                
                self.logic_wrapper.create_association(association)
            elif command == "3":
                print("edit the association")
                pass
            elif command == "4":
                self.logic_wrapper.remove_association(association)
                
            else:
                print("invalid input, try again")