class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition == 0:
            return "mint condition"
        elif self.condition <= 2:
            return "lightly used"
        elif self.condition <= 4:
            return "well loved"
        else:
            return "another man's treasure"
    