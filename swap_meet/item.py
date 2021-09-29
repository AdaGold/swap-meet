class Item:
    """
    A class to represent an item traded at the swap meet.
    
    ...

    Attributes
    ----------
    category : str
        categorical descriptor for item

    condition : int
        condition rating for item, values 1 (poor) to 5 (like new)
    
    age : int
        default=None, age of item in years
        
    Methods
    ------- 
    __str__():
        Method to stringify Item. Returns default 'hello world!' message.
    
    condition_description(self):
        Method that describes Item based on it's numeric condition rating. 
    """

    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

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

