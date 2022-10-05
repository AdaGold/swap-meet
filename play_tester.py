
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#def test_swap_best_by_category():
# Arrange
# me
item_a = Decor(condition=2.0)
item_b = Electronics(condition=4.0)
item_c = Decor(condition=4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)

# them
item_d = Clothing(condition=2.0)
item_e = Decor(condition=4.0)
item_f = Clothing(condition=4.0)
jesse = Vendor(
    inventory=[item_d, item_e, item_f]
)

# Act
result = tai.swap_best_by_category(
other=jesse,
    my_priority="Clothing",
    their_priority="Decor"
)
# print(tai.inventory)
# print(jesse.inventory)
#print(result)