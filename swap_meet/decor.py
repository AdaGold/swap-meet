from swap_meet.item import Item
# , CATEGORIES, CONDITION_DESCRIPTORS

class Decor(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Decor", condition = condition)
        # self.category = "Decor"