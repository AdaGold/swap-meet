class Vendor:
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
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

    def get_by_category(self, category=""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items

    
    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        
        self.inventory.remove(my_item)
        vendor_friend.inventory.append(my_item)

        vendor_friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
        
    def swap_first_item(self, vendor_friend):
        if self.inventory == [] or vendor_friend.inventory == []:
            return False

        my_first_item = self.inventory[0]
        their_first_item = vendor_friend.inventory[0]

        self.inventory.remove(my_first_item)
        self.inventory.append(their_first_item)

        vendor_friend.inventory.remove(their_first_item)
        vendor_friend.inventory.append(my_first_item)

        return True

# # WAVE 6
# 
    def get_best_by_category(self, category=""):
        # if no items in self.inventory that matches: return None
        if len(self.inventory) == 0:
            return None
        
        list_of_category_items = self.get_by_category(self, category=category) #BUG HERE

        # get the item with the best condition in a certain category (the most most appearing category)
        # 1. i.e. find best condition
        # 2. make sure it's a certain category
        best_item_in_category_list = self.find_best_item(list_of_category_items)
        
        # loop through self.inventory list to find the item with best condition AND matching category
        for item in self.inventory:
            if item == best_item_in_category_list:
                return item
            
        return None


    def swap_best_by_category(self, other, my_priority, their_priority):#swaps the best item of certain categories with other_vendor
        """
        other, which represents another Vendor instance to trade with
        my_priority, which represents a category that the Vendor wants to receive
        their_priority, which represents a category that other wants to receive
        """
        
        # best item in self.inventory that matches their_priority is SWAPPED with the best item in other_vendor inventory that matches my_priority
        # 1.my_priority
        # 2.their_priority
        # 3.find the best item in self.inventory that matches their_priority **can call get_best_by_category here**
        #     3b. if no match:returns False
        # 4.find the best item in other_vendor.inventory that matches their_priority **can call get_best_by_category here**
        #     4.b.  if no match:returns False
        # 5. swap the best items
            # : can we call  swap_items(): here so that swap_best_by_category and swap_first_item can use it???

        # return True
        ...

    # ***helper functions***
    def find_best_item(self, category_or_invetory_list): #???
        if len(category_or_invetory_list) == 0:
            return None

        best_item  = category_or_invetory_list[0]
        for item in category_or_invetory_list:
            if item.condition > best_item.condition:
                best_item.condition = item.condition

        return best_item
    