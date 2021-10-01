# WAVE 1
class Vendor:
    def __init__(self, category = "", inventory = []):
        self.category = category
        self.inventory = inventory
        

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, remove_item):
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False
# WAVE 2

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category: 
                items.append(item)
        
        return items

# WAVE 3
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        else:
            
            friend_vendor.inventory.append(my_item)
            self.remove(my_item)

            self.inventory.append(their_item)
            friend_vendor.remove(their_item)
            return True

# WAVE 4
    def swap_first_item(self, friend_vendor):
        if not self.inventory or not friend_vendor.inventory:
            return False
        else:
            self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])
            return True

    # Wave 6
    def get_best_by_category(self, category):
        highest_condition = 0
        highest_item = None

        for item in self.inventory:
            if item.category == category and item.condition > highest_condition:
                highest_condition = item.condition
                highest_item = item

        return highest_item 

    def swap_best_by_category(self, other, my_priority, their_priority):

        if not self.inventory or not other.inventory:
            return False

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item: 
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True
        
        








