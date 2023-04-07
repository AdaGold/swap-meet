from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = 0, width = 0, length = 0, condition = 0, age=0):
        super().__init__(id, condition,age)
        self.width = width
        self.length = length

    def __str__(self):
        str1 = super().__str__()
        str2 = f"It takes up a {self.width} by {self.length} sized space."
        return str1 + " " + str2