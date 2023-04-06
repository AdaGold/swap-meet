import uuid

class Item:
    def __init__(self, id=None, condition=0, age=0):
        if not isinstance(id, int) and id is not None:
            raise TypeError("id must be an integer")
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age
            
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
            return "Pretty good!"
        elif self.condition <=5:
            return "Practically new"
        else:
            return "Invalid condition rating."
        