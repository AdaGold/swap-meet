from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item

        return False

    def get_by_category(self, category):
        list_of_items = []
        for item in self.inventory:       
            if item.category == category:
                list_of_items.append(item)

        return list_of_items

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
    
        other_vendor.remove(their_item)
        self.add(their_item)
        self.remove(my_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory: 
            return False
        
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_item, their_item)
        return True

    def get_best_by_category(self, category):
        items_with_category = self.get_by_category(category)
        if not items_with_category:
            return None

        max_item_condition = max(items_with_category, key=lambda item: item.condition)
        return max_item_condition


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_by_category = self.get_best_by_category(their_priority)
        their_best_by_category = other.get_best_by_category(my_priority)

        if not my_best_by_category or not their_best_by_category:
            return False

        result = self.swap_items(other, my_best_by_category, their_best_by_category)
        return result

    def get_newest(self, any_list=None):
        # any_list = self.inventory if self.inventory is not None else []
        # other version #
        if any_list is None:
            any_list = self.inventory

        if not self.inventory or not any_list:
            return None

        return min(any_list, key=lambda item: item.age)
        
    
    def get_newest_by_category(self, category):
        newest_items_with_category = self.get_by_category(category)
        if not newest_items_with_category:
            return None

        newest_item = self.get_newest(newest_items_with_category)
        return newest_item


    def swap_newest(self, other):
        my_newest_item = self.get_newest()
        other_newest_item = other.get_newest()
        if not my_newest_item or not other_newest_item:
            return False

        self.swap_items(other, my_newest_item, other_newest_item)
        return True



    def swap_newest_by_category(self, other, my_priority=None, their_priority=None):
        my_newest_by_category = self.get_newest_by_category(their_priority)
        their_newest_by_category = other.get_newest_by_category(my_priority)
        if not my_newest_by_category or not their_newest_by_category:
            return False

        self.swap_items(other, my_newest_by_category, their_newest_by_category)
        return True


    

