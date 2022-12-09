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
                    association.name = self.new_association_name()
                    association.phone = self.new_association_phone()
                    association.address = self.new_association_address()
                    try:
                        validate_association_name(association.name)
                        # check_phone_length(association.phone)
                        # check_phone_isdigit(association.phone)
                        
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
                 #print(association_to_edit)
            else:
                return_command = ""
            if association_to_edit != None:
                edit_info = edit_association_only_menu(association_to_edit)
                if edit_info == 'b':
                    print("Going back")
                    return
                elif edit_info == "1":
                    return_command = self.change_association_name(association_to_edit)
                elif edit_info == "2":
                    return_command = self.change_association_phone(association_to_edit)
                elif edit_info == "3":
                    return_command = self.change_association_address(association_to_edit)
               

    def change_association_name(self, association_to_edit):
        new_association_name = self.new_association_name(1)
        confirm_name = input(f"The team will be renamed {new_association_name}. Would you like to confirm (yes/no)?  ").lower()
        while True:
            if confirm_name == 'yes':
                association_to_edit.association_name = new_association_name
                success = self.logic_wrapper.update_association_name(association_to_edit)
                if success == True:
                    print(f"Association name has successfully been updated to {new_association_name}")
                    input("Press enter to return: ")
                    return "back"
                else:
                    print("Association name failed to update, try again or go back")
            elif confirm_name =='no':
                return self.back_command()
            else:
                print('Invalid input, please answer with "yes" or "no"')

    
    def change_association_phone(self, association_to_edit: Association):
        new_association_phone = self.new_association_phone(1)
        confirm_name = input(f"The phone number will be changed to {new_association_phone}. Would you like to confirm (yes/no)?  ").lower()
        while True:
            if confirm_name == 'yes':
                association_to_edit.association_phone = new_association_phone
                success = self.logic_wrapper.update_association_phone(association_to_edit)
                if success == True:
                    print(f"Association phone number has successfully been updated to {new_association_phone}")
                    input("Press enter to return: ")
                    return "back"
                else:
                    print("Association phone failed to update, try again or go back")
            elif confirm_name =='no':
                return self.back_command()
            else:
                print('Invalid input, please answer with "yes" or "no"')

    
    def change_association_address(self, association_to_edit: Association):
        new_association_address = self.new_association_address(1)
        confirm_name = input(f"The address will be changed to {new_association_address}. Would you like to confirm (yes/no)?  ").lower()
        while True:
            if confirm_name == 'yes':
                association_to_edit.association_address = new_association_address
                success = self.logic_wrapper.update_association_address(association_to_edit)
                if success == True:
                    print(f"Association address has successfully been updated to {new_association_address}")
                    input("Press enter to return: ")
                    return "back"
                else:
                    print("Association address failed to update, try again or go back")
            elif confirm_name =='no':
                return self.back_command()
            else:
                print('Invalid input, please answer with "yes" or "no"')



    def new_association_name(self, rename=0):
        while True:
            if rename == 0:            
                association_name = input("Enter the name of the association (max 30 char): ")
            else:
                association_name = input("Enter the desired new name for the association (max 30 char): ")
            try:
                validate_association_name(association_name)
                break
            except AssociationNameLengthException:
                print("Name was too long or to short")
            except:
                print("Something went wrong, please try again.")
        return association_name

    def new_association_phone(self, rename=0):
        while True:
            if rename == 0:            
                association_phone = input("Enter the phone of the association (7 digits): ")
            else:
                association_phone = input("Enter the desired new phone for the association (7 digits): ")
            try:
                validate_phonenumber(association_phone)
                break
            except PhoneNumberException:
                print("Phone number length incorrect.")
            except:
                print("Something went wrong, please try again.")
        return association_phone

    def new_association_address(self, rename=0):
        while True:
            if rename == 0:            
                association_address = input("Enter the address of the association (Street name and number): ")
            else:
                association_address = input("Enter the desired new address for the association (Street name and number): ")
            try:
                validate_home_address(association_address)
                break
            except HomeAddressException:
                print("Illegal home address.")
            except:
                print("Something went wrong, please try again.")
        return association_address