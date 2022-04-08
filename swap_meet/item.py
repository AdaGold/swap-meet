class Item:
    """
        A class to represent an item.

    ...

    Attributes
    ----------
    category : string (optional)
        a string that represents the category of the item
    condition:
        a float number between 0 and 5 that represents the current condition of the item

    age :
        an integer that represents the age of the item

    Methods
    -------
    condition_description:
        - returns "Just trash it!" if condition is between 0 and 1
        - returns "Enjoy the last moments!" if condition is between 1 and 2
        - returns "As good as 30 year old wine!" if condition is between 2 and 3
        - returns "Better than the new one" if condition is between 3 and 4
        - returns "No need to ask!" if condition is between 4 and 5
        - returns False if condition is not between 0 and 5
    """
    def __init__(self,category = "", condition = 0.0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age
    def __str__(self):
        
        return f"Hello World!"
    
    def condition_description(self):
        if 0 <= self.condition < 1:
            return "Just trash it!"
        elif 1 <= self.condition < 2:
            return "Enjoy the last moments!"
        elif 2 <= self.condition < 3:
            return "As good as 30 year old wine!"
        elif 3 <= self.condition < 4:
            return "Better than the new one"
        elif 4 <= self.condition <= 5:
            return "No need to ask!"
        else:
            return False
    
        
    
    # pass