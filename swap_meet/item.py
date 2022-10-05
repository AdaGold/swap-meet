class Item:
    def __init__(self, category=None, condition=0.0):
        self.category = category if category is not None else ""
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self, condition):
        if condition in range(0,6):
            if condition == 0:
                return "Are you sure you want this?"
            if condition == 1:
                return "Condition kinda poor..."
            if condition == 2:
                return "You get what pay for!"
            if condition == 3:
                return "Not bad *shrug*"
            if condition == 4:
                return "Pretty good find. Nice."
            if condition == 5:
                return "AMAZINGGGG. Literally couldn't do better."
    
