class Item:
    def __init__(self,category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age
    def __str__(self):
        
        return f"Hello World!"
    
    def condition_description(self):
        if 0 <= self.condition < 1:
            return "Just trash it!"
        elif 1 <= self.condition < 2:
            return "Enjoy the last moments!"
        elif 2 <= self.condition < 3:
            return "As good as 30 year old wine!"
        elif 3 <= self.condition < 4:
            return "Better than the new one"
        elif 4 <= self.condition <= 5:
            return "No need to ask!"
        else:
            return False
    
        
    
    # pass