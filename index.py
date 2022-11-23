#####################################################################
################## RU-OPEN-TOURNAMENT CLASSES #######################
#####################################################################

class User():
    def __init__(self, name, ssn, phone_nr, email):
        '''Constructor'''

        self.name = name
        self.ssn = ssn
        self.phone_nr = phone_nr
        self.email = email

    def __str__(self):
        '''String representation of the object'''
        return f"{self.name}\n{self.ssn}\n{self.phone_nr}\n{self.email}"


class Association():
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''
        return f"{self}"


class Team(Association):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class Player(User, Team):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class Captain(Player):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class Supervisor(User):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class Tournant(Supervisor):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class GameMatch(Tournant):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class GameMode(GameMatch):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class Round(GameMode):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


class Results(GameMatch):
    def __init__(self):
        '''Constructor'''

        pass

    def __str__(self):
        '''String representation of the object'''

        return f"{self}"


#####################################################################
################## MAIN PROGRAM #####################################
#####################################################################

def main():
    # pass
    user_name = input("Users name: ")
    user_ssn = input("Users social security number: ")
    user_phone_nr = input("Users phone number: ")
    user_email = input("Users email: ")
    user1 = User(user_name, user_ssn, user_phone_nr, user_email)
    print(user1)


if __name__ == "__main__":
    main()