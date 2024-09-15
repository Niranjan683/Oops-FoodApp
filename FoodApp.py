#finally added to github

from models.User import User
from models.UserManager import UserManager

class LoginSystem:

    def Login(self):
        
        email= input("Enter Mail : ")
        password= input('Enter Password : ')
        
        user = UserManager.FindUser(mail= email, password= password)
        
        if user is not None:
            print("loged in Successfully! ")
            pass # NExt step
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

    def ValidateOption(self,option):
        if option == 1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.GuestLogin()
        elif option== 4:
            print("Thank You For Using Our Application")
            exit()
        else:
            print(" Invalid Choice... Please Retry. ")



class FoodApp:
    LoginOptions= {1: 'Log-in', 2:'register',3:'Guest',4:"Exit"}

    @staticmethod
    def Init():
        print("<<-- Welcome To Our Online Food Ordering App -->>")

        loginSysten= LoginSystem()

        while True:

            for option, value in FoodApp.LoginOptions.items():
                print(f"{option} : {value}", end=" | ")
            print()
       
            try:
                choice= int(input("Please Enter Your Choice : "))
                print(f"Great! You've selected  option {choice}")
                loginSysten.ValidateOption(choice)
            except ValueError:
                print("Invalid Choice type. you should give the choice as an Integer")
        




#c= FoodApp()
#c.Init()
FoodApp.Init()
