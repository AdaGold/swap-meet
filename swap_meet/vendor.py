class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as ve:
            return False
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        my_first = self.inventory[0]
        other_first = other_vendor.inventory[0]
        self.remove(my_first)
        other_vendor.remove(other_first)
        self.add(other_first)
        other_vendor.add(my_first)
        return True

    def get_best_by_category(self, category):
        inv_by_category = [item for item in self.inventory if item.category == category]

        if len(inv_by_category) == 0:
            return None

        print(inv_by_category)

        max = inv_by_category[0]
        for item in inv_by_category:
            if item.condition > max.condition:
                max = item
        
        return max

    def swap_best_by_category(self, other: 'Vendor', my_priority: str, their_priority: str):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if my_best is None or their_best is None:
            return False

        self.remove(my_best)
        other.remove(their_best)
        self.add(their_best)
        other.add(my_best)
        return True
