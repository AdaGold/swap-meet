import uuid

class Item:
    def __init__(self, id = 0, condition = 0, age = 100):
        if id == 0:
            self.id = uuid.uuid1().int
        else:
            self.id = id
        self.condition = condition
        self.age = age

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition == 1:
            return "Heavily used"
        if self.condition == 2:
            return "Regular used"
        if self.condition == 3:
            return "Used"
        if self.condition == 4:
            return "Almost new"
        if self.condition == 5:
            return "Like new"
