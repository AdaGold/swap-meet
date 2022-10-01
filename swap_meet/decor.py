from swap_meet.item import Item
class Decor(Item):
    """
    A class to represent a decor.
    ...

    Attributes
    ----------
    category : string (optional)
        a string that represents the category of the decor    
    condition:
        a float number between 0 and 5 that represents the current condition of the decor
    age :
        an integer that represents the age of the decor
    Methods
    -------
    __str__:
        - returns "Something to decorate your space."
    """
    def __init__(self, condition = 0, age = 0):
        super().__init__(category = "Decor", condition = condition, age = age)
        
    def __str__(self):
        return "Something to decorate your space."