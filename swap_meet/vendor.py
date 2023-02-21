class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
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
        filtered_list = []
        for item in self.inventory:
            if item.category == category:
                filtered_list.append(item)
        return filtered_list

    def get_by_id(self, id):
        result = None
        for item in self.inventory:
            if item.id == id:
                result = item

        return result

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        #adding and removing to self
        self.remove(my_item)
        self.add(their_item)

        #adding and removing to other_vendor
        other_vendor.remove(their_item)
        other_vendor.add(my_item)

        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        # get first item
        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        #swap
        self.inventory = self.inventory[1:]
        other_vendor.inventory = other_vendor.inventory[1:]

        self.inventory.append(other_first_item)
        other_vendor.inventory.append(my_first_item)

        return True

    def get_best_by_category(self, category):
        highest = 0
        best_item = None

        for item in self.inventory:
            if item.category == category and item.condition > highest:
                best_item = item
                highest = item.condition

        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if their_best_item == None or my_best_item == None:
            return False

        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True
