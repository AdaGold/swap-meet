import uuid

# unique_id = int(uuid.uuid4())
# print(unique_id)

class Item:
    def __init__(self, id = None):
        if id is None:
            id = int(uuid.uuid4())
        self.id = id

    def get_category(self):
        return type(self).__name__

