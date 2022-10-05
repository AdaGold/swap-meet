class Item:
    
    def __init__(self, category = None, condition = 0):
        if category is None:
            category = ""
        self.category = category 
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self, num):
        if num >= 5:
            return "Perfect in every way!"
        elif num >= 4:
            return "Not bad, not bad"
        elif num >= 3:
            return "I've seen worse"
        elif num >= 2:
            return "Well, at least it's free"
        elif num >= 1:
            return "Better than a poke in the eye with a sharp stick"
        elif num > 0:
            return "Oof"
        