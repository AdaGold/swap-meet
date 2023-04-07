#from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory


    def add(self, item):
        self.inventory.append(item)
        return item
    

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item
    

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    

    def swap_items(self, other_vendor, my_item, their_item):    
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        return False    
    

    def swap_first_item(self, other_vendor):
        try:
            return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        except IndexError:
            return False
        

    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]


    def get_best_by_category(self, category):
        category_selection = self.get_by_category(category)
        try:
            return max(category_selection, key=lambda item: item.condition)
        except ValueError:
            return None

    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, my_best_item, their_best_item)
