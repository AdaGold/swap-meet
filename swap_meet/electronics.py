from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id =0, type = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.type = type

    def __str__(self):
        str1 = super().__str__()
        str2 = f"This is a {self.type} device."
        return str1 + " " + str2
