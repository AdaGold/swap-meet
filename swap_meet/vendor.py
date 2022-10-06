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

# WAVE 6
    def get_best_by_category(self, category):
        print(self.inventory)
        # search self.inventory for list of items with specific category
        list_of_items = self.get_by_category(category)
        print(list_of_items)
        
        # search list of items for highest condition
        best_condition = list_of_items[0]
        for item in list_of_items:
            ...

        # if item found, return item
        # if item not found,  return None


#     def swap_best_by_category(self, other, my_priority, their_priority):#swaps the best item of certain categories with other_vendor
#         """
#         other, which represents another Vendor instance to trade with
#         my_priority, which represents a category that the Vendor wants to receive
#         their_priority, which represents a category that other wants to receive
#         """
        
#         # best item in self.inventory that matches their_priority is SWAPPED with the best item in other_vendor inventory that matches my_priority
#         # 1.my_priority
#         # 2.their_priority
#         # 3.find the best item in self.inventory that matches their_priority **can call get_best_by_category here**
#         #     3b. if no match:returns False
#         # 4.find the best item in other_vendor.inventory that matches their_priority **can call get_best_by_category here**
#         #     4.b.  if no match:returns False
#         # 5. swap the best items
#             # : can we call  swap_items(): here so that swap_best_by_category and swap_first_item can use it???

#         # return True
#         ...