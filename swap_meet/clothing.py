from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, fabric="Unknown", id=None, condition=0):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}." \
                f" It is made from {self.fabric} fabric."