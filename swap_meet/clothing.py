from swap_meet.item import Item
class Clothing(Item):

    # instantiate a class: this is where __init__ and attributes go
    def __init__(self, condition=0):
        super().__init__(category="Clothing", condition=condition)
    
    def __str__(self):
        return f"The finest clothing you could wear."
    
    
