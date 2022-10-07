class Item:
    
    def __init__(self, category = None, condition = 0):
        if category is None:
            category = ""
        self.category = category 
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition >= 5:
            return "Perfect in every way!"
        elif self.condition >= 4:
            return "Not bad, not bad"
        elif self.condition >= 3:
            return "I've seen worse"
        elif self.condition >= 2:
            return "Well, at least it's free"
        elif self.condition >= 1:
            return "Better than a poke in the eye with a sharp stick"
        elif self.condition > 0:
            return "Oof"
        