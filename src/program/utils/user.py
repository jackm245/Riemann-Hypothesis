# will store the users credentials

class ProgramUser():

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


User = ProgramUser()
