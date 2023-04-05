from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self, id):
        for i in range (len(self.inventory)):
            if self.inventory[i].id == id:
                return self.inventory[i]
        return None

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)

        return True
    
    def swap_first_item(self, other_vendor):

        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        first_item_self_inv = self.inventory[0]
        first_item_friend_inv = other_vendor.inventory[0]

        self.remove(first_item_self_inv)
        self.add(first_item_friend_inv)

        other_vendor.remove(first_item_friend_inv)
        other_vendor.add(first_item_self_inv)

        return True
    
    def get_by_category(self, category):
        items_same_category = []
        for item in self.inventory:
            if category == item.get_category():
                items_same_category.append(item)
        return items_same_category
