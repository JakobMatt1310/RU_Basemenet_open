class NameLengthException(Exception):
    pass

def validate_name(name):
    if len(name) >= 45:
        raise NameLengthException()