# from .clothing import Clothing
# from .decor import Decor 
# from .electronics import Electronics 

class Item:
    def __init__(self, category = '', condition=0.0): 
        self.category = category
        self.condition = condition
       

    def __str__(self): 
        return "Hello World!" 

    def condition_description(self): 
        if self.condition <= 0: 
            return "disgusting"
        if self.condition <= 1:
            return "needs a wash"
        if self.condition <= 2: 
            return "passable"
        if self.condition <= 3: 
            return "a bargain"
        if self.condition <= 4: 
            return "gross"
        if self.condition <= 5: 
            return "mint!"


    '''
    All three classes and the Item class have an instance method 
    named condition_description, which should describe the condition 
    in words based on the value, assuming they all range from 0 to 5. 
    These can be basic descriptions (eg. 'mint', 'heavily used') but 
    feel free to have fun with these 
    (e.g. 'You probably want a glove for this one..."). 
    The one requirement is that the condition_description for 
    all three classes above have the same behavior.
    '''
    
   

     






   

