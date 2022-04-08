class Vendor:
    def __init__ (self, inventory = None):
        if not inventory:
            inventory = []
            
        self.inventory = inventory

    def add(self, item): 
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try: 
            self.inventory.remove(item)
            return item

        except:
            return False

    def get_by_category(self, category):
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)

        return items

    def swap_items(self, vendor, my_item, their_item):
        '''
        add my item to vendor's inventory
        remove my item from my inventory
        add their item to my inventory
        remove their item from their inventory
        ---
        I initially used the above add() and remove() methods, but wanted something a bit more logically streamlined. 
        Accomplishing the swap of items using a tuple allows for a direct in-place substitution without iterating over the lists.
        However, I'm not sure if list index() and list remove() have significantly different time complexity - both seem to be O(n).
        In addition, using this method throws an error if either item is not in the list, 
        which allows me to return False using try-except, instead of manually checking and returning False.
        '''
        try:
            my_item_index = self.inventory.index(my_item)
            their_item_index = vendor.inventory.index(their_item)

            swap_items = self.inventory[my_item_index], vendor.inventory[their_item_index]
            vendor.inventory[their_item_index], self.inventory[my_item_index] = swap_items
            return True

        except:
            return False

    def swap_first_item(self, vendor):
        '''
        swap the first item between my inventory and vendor's inventory.
        return false if either inventory is empty.
        '''
        try:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, their_item)
            return True

        except:
            return False
    
    def get_best_by_category(self, category):
        '''
        return item with best condition in a given category (returns one item only)
        if no items match the given category, return None
        '''
        condition = -1
        best_item = None
        items = self.get_by_category(category)

        for item in items:
            if item.condition > condition:
                best_item = item
                condition = item.condition

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        swap items with best condition between my preferred category and another vendor's preferred category
        if no items are in the category in either vendor's inventory, return False
        '''
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if None in (my_item, their_item):
            return False

        self.swap_items(other, my_item, their_item)
        return True