from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        for i in range (len(self.inventory)):
            if self.inventory[i].id == id:
                return self.inventory[i]
        return None

    def swap_items(self, other_vendor, my_item, their_item):

        if self.get_by_id(my_item.id) == None or other_vendor.get_by_id(their_item.id) == None:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):

        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        first_item_self_inv = self.inventory[0]
        first_item_friend_inv = other_vendor.inventory[0]

        return self.swap_items(other_vendor, first_item_self_inv, first_item_friend_inv)
    
    def get_by_category(self, category):
        items_same_category = []
        for item in self.inventory:
            if category == item.get_category():
                items_same_category.append(item)
        return items_same_category
    
    def get_best_by_category(self, category):
        max_condition = 0
        max_item = None
        for item in self.inventory:
            if max_condition < item.condition and category == item.get_category():
                max_condition = item.condition 
                max_item = item
        return max_item
    
    def swap_best_by_category(self,other_vendor, my_priority, their_priority):

        other_vendor_best_item = self.get_best_by_category(their_priority)
        self_best_item = other_vendor.get_best_by_category(my_priority)

        if other_vendor_best_item == None or self_best_item == None:
            return False
        return self.swap_items(other_vendor, other_vendor_best_item, self_best_item)
