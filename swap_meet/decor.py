from .item import Item

class Decor(Item):
    """
    A class to represent an item of decor traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        "Decor", mandatory categorical descriptor for decor

    condition : int
        condition rating for item, values 1 (poor) to 5 (like new)
    
    age : int
        default=None, age of item in years

    Methods
    ------- 
    __str__():
        Method to stringify Decor. Returns default message.
    """
    def __init__(self, condition=0, age=None):
        super().__init__(category="Decor", condition=condition, age=age)

    def __str__(self):
        """Method to stringify Decor. Returns default message."""
        return "Something to decorate your space."
