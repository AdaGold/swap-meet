import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
            
    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        if self.condition == 0:
            return "Throw it away!"
        elif self.condition <= 1:
            return "It's seen better days"
        elif self.condition <=2:
            return "Meh"
        elif self.condition <=3:
            return "It's alright"
        elif self.condition <=4:
            return "Ok"
        elif self.condition <=5:
            return "Practically new"
        else:
            return "Invalid"
        