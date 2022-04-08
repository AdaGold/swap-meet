from swap_meet.item import Item 

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    @staticmethod
    def check_if_in_inventory(inventory, item):  
        if item not in inventory: 
           return False
        return True 

    # pass in vendors as tuple, and items as tuple to iterate through them 
    # just have one static method 
    
    @staticmethod 
    def combo_static_combo(vendor_1, vendor_2, item_1, item_2): 
        if Vendor.check_if_in_inventory(vendor_1.inventory, item_1) and Vendor.check_if_in_inventory(vendor_2.inventory, item_2):
            return True 
        return False 


    def add(self, item): 
        self.inventory.append(item)
        return item 


    def remove(self, item):
        if Vendor.check_if_in_inventory(self.inventory, item): 
            self.inventory.remove(item)
            return item 
        return False 


    def get_by_category(self, category = ''):
        category_list = []
  
        for item in self.inventory: 
            if item.category == category: 
                category_list.append(item)
        return category_list 
    
    def swap_items(self, vendor, my_item, their_item):
        if Vendor.combo_static_combo(self, vendor, my_item, their_item):    
        
            vendor.inventory.append(my_item)
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            return True 
        return False 

    def swap_first_item(self, vendor):
        if self.inventory == []  or vendor.inventory == []: 
            return False

        first_self = self.inventory[0]
        first_vendor = vendor.inventory[0]

        item_swap = self.swap_items(vendor, first_self, first_vendor)
        return True 


    def get_best_by_category(self, category = ''):
        if self.inventory == []: 
            return None 

       
        item_list = self.get_by_category(category)
        if len(item_list) == 0:
            return None 


        # item_dict = {}
        # for item in item_list: 
        #     item_dict[item] = item.condition 

        item_dict = dict.fromkeys{item_list, item.condition }
        item_dict = {item.condition for (item, item.condition in item_list}

        best_score = max(item_dict, key=item_dict.get)
        return(best_score)
        
      
    


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        result = self.swap_items(other, my_item, their_item)
        
        return result 

