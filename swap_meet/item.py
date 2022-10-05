class Item:
    
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        conditions = {
            0: "You don't want this.",
            1: "Anything is cheap enough.",
            2: "It's OK.",
            3: "No major issues.",
            4: "Hardly worn and well taken care of.",
            5: "Gonna go fast!"
        }
        return f"{conditions[self.condition]}"