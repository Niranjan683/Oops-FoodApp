from .AbstractItem import AbstractItem

class FoodItems (AbstractItem):
    def __init__(self, name, rating, price, description):
        super().__init__(name=name,rating=rating)
        self.Price = price
        self.Description = description