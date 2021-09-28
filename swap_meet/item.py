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
    
    condition_description(self):
        Method that describes Item based on it's condition rating. 
    """

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        """Method to stringify Item. Returns default message."""
        return "Hello World!"

    def condition_description(self):
        """Method that describes Item based on it's condition rating."""
        if self.condition > 4:
            return "Like new!"
        elif self.condition > 3:
            return "In good shape!"
        elif self.condition > 2:
            return "Fair..."
        elif self.condition > 1:
            return "Passable, but not great."
        else:
            return "Poor Quality"

