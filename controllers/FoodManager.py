from ..models.FoodItems import FoodItems
from models.FoodMenu import FoodMenu
from models.Restaurent import Restaurant
#class foo

class FoodManager:
    def __init__ (self):
        self.Restaurants = self.__PrepareRestaurant()

        
    def __PrepareFoodItems(self):
        item1 = FoodItems(name="MuttonBiriyani",rating=4,price=100,description="***")
        item2 = FoodItems(name="chickenBiriyani",rating=4.5,price=150,description="***")
        item3 = FoodItems(name="RoastDosa",rating=3,price=70,description="***")
        item4 = FoodItems(name="Idly",rating=3.5,price=50,description="***")
        item5 = FoodItems(name="Noodles",rating=4.5,price=65,description="***")
        item6 = FoodItems(name="FriedRice",rating=4.1,price=120,description="***")
        return [item1,item2,item3,item4,item5,item6]

    def   __PrepareFoodMenus(self):
        FoodItems= self.__PrepareFoodItems()
        menu1 = FoodMenu("veg")
        menu1.FoodItems = [FoodItems[2], FoodItems[3]]
        
        menu2 = FoodMenu("Non-veg")
        menu2.FoodItems=[FoodItems[0],FoodItems[1]]

        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [FoodItems[4],FoodItems[5]]
        return [menu1, menu2, menu3]

    def __PrepareRestaurant(self):
        FoodMenus = self.__PrepareFoodMenus()
        res1= Restaurant(name="A2b",rating=4.5,location='kovai',offer=10)
        res1.FoodMenu=[FoodMenus[0]]
        res2= Restaurant(name="MuniyandiVilas",rating=4.5,location='Tirupur',offer=20)
        res2.FoodMenu = [FoodMenus[0], FoodMenus[1]]
        res3= Restaurant(name="KFC",rating=4.5,location='Chennai',offer=15)
        res3.FoodMenu = [FoodMenus[1], FoodMenus[2]]

        return [res1, res2, res3]





