from swap_meet.item import Item, CATEGORIES, CONDITION_DESCRIPTORS

class Clothing(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Clothing", condition = condition)
        # self.category = "Clothing"