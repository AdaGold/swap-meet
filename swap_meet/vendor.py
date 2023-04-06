#Wave 1
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False
        
#Wave2
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item

        return None

#Wave3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            return True
        
        return False
        
#Wave4
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            self.swap_items(
                other_vendor, 
                self.inventory[0], 
                other_vendor.inventory[0]
            )
            return True

        return False
    
#Wave6
    def get_by_category(self, category):
        inv = self.inventory.copy()
        return list(filter(lambda item: item.get_category() == category, inv))
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        return max(items, default=None, key=lambda item: item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if my_best and their_best:
            self.swap_items(other_vendor, my_best, their_best)
            return True

        return False