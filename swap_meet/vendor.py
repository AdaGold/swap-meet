class Vendor:
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category=""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items

    
    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        
        self.inventory.remove(my_item)
        vendor_friend.inventory.append(my_item)

        vendor_friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
        
    def swap_first_item(self, vendor_friend):
        if self.inventory == [] or vendor_friend.inventory == []:
            return False

        my_first_item = self.inventory[0]
        their_first_item = vendor_friend.inventory[0]

        self.inventory.remove(my_first_item)
        self.inventory.append(their_first_item)

        vendor_friend.inventory.remove(their_first_item)
        vendor_friend.inventory.append(my_first_item)

        return True

# # WAVE 6
# def get_by_category(self,category=""):
#     ...
#     list_of_items = []
#     if True:
# for item in self.inventory:
#     self.inventory.remove(item)
#         else:
#             return False
#     return True

# def get_best_category(self):
#     ...
    # list = get_by_category()
    # create a variable to hold the item with the best condition using max function(in the list, key=condition)
    # acces each items?



# ***helper function***
def find_best_item():
    ...

    