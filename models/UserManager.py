try:
    from .acc import User
except Exception:
    import sys,os
    print(sys.path)
    print(os.getcwd())

class UserManager:
    __User = []
    @classmethod
    def add_user(cls,user):
        if isinstance(user, User):
            cls.__User.append(user)
            print("You have been successfully registered")
        else:
            print("Invalid User")
    @classmethod
    def FindUser(cls,mail, password):
        for user in UserManager.__User:
            if user.mail == mail and user.password== password :
                return user
