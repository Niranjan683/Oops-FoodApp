from .AbstractItem import AbstractItem
from .FoodMenu import FoodMenu

class Restaurant(AbstractItem):

    def __init__(self, name, rating, location,  offer): 
        super().__init__(name,rating)
        self.Location=location
        self.Offer=offer
        self.FoodMenu=[]

    @property
    def FoodMenus(self):
        return self.__FoodItems
    
    @FoodMenus.setter
    def FoodMenus(self,items):  
        for item in items:
            if not isinstance(item, FoodMenu):
                print("Invalid FoodMenu..........")
                return
        self.__FoodItems= items    
