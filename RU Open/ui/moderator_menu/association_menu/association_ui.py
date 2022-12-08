from model.association import Association
from model.team import Team
from logic.logic_wrapper import Logic_Wrapper
from ui.print_layouts import *
from ui.input_validators import *

class Association_UI:
    Menu_selection = {"Current Menu": "Associations", 
                    "View Associations": ">>> Lists every association",
                    "Create Association": ">>> Creates an association",
                    "Edit Association": ">>> Modify menu for selected association",
                    "Remove Association": ">>> Deletes an association and the teams within"}    
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print_current_menu(self.Menu_selection)

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
                associations_all = self.logic_wrapper.get_all_associations()
                teams_no = self.logic_wrapper.teams_in_association()
                view_association(associations_all, teams_no)

            elif command == "2":
                association = Association()
                while True:
                    association.association_name = input("Enter the name of the association: ")
                    association.association_phone = input("Enter the phone number for the association: ")
                    association.association_address = input("Enter the address of the association: ")
                    try:
                        validate_association_name(association.association_name)
                        # check_phone_length(association.association_phone)
                        # check_phone_isdigit(association.association_phone)
                        
                        break
                    except AssociationNameLengthException:
                        print("name was too long")
                    # except PhoneNumberCharacterException:
                    #     print("The phone number can only consist of NUMBERS and no other characters.")
                    # except PhoneNumberLengthException:
                    #     print("Phone number length invalid, the phone number must be a 7 digit number.")
                    except:
                        print("There was an error, something is wrong with your input.")
                
                self.logic_wrapper.create_association(association)
            elif command == "3": #to edit association
                #association_to_edit = input("Please type the name of the Association you wish to edit: ")
                self.edit_an_association()
                
            elif command == "4": #to delete an association
                #old_list_lenght = len(list_of_associations)
                association.association_to_delete = input("Please enter the name of the association you wish to delete: ")
                #something cool happens
                #ass has been deleted
                #new_list_length = len(list_of_associations)
                #if new == old:
                    #print(seems like that association does not exist)
                #elif new == old - 1:
                    #print(the assocition association_to_delete has been deleted)                
                
            else:
                print("invalid input, try again")
    


    def edit_an_association(self):
        """this function prompts for edit a team"""
        return_command = ""
        while True:
            if return_command != "back":
                 association_to_edit = input("Please type the name of the Association you wish to edit: ")
                 association_to_edit = self.logic_wrapper.get_association(association_to_edit)
                 print(association_to_edit)
               