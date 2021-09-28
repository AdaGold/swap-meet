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
        Item matches.

    swap_items(other_vendor, item_a, item_b):
        Swaps two items from current instance of Vendor with another vendor, 
        as defined in 'vendor_name'.
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
        
        # Loop through each item in instance's inventory list
        for item in self.inventory:
            # self.inventory => [<__main__.Item object at 0x10c302970>]
            # If category name matches an existing item category
            if category == item.category:
                item_of_category_list.append(item)

        return item_of_category_list

    def swap_items(self, other_vendor, item_a, item_b):
        """Swaps two items from current instance of Vendor with another vendor, 
        as defined in 'vendor_name'."""

        # Check if items in respective Vendor's inventories
        if item_a in self.inventory and item_b in other_vendor.inventory:
            # Add item_a to other_vendor inventory & remove from current
            self.add(item_b)
            self.remove(item_a)
            # Add item_b to current and remove from other_vendor inventory
            other_vendor.add(item_a)
            other_vendor.remove(item_b)

            return True
        else:
           return False