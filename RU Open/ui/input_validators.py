#from email_validator import validate_email, EmailNotValidError

class NameLengthException(Exception):
    pass
def validate_name(name):
    if len(name) < 3 or len(name) > 30:
        raise NameLengthException()

class SsnLengthException(Exception):
    pass
def validate_ssn(ssn):
    if len(ssn) != 10:
        raise SsnLengthException()
    try:
        ssn = int(ssn)
    except ValueError:
        raise SsnLengthException()

class PhoneNumberException(Exception):
    pass
def validate_phonenumber(phone):
    if len(phone) != 7:
        raise PhoneNumberException()
    try:
        phone = int(phone)
    except ValueError:
        raise PhoneNumberException()

class InvalidEmailException(Exception):
   pass
def validate_email(email):
        if len(email) < 12 or len(email) > 30:
            raise InvalidEmailException()

        else:
            att = 0
            ending = 0
            for letter in email:
                if letter == "@":
                    att += 1
            if letter[-3:] == ".is":
                ending += 1
            elif letter[-4:] == ".com":
                ending += 1
            elif letter[-4:] == ".net":
                ending += 1
                    
                    
            if att != 1 and ending != 1:
                raise InvalidEmailException()

class HomeAddressException(Exception):
    pass
def validate_home_address(home_address):
    if len(home_address) > 30 or len(home_address) < 3:
        raise HomeAddressException()
    if home_address[-1].isdigit() == False:
        if home_address[-2].isdigit() == False:
            raise HomeAddressException()

class TeamNameLengthException(Exception):
    pass
def validate_team_name(team_name):
    if len(team_name) < 3 or len(team_name) > 30:
        raise TeamNameLengthException()

class AssociationNameLengthException(Exception):
    pass
def validate_association_name(association_name):
    if len(association_name) < 3 or len(association_name) > 30:
        raise AssociationNameLengthException()

class TournamentNameLengthException(Exception):
    pass
def validate_tournament_name(tournament_name):
    if len(tournament_name) < 3 or len(tournament_name) > 30:
        raise TournamentNameLengthException()
