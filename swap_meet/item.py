# from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, category = None, condition = 0):
        self.category = category if category is not None else ""
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        self.condition = round(self.condition)
        if self.condition == 0:
            return "garbage"
        elif self.condition == 1:
            return "bad"
        elif self.condition == 2:
            return "used"
        elif self.condition == 3:
            return "lightly used"
        elif self.condition == 4:
            return "like new"
        else:
            return "new"

