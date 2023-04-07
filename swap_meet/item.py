import uuid

# unique_id = int(uuid.uuid4())
# print(unique_id)

class Item:
    def __init__(self, id = None, condition = 0):
        if id is None:
            id = int(uuid.uuid4())
        self.id = id

    def get_category(self):
        return type(self).__name__
        #return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."