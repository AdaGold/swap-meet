class Vendor:
    """The Vendor class has optional arguement inventory,
    methods: .add(item), .remove(item), .get_by_category(category),
    swap_items(swapping_vendor, my_item, their_item)"""
    def __init__(self, inventory = None):
        #if an inventory list is given, assign it to the attribute
        if inventory:
            self.inventory = inventory
        #if no inventory list is given, initialize an empty list for inventory.
        else:
            self.inventory = []

    def add(self, item):
        """appends the item to the inventory list and returns the item"""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """removes an item from the inventory list"""
        #if item is in inventory, remove it
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        """given a category, return a list of all items in inventory
        that have that as their attribute category."""
        items_in_category = []
        #iterate through inventory to append items with the given category
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, swapping_vendor, my_item, their_item):
        """given another vendor, my_item to swap, their_item to receive, make that swap."""
        #if each item is in the right place, make the swap:
        if my_item in self.inventory and their_item in swapping_vendor.inventory:
            #make the swap
            self.remove(my_item)
            self.add(their_item)
            swapping_vendor.add(my_item)
            swapping_vendor.remove(their_item)
            
            return True
        else:
            return False

    def swap_first_item(self, swapping_vendor):
        """given another vendor, swap the first item
        in each of your inventories."""
        if self.inventory and swapping_vendor.inventory:
            #call swap_items, inputing the first item on each of your inventories:
            result = self.swap_items(swapping_vendor, self.inventory[0], swapping_vendor.inventory[0])
            return result
        else:
            return False

    def get_best_by_category(self, category):
        """this will return the best item a vendor has in a given category"""
        #In the case of a tie, it will return the LAST instance of this item.
        best_item = None
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
                #I think there's a faster way to do this, in one loop.
                #for now, I'm just going to get it working.
        if items_in_category:
            best_item = items_in_category[0]
            for cat_item in items_in_category:
                if cat_item.condition >= best_item.condition:
                    best_item = cat_item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """This will swap two items: self will give their item
        of highest quality from the category their_priority.
        In return, the swapping_vendor will give their best item from 
        the category my_priority."""
        #figure out what items will be swapped.
        my_item_to_swap = self.get_best_by_category(their_priority)
        their_item_to_swap = other.get_best_by_category(my_priority)
        result = self.swap_items(other, my_item_to_swap, their_item_to_swap)
        return result



