import uuid

class Item:
    def __init__(self, id = 0):
        if id == 0:
            self.id = uuid.uuid1().int
        else:
            self.id = id

    def get_category(self):
        return Item.__name__
