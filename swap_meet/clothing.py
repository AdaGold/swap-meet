from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Clothing", condition = condition)