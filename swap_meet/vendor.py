from typing import ItemsView
from .item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self,category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, friend_inventory, my_item, their_item):

        if my_item in self.inventory or their_item in friend_inventory:
            self.inventory.add(their_item)
            friend_inventory.remove(their_item)
            self.inventory.remove(my_item)
            friend_inventory.add(my_item)
            
            return True
        return False


