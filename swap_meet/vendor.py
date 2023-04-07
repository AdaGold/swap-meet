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
    #     # other_vendor = the friend the vendor is swapping with
    #     # my_item = the item this Vendor instance plans to give
    #     # their_item = item the friend Vendor plans to give
        
    #     if my_item not in self.inventory or their_item not in other_vendor.inventory:
    #         return False
    #     else:
    #         self.inventory.remove(my_item)
    #         self.inventory.append(their_item)
    #         other_vendor.inventory.remove(their_item)
    #         other_vendor.inventory.append(my_item)
    #         return True

        # if my_item in self.inventory and their_item in other_vendor.inventory:
        #     self.inventory.remove(my_item)
        #     self.inventory.append(their_item)
        #     other_vendor.inventory.remove(their_item)
        #     other_vendor.inventory.append(my_item)
        #     return True
        # return False
    
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
