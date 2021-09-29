from .item import Item

class Electronics(Item):
    """
    A class to represent an item of electronics traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        "Electronics", required categorical descriptor for electronics

    condition : int
        condition rating for item, values 1 (poor) to 5 (like new)
    
    age : int
        default=None, age of item in years

    Methods
    ------- 
    __str__():
        Method to stringify Electronics. Returns default message.
    """

    def __init__(self, condition=0, age=None):
        super().__init__(category="Electronics", condition=condition, age=age)

    def __str__(self):
        """Method to stringify Electronics. Returns default message."""
        return "A gadget full of buttons and secrets."
