from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# vendor = Vendor(inventory=["a", "b", "c"])
# print(vendor.inventory)
# item_a = Item(category = "clothing", condition = 1, age = 2)
# item_b = Item(category = "Decor", condition = 3, age = 1)
# item_c = Item(category = "Electerical", condition = 2, age = 3)
# item_d = Item(category = "clothing", condition = 4, age = 5)
# item_e = Item(category = "Decor", condition = 2, age = 4)
# item_f = Item(category = "Electronics", condition = 3, age = 3)
# raha = Vendor([item_a,item_b,item_c])
# # print (raha.inventory)
# mitra = Vendor([item_d,item_e,item_f])
# print(vendor.add("d"))
# print(vendor.remove("d"))
# print(vendor.inventory)
item_a = Decor(age = 2.0)
item_b = Electronics(age=4.0)
item_c = Decor(age=4.0)
tai = Vendor(
        inventory=[item_b, item_a, item_c]
    )

    # them
item_d = Clothing(age=2.0)
item_e = Decor(age=4.0)
item_f = Clothing(age=4.0)
jesse = Vendor(
        inventory=[item_e, item_d,item_f]
    )
print(tai.inventory)
# print(jesse.inventory)

print(tai.swap_first_item(jesse))
print(tai.swap_by_newest(jesse))
