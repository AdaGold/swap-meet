class Clothing:
    """
    A class to represent an item of clothing traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        categorical descriptor for clothing

    Methods
    ------- 
    __str__():
        Method to stringify Clothing. Returns default message.
    """

    def __init__(self, category="Clothing"):
        self.category = category

    def __str__(self):
        """Method to stringify Clothing. Returns default message."""
        return "The finest clothing you could wear."