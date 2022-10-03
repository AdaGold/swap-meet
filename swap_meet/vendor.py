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

