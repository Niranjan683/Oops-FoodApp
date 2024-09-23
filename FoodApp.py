#finally added to github

from models.acc import User
from models.UserManager import UserManager
from  controllers.MainMenu import MainMenu

class LoginSystem:

    def Login(self):
        
        email= input("Enter Mail : ")
        password= input('Enter Password : ')
        
        user = UserManager.FindUser(mail= email, password= password)
        
        if user is not None:
            print("loged in Successfully! ")
            menu = MainMenu()
            menu.Start()

            
            
        else:
            print(" Invalid MailId / Password. Please re-enter your MailId and Password  ")
    
    
    def Register(self):
        name= input(" Enter Name : ")
        mobile= int(input("Enter Mobile Number : "))
        email= input("Enter Mail : ")
        password= input('Enter Password : ')
        
        user=User(name=name, phn=mobile, mail=email, password=password)
        UserManager.add_user(user)


    def GuestLogin(self):
        pass

    def Exit(self):
        print("Thank You For Using Our Application")
        exit()

    def ValidateOption(self,option):
        getattr(self,option)()

    

class FoodApp:
    LoginOptions= {1: 'Login', 2:'Register',3:'Guestlogin',4:"Exit"}

    @staticmethod
    def Init():
        print("<<-- Welcome To Our Online Food Ordering App -->>")

        loginSysten= LoginSystem()

        while True:

            for option, value in FoodApp.LoginOptions.items():
                print(f"{option} : {value}", end=" | ")
            print()
       
            try:
                choice = int(input("Please Enter Your Choice : "))
                print(f"Great! You've selected  option {choice}")
                loginSysten.ValidateOption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid Choice type. you should give the choice as an Integer")
        




#c= FoodApp()
#c.Init()
FoodApp.Init()
