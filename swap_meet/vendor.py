from operator import itemgetter
from swap_meet.item import Item


class Vendor(Item):
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        super().__init__(category = None, condition = 0)
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
        items_list = [item for item in self.inventory if item.category == category]
                
        if items_list == []:
            return []
        return items_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        self.add(their_item)
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        return True

    def swap_first_item(self, vendor):
        if self.inventory == [] or vendor.inventory == []:
            return False
        
        self.add(vendor.inventory[0])
        vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        vendor.remove(vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        '''
        Input: category of item
        Output: item of best condition within that category
        '''
        if self.get_by_category(category) == []:
            return None
        best_item = max(self.get_by_category(category), key = lambda i : i.condition)
        return best_item 
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Input: other (for other vendor), my_priority (category vendor prefers),
        and their_priority (category other vendor prefers) 
        Output: 
            - returns True if best item in Vendor inventory matches their_priority
            and is swapped with the best item in other's inventory
            - returns False if not matches
        '''
        vendor_best_item = self.get_best_by_category(their_priority)
        other_best_item = other.get_best_by_category(my_priority)

        if vendor_best_item is None or other_best_item is None:
            return False
        self.swap_items(other, vendor_best_item, other_best_item)
        return True