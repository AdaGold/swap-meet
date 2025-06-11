from .item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.type = type

    # Initially wrote get_category instance method to return "Electronics". However, the code would be cleaner
    # if I removed this instance method altogether, referenced the __str__ method instance in the Item class,
    # and edited the return string in __str__ to remove any redundancy.

    def __str__(self):
        return f"{super().__str__()} This is a {self.type} device."

