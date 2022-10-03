class Vendor:
    #testing a small change for git hub
    def __init__(self, inventory = None):
        #if an inventory list is given, assign it to the attribute
        if inventory:
            self.inventory = inventory
        #if no inventory list is given, initialize an empty list for inventory.
        else:
            self.inventory = []

    def add(self, item):
        #append the item to the inventory list.
        self.inventory.append(item)
        #return the new item
        return item
        