#from item import Item

class Electronics():
    
    def __init__(self, category = "Electronics", condition = 0):
        #super().__init__(category = None, condition = 0)
        self.category = category
        self.condition = condition

    def __str__(self):
        return "A gadget full of buttons and secrets."
