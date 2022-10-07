from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
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

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend_vendor, my_item, their_item):
        if their_item not in friend_vendor.inventory or my_item not in self.inventory:
            return False
        self.remove(my_item)
        friend_vendor.add(my_item)
        friend_vendor.remove(their_item)
        self.add(their_item)
        return True
    
    def swap_first_item(self, friend_vendor):
        if self.inventory == [] or friend_vendor.inventory == []:
            return False
        my_first_item = self.inventory[0]
        their_first_item = friend_vendor.inventory[0]
        is_swapped = self.swap_items(friend_vendor, my_first_item, their_first_item)
        return is_swapped
        