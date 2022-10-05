#from item import Item

class Decor():
    
    def __init__(self, category = "Decor", condition = 0):
        #super().__init__(category = None, condition = 0)
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."