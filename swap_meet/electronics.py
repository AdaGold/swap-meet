class Electronics:
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

    def __init__(self, category="Electronics"):
        self.category = category

    def __str__(self):
        """Method to stringify Electronics. Returns default message."""
        return "A gadget full of buttons and secrets."
