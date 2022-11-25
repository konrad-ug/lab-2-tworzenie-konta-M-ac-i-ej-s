class RejestrKont:
    users = []
    
    @classmethod
    def addUser(cls, konto):
        cls.users.insert(0,konto)

    @classmethod
    def searchUser(cls, pesel):
        for user in cls.users:
            if(user.pesel == pesel):
                return user
        return None        

    @classmethod
    def howManyUsers(cls):
        return len(cls.users)    