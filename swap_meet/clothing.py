from .item import Item

class Clothing(Item):
    def __init__(self, id = None, fabric = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.fabric = fabric
    
    # Initially wrote get_category instance method to return "Clothing". However, the code would be cleaner
    # if I removed this instance method altogether, referenced the __str__ method instance in the Item class,
    # and edited the return string in __str__ to remove any redundancy.
       
    def __str__(self):
        return f"{super().__str__()} It is made from {self.fabric} fabric."
        