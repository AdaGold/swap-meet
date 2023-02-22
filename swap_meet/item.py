import uuid

class Item:
    def __init__(self, condition=0, id=None):
        self.condition = condition
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def condition_description(self):
        if self.condition > 3:
            return "It's great!"
        else:
            return "It stinks!"