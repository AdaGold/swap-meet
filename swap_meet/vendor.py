class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
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
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            another_vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            another_vendor.inventory.remove(their_item)
            return True

    def swap_first_item(self, another_vendor):
        if self.inventory == [] or another_vendor.inventory == []:
            return False
        else:
            self.inventory.append(another_vendor.inventory[0])
            another_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            another_vendor.inventory.remove(another_vendor.inventory[0])
            
            
            return True