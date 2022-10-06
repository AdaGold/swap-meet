class Item:
    def __init__(self, category=None, condition=0, age=0):
        self.category = category if category is not None else ""
        self.condition = condition
        self.age = age
        
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if not self.condition:
            return None
        elif self.condition <= 3:
            return "Are you sure you want this?"

        elif self.condition <= 5:
            return "Pretty good find. Nice."
    
    
