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
        list_of_items = self.get_by_category(category)
        if not list_of_items:
            return None
        else:
            best_item =  max(list_of_items, key = lambda item: item.condition)
        
        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):#swaps the best item of certain categories with other_vendor
        
        # if their_priority not in self.inventory or my_priority not in other.inventory:
        #     return False
        
        best_item = max(self.inventory, key = lambda item: item.condition)
        print(f"best item: {best_item}")
        # self.inventory.remove(my_item)
        # vendor_friend.inventory.append(my_item)

        # vendor_friend.inventory.remove(their_item)
        # self.inventory.append(their_item)
        # return True
        
#         # best item in self.inventory that matches their_priority is SWAPPED with the best item in other_vendor inventory that matches my_priority
#         # 1.my_priority
#         # 2.their_priority
#         # 3.find the best item in self.inventory that matches their_priority **can call get_best_by_category here**
#         #     3b. if no match:returns False
#         # 4.find the best item in other_vendor.inventory that matches their_priority **can call get_best_by_category here**
#         #     4.b.  if no match:returns False
#         # 5. swap the best items
#             # : can we call  swap_items(): here so that swap_best_by_category and swap_first_item can use it???
        
#         ...

    # # helper_function
    # def get_best_item(self, list_of_items):
    #     if not list_of_items:
    #         return None
        
    #     best_item = list_of_items[0]

    #     for item in list_of_items:
    #         if item.condition > best_item.condition:
    #             best_item = item

    #         return best_item
