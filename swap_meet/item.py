import uuid

class Item:
    def __init__(self, id = 0, condition = 0):
        if id == 0:
            self.id = uuid.uuid1().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        match self.condition:
            case 1:
                return "Heavily used"
            case 2:
                return "Regular used"
            case 3:
                return "Used"
            case 4:
                return "Almost new"
            case 5:
                return "Like new"
            case _:
                return "Default"
