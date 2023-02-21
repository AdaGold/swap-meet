from swap_meet.item import Item

class Clothing(Item):
    category = "Clothing"

    def __init__(self, condition=None, id=None, fabric="Unknown"):
        super().__init__(condition=condition, id=id)
        self.fabric = fabric

    def get_category(self):
        return self.category

    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. It is made from {self.fabric} fabric."
