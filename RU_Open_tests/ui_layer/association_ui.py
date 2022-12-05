from model.association_model_dummy import Association
from model.team_model_dummy import Team
from logic_wrapper_dummy import Logic_Wrapper
from print_layouts import *
from input_validators import *


class Associations_UI:
    Menu_selection = {"Current Menu": "Associations", 
                    "View Associations": ">>> Lists every association",
                    "Create Association": ">>> Creates an association",
                    "Edit Association": ">>> Modification menu for the selected association",
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
                self.logic_wrapper.get_all_associations()
                return
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
                list_of_associations = self.logic_wrapper.get_all_associations()
                association_to_delete = input("Please enter the name of the association that you want to remove: ")
                if association_to_delete in list_of_associations:
                    confirm = input("Removing this association will delete all teams and players within the association, Are you sure you want to remove this association? (yes/no)").islower()
                    if confirm == 'yes':
                        self.logic_wrapper.remove_association(association)
                    elif confirm == 'no':
                        print("No action was performed, the association will stay active.")
                    else:
                        print('Invalid input, please answer with "yes" or "no" ')
                        
                        
                
            else:
                print("invalid input, try again")