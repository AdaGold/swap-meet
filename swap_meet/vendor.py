class Vendor:
    ''' '''
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, inventory_item):
        ''' Add an item to instance inventory list. Returns
        item.'''
        self.inventory.append(inventory_item)
        return inventory_item

    def remove(self, inventory_item):
        ''' Removes item from list, returning item. Returns
        False if not found.'''
        try:
            self.inventory.remove(inventory_item)
            return inventory_item
        except ValueError:
            return False