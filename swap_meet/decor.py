from .item import Item

class Decor(Item):
    def __init__(self, id = None, width = 0, length = 0, condition = 0):
        super().__init__(id, condition)
        self.width = width
        self.length = length
    
    # Initially wrote get_category instance method to return "Decor". However, the code would be cleaner
    # if I removed this instance method altogether, referenced the __str__ method instance in the Item class,
    # and edited the return string in __str__ to remove any redundancy.
    
    def __str__(self):
        return f"{super().__str__()} It takes up a {self.width} by {self.length} sized space."