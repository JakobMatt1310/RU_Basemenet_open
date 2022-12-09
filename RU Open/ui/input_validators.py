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
    if len(association_name) < 2 or len(association_name) > 30:
        raise AssociationNameLengthException()

class TournamentNameLengthException(Exception):
    pass
class TournamentNameExists(Exception):
    pass
def validate_tournament_name(tournament_name, all_tournaments):
    all_names = [tournament.name for tournament in all_tournaments]
    if len(tournament_name) > 30:
        raise TournamentNameLengthException()
    for name in all_names:
        if tournament_name == name:
            raise TournamentNameExists()

class StartDateException(Exception):
    pass
class EndDateException(Exception):
    pass

def validate_start_date(start_date, current_date):
    if start_date.month > 12:
        raise StartDateException
    if start_date.day > 31:
        raise StartDateException
    if start_date.year < current_date.year:
        raise StartDateException
    if start_date.month < current_date.month:
        raise StartDateException
    if start_date.day < current_date.day:
        raise StartDateException

def validate_end_date(start_date, end_date):
    if end_date.month > 12:
        raise EndDateException
    if end_date.day > 31:
        raise EndDateException
    if start_date.year > end_date.year:
        raise EndDateException
    if start_date.month > end_date.month:
        raise EndDateException
    if start_date.day > end_date.day:
        raise EndDateException