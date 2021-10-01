class Item:
    def __init__(self, category = None, condition = 0):
        if not category:
            self.category = ""
        else:
            self.category = category

        self.condition = condition    

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 0 and self.condition < 2.5:
            return "Slightly used"
        elif self.condition >= 2.5 and self.condition <= 5:
            return "Looks great"
        
    
    
        


