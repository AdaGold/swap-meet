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

    # TODO: Is there a less repetitive way to do this?
    def __init__(self, category="Electronics", condition=0):
        self.category = category
        self.condition = condition

    # def __init__(self, category="Electronics", condition=0)
    #     super().__init__(category="Electronics", condition=0)

    def __str__(self):
        """Method to stringify Electronics. Returns default message."""
        return "A gadget full of buttons and secrets."
