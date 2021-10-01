from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing

# item_a = Item(category = "furniture")
# print(item_a)

item_a = Clothing(condition = 3.0)
item_b = Clothing(condition = 4.5)

ada = Vendor(inventory = [item_a, item_b])

print(ada.get_best_by_category("Clothing"))
