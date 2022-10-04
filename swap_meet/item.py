class Item:
    def __init__(self, category=None):
        self.category = category if category is not None else ""
    
    def __str__(self):
        return "Hello World!"
