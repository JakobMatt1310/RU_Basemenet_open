#from email_validator import validate_email, EmailNotValidError

class NameLengthException(Exception):
    pass

def validate_name(name):
    if len(name) >= 45:
        raise NameLengthException()

class SsnLengthException(Exception):
    pass

def validate_ssn(ssn):
    if len(ssn) != 10:
        raise SsnLengthException()

class PhoneNumberLengthException(Exception):
    pass
def check_phone_length(phone)
    if len(phone) != 7:
        raise PhoneNumberLengthException()
        
class PhoneNumberCharacterException(Exception):
    pass
def check_phone_isdigit(phone)
    if int(phone).isdigit() == False:
        raise PhoneNumberLengthException()

#class InvalidEmailException(Exception):
#    pass
#def is_valid_email(email):
#    if validate_email(email) == False:
#        raise InvalidEmailException

class TeamNameLengthException(Exception):
    pass

def validate_team_name(team_name):
    if len(team_name) < 3 or len(team_name) > 25:
        raise TeamNameLengthException()
