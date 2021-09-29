from swap_meet.item import Item

class Vendor:
    """
    A class to represent a trading vendor at the swap meet.
    
    ...

    Attributes
    ----------
    inventory : list
        list of Item ojbects in vendor's possession

    Methods
    -------
    add(inventory_item):
        Adds an item to instance inventory list. Returns
        item.

    remove(inventory_item):
        Removes item from list, returning item. Returns
        False if not found.

    get_by_category(category):
        Search Vendor's inventory for item category, return a list of
        Item object matches.
    
    get_best_by_category(category):
        Search Vendor's inventory for highest rated item in a particular
        category, return item object.

    swap_items(other_vendor, item_a, item_b):
        Swaps two items from current instance of Vendor with another vendor.

    swap_first_item(other_vendor):
        Swaps first listed items of current instance of Vendor and another 
        vendor.
    """

    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, inventory_item):
        """ Add an item to instance inventory list. Returns
        item."""
        self.inventory.append(inventory_item)
        return inventory_item

    def remove(self, inventory_item):
        """ Removes item from list, returning item. Returns
        False if not found."""
        try:
            self.inventory.remove(inventory_item)
            return inventory_item
        except ValueError:
            return False

    def get_by_category(self, category):
        """Search Vendor's inventory for item category, return a list of
        Item matches."""
        item_of_category_list = []
        
        for item in self.inventory:
            # self.inventory => [<__main__.Item object at 0x10c302970>]
            # If provided category name matches an item category in inventory
            if category == item.category:
                item_of_category_list.append(item)

        return item_of_category_list

    def get_best_by_category(self, category):
        """Search Vendor's inventory for highest rated item in a particular
        category, return item. """

        # Store list of vendor's items matching specified category
        items = self.get_by_category(category)

        # Return False for no matches
        if not items:
            return None
        else:
            # Find max value based on item.condition values
            item_with_max_val = max(items, key=lambda item: item.condition)
            return item_with_max_val

    def swap_items(self, other_vendor, self_item, other_item):
        """Swaps two items from current instance of Vendor with another vendor, 
        as defined in 'vendor_name'."""

        # Check if items in respective Vendor's inventories
        if self_item in self.inventory and other_item in other_vendor.inventory:
            # Add item_a to other_vendor inventory & remove from current
            self.add(other_item)
            self.remove(self_item)
            # Add item_b to current and remove from other_vendor inventory
            other_vendor.add(self_item)
            other_vendor.remove(other_item)

            return True
        else:
           return False

    def swap_first_item(self, other_vendor):
        """Swaps first items of current vendor and other vendor. """
        # Check that both vendors have items in inventory
        if self.inventory and other_vendor.inventory:
            # Append first item of each vendor's inventory to the 
            # inventory of the other
            self.add(other_vendor.inventory[0])
            other_vendor.add(self.inventory[0])

            # Remove the first item from each inventory list
            self.remove(self.inventory[0])
            other_vendor.remove(other_vendor.inventory[0])

            return True
        else:
            return False

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps item in best condition in current instance and other vendor's 
        instance, filtered by explicitly preferred category from each user."""
        
        my_priority_in_other = other.get_best_by_category(my_priority)
        others_priority_in_mine = self.get_best_by_category(their_priority)

        if my_priority_in_other and others_priority_in_mine:
            return self.swap_items(other, others_priority_in_mine, 
                                    my_priority_in_other)
        else:
            return False