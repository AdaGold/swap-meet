from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category=None, condition=None):
        super().__init__("Clothing")

    def __str__(self):
        return "The finest clothing you could wear."