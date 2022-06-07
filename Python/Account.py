from Base_variables import AccountStatus
class Account:
    def __init__(self, id, password, status=AccountStatus.Active):
        self.__id = id
        self.__password = password
        self.__status = status 

    def reset_password(self):
        password = True
        if password == True:
            pass
