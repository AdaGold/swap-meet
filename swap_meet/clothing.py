from swap_meet.item import Item
class Clothing(Item):

    """
        A class to represent a cloth.

    ...

    Attributes
    ----------
    category : string (optional)
        a string that represents the category of the cloth    
    condition:
        a float number between 0 and 5 that represents the current condition of the cloth
    age :
        an integer that represents the age of the cloth
    Methods
    -------
    __str__:
        - returns "The finest clothing you could wear."
    """
    def __init__(self, condition = 0, age = 0):
        super().__init__(category = "Clothing", condition = condition, age = age)
        
    def __str__(self):
        return "The finest clothing you could wear."


    # pass