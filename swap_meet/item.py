# from swap_meet.vendor import Vendor

class Item:
    
    def __init__(self, category = None, condition = 0, age = 0):
        self.category = category if category is not None else ""
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        self.condition = round(self.condition)
        condition_dict = {
            0 : "garbage",
            1 : "bad",
            2 : "used",
            3 : "lightly used",
            4 : "like new",
            5 : "new"
        }
        return condition_dict[self.condition]

