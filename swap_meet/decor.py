from swap_meet.item import Item
class Decor(Item):
    
    def __init__(self, condition=0):
        super().__init__(category="Decor", condition=condition)
    
    def __str__(self):
        return f"Something to decorate your space."
    
    
        