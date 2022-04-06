class Vendor:
    def __init__ (self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item): 
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try: 
            self.inventory.remove(item)
            return item
        except:
            return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, vendor, my_item, their_item):
        '''
        add my item to vendor's inventory
        remove my item from my inventory
        add their item to my inventory
        remove their item from their inventory
        '''
        try:
            vendor.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            return True
        except:
            return False
