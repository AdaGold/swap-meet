class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            another_vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            another_vendor.inventory.remove(their_item)
            return True

    def swap_first_item(self, another_vendor):
        if self.inventory == [] or another_vendor.inventory == []:
            return False
        else:
            self.inventory.append(another_vendor.inventory[0])
            another_vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            another_vendor.inventory.remove(another_vendor.inventory[0])
            
            
            return True

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        
        if category_items == []:
            return None

        best_product = ""
        best_condition = 0

        for product in category_items:
            if product.condition > best_condition:
                best_condition = product.condition
                best_product = product
        return best_product

    def swap_best_by_category(self, other, my_priority, their_priority):
        i_have = False
        they_have = False

        if self.inventory == [] or other.inventory == []:
            return False

        for product in self.inventory:
            if product.category == their_priority:
                i_have = True

        for product in other.inventory:
            if product.category == my_priority:
                they_have = True

        if i_have is True and they_have is True:
            other_wanted = self.get_best_by_category(their_priority)
            my_wanted = other.get_best_by_category(my_priority)

            self.swap_items(other, other_wanted, my_wanted)

            return True

        else:
            return False