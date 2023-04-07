#from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory


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
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            other_vendor.add(my_first_item)
            self.remove(my_first_item)
            self.add(their_first_item)
            other_vendor.remove(their_first_item)
            return True
        

    def get_by_category(self, category):
        category_inventory = []
        for item in self.inventory:
            if item.get_category() == category:
                category_inventory.append(item)
        return category_inventory


    def get_best_by_category(self, category):
        category_selection = self.get_by_category(category)
        if not category_selection:
            return None
        else:
            highest_condition = category_selection[0]
            for item in category_selection:
                if item.condition > highest_condition.condition:
                    highest_condition = item
            return highest_condition

    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True
        else:
            return False