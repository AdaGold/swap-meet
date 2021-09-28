from .item import Item

class Decor(Item):
    """
    A class to represent an item of decor traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        categorical descriptor for decor

    Methods
    ------- 
    __str__():
        Method to stringify Decor. Returns default message.
    """

    def __init__(self, category="Decor", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        """Method to stringify Decor. Returns default message."""
        return "Something to decorate your space."
