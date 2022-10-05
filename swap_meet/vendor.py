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

        if my_item in self.inventory and their_item in friend_inventory.inventory:
            self.inventory.append(their_item)
            friend_inventory.inventory.remove(their_item)
            friend_inventory.inventory.append(my_item)
            self.inventory.remove(my_item)
            
            return True
        return False
    
    def swap_first_item(self,friend):
        
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        return False





