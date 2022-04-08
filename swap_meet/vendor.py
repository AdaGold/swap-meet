import operator

class Vendor:

    """
        A class to represent a vendor.

    ...

    Attributes
    ----------
    inventory : list
        a list of available items for each vendor


    Methods
    -------
    add(item):
        adds a new item to the vendor's inventory
        Returns the updated inventory list
    remove(item):
        removes an item from the vendor's inventory list
        Returns the updated inventory list
    get_best_by_category(category):
        takes a string representing a category
        Returns a list of items in the inventory with the same category
    """


    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as ve:
            return False

    def get_by_category(self,category):
        result = [item for item in self.inventory if item.category == category]
        return result

    def swap_items(self,other_vendor,my_item,their_item):
        if not all ((other_vendor, my_item, their_item)):
            return False
        if  my_item == their_item:
            return True
        elif my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(their_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.remove(my_item)
            return True

    def swap_first_item(self, friend_vendor):
        if not all((friend_vendor.inventory, self.inventory)):
            return False 
        
        friend_vendor.add(self.inventory[0])
        self.add(friend_vendor.inventory[0])
        friend_vendor.remove(friend_vendor.inventory[0])
        self.remove(self.inventory[0])
        print (self.inventory)
        return self.inventory and True

    def get_best_by_category(self,category):
        matched_category = [item for item in self.inventory if category == item.category]
        if len(matched_category) == 0:
            return None
        max = matched_category[0]
        for item in matched_category:
            if item.condition > max.condition:
                max = item
        return max

    def swap_best_by_category(self,other,my_priority,their_priority):
        their_choice = self.get_best_by_category(their_priority)
        my_choice = other.get_best_by_category(my_priority)

        if my_choice and their_choice:
            self.swap_items(other, their_choice,  my_choice)
            return True
        return False



    def swap_by_newest(self,other):
        self.inventory = sorted(self.inventory, key=lambda item: item.age, reverse=False)
        other.inventory = sorted(other.inventory, key=lambda item: item.age, reverse=False)
        return self.swap_first_item(other)





    # def newest_item(self):
    #     if self.inventory == []:
    #         return None
    #     new_item = self.inventory[0]
    #     for item in self.inventory:
    #         if item.age < new_item.age:
    #             new_item = item
    #     return new_item

        # sorted_inventory = self.inventory.sort(key = lambda item: item.age)
        # return sorted_inventory
        # new_self = self.newest_item()
        # new_other = other.newest_item()
        # return new_self.inventory.swap_first_item(new_other.inventory)
        # return self.swap_items(other, new_self,new_other)
    # pass
