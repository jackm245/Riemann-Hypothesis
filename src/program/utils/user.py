"""
user.py
=======

Contains the ProgramUser class

A single instance of this class is used to store the
current user's credentials and data
"""

class ProgramUser():

    """
    The ProgramUser class is used to store the user's credentials

    The class contains Setter and Getter methods in order to interact with these
    credentials throughout the runtime of the program
    """

    def __init__(self, signed_in=False, user_id=None, username=None, email=None):
        super(ProgramUser, self).__init__()
        self.signed_in = signed_in
        self.user_id = user_id
        self.username = username
        self.email = email

    def SetSignedIn(self, signed_in):
        self.signed_in = signed_in

    def SetUserID(self, user_id):
        self.user_id = user_id

    def SetUsername(self, username):
        self.username = username

    def SetEmail(self, email):
        self.email = email

    def GetSignedIn(self):
        return self.signed_in

    def GetUserID(self):
        return self.user_id

    def GetUsername(self):
        return self.username

    def GetEmail(self):
        return self.email


"""
This instance of the ProgramUser is imported by various other namespaces
and is used throughout the program, in order to interact with the ProgramUser
class
"""
User = ProgramUser()
