from swap_meet.item import Item

class Vendor:
    ''' '''
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
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

    def get_by_category(self, category):
        '''Search Vendor's inventory for item category, return a list of
        Item matches.'''
        item_list = []
        
        # Loop through each item in instance's inventory list
        for item in self.inventory:
            # self.inventory => [<__main__.Item object at 0x10c302970>]
            # If category name matches an existing item category
            if category == item.category:
                item_list.append(item)

        return item_list