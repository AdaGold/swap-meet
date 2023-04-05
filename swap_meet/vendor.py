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
        # other_vendor = the friend the vendor is swapping with
        # my_item = the item this Vendor instance plans to give
        # their_item = item the friend Vendor plans to give
        
        if my_item in self.inventory or their_item in other_vendor:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        else:
            return False
