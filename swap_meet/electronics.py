from swap_meet.item import Item, CATEGORIES, CONDITION_DESCRIPTORS

class Electronics(Item):
    def __init__(self, condition = 0):
        super().__init__(category = "Electronics", condition = condition)
        # self.category = "Electronics"