class Item:
    """
    A class to represent an item traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        categorical descriptor for item

    Methods
    ------- 
    __str__():
        Method to stringify Item. Returns default 'hello world!' message.
    """

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        """Method to stringify Item. Returns default message."""
        return "Hello World!"

