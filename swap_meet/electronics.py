class Electronics:
    pass

from swap_meet.item import Item
class Electronics(Item):
    """
    A class to represent an electronic item.
    ...
    Attributes
    ----------
    category : string (optional)
        a string that represents the category of the electronic item    
    condition:
        a float number between 0 and 5 that represents the current condition of the electronic item
    age :
        an integer that represents the age of the electronic item
    Methods
    -------
    __str__:
        - returns "A gadget full of buttons and secrets."
    """
    def __init__(self, condition = 0, age = 0):
        super().__init__(category = "Electronics", condition = condition, age = age)
        
    def __str__(self):
        return "A gadget full of buttons and secrets."