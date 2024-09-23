from .FoodManager import FoodManager

class MainMenu:
    __Options = {1: "Show_Restaurant", 2: "Show_FoodItems", 3: "Search_restaurant", 4: "Search_FoodItems", 5: "Log_out"}
    
    def __init__(self):
        self.FoodManager = FoodManager()

    def Start(self):
        for option in MainMenu.__Options:
            print(f" {option}.{MainMenu.__Options[option]}",end = " ")
        print()

        try:
            choice = int(input("Please Enter Your Choice : "))
            Value = MainMenu.__Options[choice]
        except (ValueError,KeyError):
            print("Invalid Input... Please Enter the valid Choice")
        

