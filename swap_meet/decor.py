from swap_meet.item import Item

class Decor(Item):
    category = "Decor"

    def __init__(self, condition=None, id=None, width=0, length=0):
        super().__init__(condition=condition, id=id)
        self.width = width
        self.length = length


    def get_category(self):
        return self.category

    def __str__(self):
        return f"An object of type {self.category} with id {self.id}. It takes up a {self.width} by {self.length} sized space."
