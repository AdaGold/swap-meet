from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0, id=None, type="Unknown"):
        super().__init__(condition=condition, id=id)
        self.condition = condition
        self.type = type

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."