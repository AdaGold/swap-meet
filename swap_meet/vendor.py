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
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            friend.remove(their_item)
            friend.add(my_item)
            self.remove(my_item)
            
            return True
        return False
    
    def swap_first_item(self, friend):
        
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        return False

    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None
        return max(self.get_by_category(category), key=lambda item: item.condition)

    
    def swap_best_by_category(self,other,my_priority,their_priority):
        self_best_item = self.get_best_by_category(their_priority)
        other_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other,self_best_item,other_best_item)
