from .item import Item

class Electronics(Item):
    """
    A class to represent an item of electronics traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        categorical descriptor for electronics

    Methods
    ------- 
    __str__():
        Method to stringify Electronics. Returns default message.
    """

    #Inherits Item init, requiring "Electronics" as category
    def __init__(self, condition=0):
        super().__init__(category="Electronics", condition=condition)

    def __str__(self):
        """Method to stringify Electronics. Returns default message."""
        return "A gadget full of buttons and secrets."
