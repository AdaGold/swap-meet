from nis import cat


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

# WAVE 6
    def get_best_by_category(self, category):
        list_of_items = self.get_by_category(category)
        if not list_of_items:
            return None
        else:
            best_item =  max(list_of_items, key = lambda item: item.condition)
        
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False

        their_priority_item = other.get_best_by_category(my_priority)
        if not their_priority_item:
            return False

        my_priority_item = self.get_best_by_category(their_priority)
        if not my_priority_item:
            return False

        return self.swap_items(other, my_priority_item, their_priority_item)
