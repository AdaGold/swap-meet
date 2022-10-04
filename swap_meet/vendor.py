from operator import itemgetter


class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_list = []

        for item in self.inventory:
            if item.category == category: 
                items_list.append(item)
        
        if items_list == []:
            return "Sorry, there are no items within that category."

        return items_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        self.add(their_item)
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        return True