class Item:
    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition
    def __str__(self):
        return "Hello World!"
    def condition_description(self):
        if self.condition <= 1:
            return "OMG Don't swap for this!"
        elif self.condition <= 2:
            return "This item is well-loved"
        elif self.condition <= 3:
            return "This is average qualtiy"
        elif self.condition <= 4:
            return "This is in pretty good condition"
        else:
            return "Love this.  Great condition."