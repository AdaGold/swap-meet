from .item import Item

class Clothing(Item):
    """
    A class to represent an item of clothing traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        "Clothing", mandatory categorical descriptor for clothing

    condition : int
        condition rating for item, values 1 (poor) to 5 (like new)
    
    age : int
        default=None, age of item in years

    Methods
    ------- 
    __str__():
        Method to stringify Clothing. Returns default message.
    """

    def __init__(self, condition=0, age=None):
        super().__init__(category="Clothing", condition=condition, age=age)

    def __str__(self):
        """Method to stringify Clothing. Returns default message."""
        return "The finest clothing you could wear."