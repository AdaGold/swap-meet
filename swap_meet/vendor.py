#Wave 1
class Vendor:
    def __init__(self, inventory = None):
        if inventory is None: 
            self.inventory = []
        else:
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
        else:
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