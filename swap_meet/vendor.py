from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory


    def add(self, added_item):
        
        self.inventory.append(added_item)

        return added_item


    def remove(self, removed_item):
        
        if removed_item in self.inventory:
            self.inventory.remove(removed_item)
        else:
            return False
        
        return removed_item