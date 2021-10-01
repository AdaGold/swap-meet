class Item:
    def __init__(self, condition = 0, category = ""):
        self.condition = condition
        self.category = category

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition < 2:
            return "Bare hands should be ok"
        elif 2 <= self.condition < 4:
            return "Gloves are recommended but not required"
        else:
            return "You probably want a glove for this one"