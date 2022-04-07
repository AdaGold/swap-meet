from swap_meet.item import Item 


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []


    def add(self, item): 
        self.inventory.append(item)
        return item 
    def remove(self, item):
        if item not in self.inventory:
            return False 
        self.inventory.remove(item)
        return item 

    def get_by_category(self, category = ''):
        category_list = []
  
        for item in self.inventory: 
            if item.category == category: 
                category_list.append(item)
        return category_list 
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory: 
            return False 
       
        
        vendor.inventory.append(my_item)
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        vendor.inventory.remove(their_item)
        return True 

    def swap_first_item(self, vendor):
        if self.inventory == []  or vendor.inventory == []: 
            return False

        first_self = self.inventory[0]
        first_vendor = vendor.inventory[0]

        self.inventory.pop(0)
        vendor.inventory.pop(0)
        self.inventory.append(first_vendor)
        vendor.inventory.append(first_self)
        return True 


    def get_best_by_category(self, category = ''):
        if self.inventory == []: 
            return None 

        category_score = []
        item_list = self.get_by_category(category)
        if len(item_list) == 0:
            return None 
        for item in item_list: 
            category_score.append(item.condition)

        best_score = max(category_score)

        for item in item_list:
            if item.condition == best_score: 
                return item 


    


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        result = self.swap_items(other, my_item, their_item)
        
        return result 

