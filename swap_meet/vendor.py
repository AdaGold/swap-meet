class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
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
        
    def get_by_category(self, category):
        return_list = []
        for item in self.inventory:
            if item.category == category:
                return_list.append(item)
        return return_list
    
    def swap_items(self, friend_vendor, my_item, friend_item):
        try:
            if not self.remove(my_item):
                return False

            if not friend_vendor.remove(friend_item):
                # If swap cannot be completed, put the removed item back in the self inventory
                self.add(my_item)
                return False

            self.add(friend_item)                
            friend_vendor.add(my_item)

            return True
        except Exception as e:
            print(str(e))
            return False

    def swap_first_item(self, friend_vendor):
        try:
            return self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])
        except Exception as e:
            print(str(e))
            return False

    def get_best_by_category(self, best_category):
        #Create the vairables that are involved with category and condition.
        winning_condition = 0
        winning_item = None
        #Create a loop to look  to get best item from get_by_category
        for item in self.get_by_category(best_category):
            if item.condition > winning_condition:
                winning_item = item
                winning_condition = item.condition
        
        return winning_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        #do some checking
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        my_best_item = self.get_best_by_category(their_priority)
        if my_best_item == None:
            return False
        their_best_item = other.get_best_by_category(my_priority)
        if their_best_item == None:
            return False
        
        self.swap_items(other, my_best_item, their_best_item)
        return self

