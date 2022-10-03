class Vendor:
    """The Vendor class has optional arguement inventory,
    methods .add(item), .remove(item)"""
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

        