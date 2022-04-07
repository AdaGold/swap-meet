from swap_meet.item import Item
from swap_meet.vendor import Vendor 
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

'''
example_item = Item()
trenisha = Vendor()

print(vars(trenisha))
## will print out the attributes of Trenisha into a dictionary (attribute:"value")

trenisha.get_by_category() 
## if that is an instance of vendor (), will show return value of that method 


print(trenisha.get_by_category())
## will print the return statement from that method 
# (return & print statement from that method call)


print(dir(trenisha))
# will print out directory of all of the possible default 
# attributes / methods for class (__init__, __str__ etc)





# example_item = Item("Electronics", 4)
# print(vars(example_item))
# print(example_item.condition)

# item_a = Clothing(condition=2.0)
# item_b = Decor(condition=2.0)
# item_c = Clothing(condition=4.0)
# item_d = Decor(condition=5.0)
# item_e = Clothing(condition=3.0)


# trenisha = Vendor(inventory = [item_a, item_b, item_c] )


# print(vars(trenisha.inventory))
'''


item_a = Clothing(condition=2.0)
item_b = Decor(condition=2.0)
item_c = Clothing(condition=4.0)
item_d = Decor(condition=5.0)
item_e = Clothing(condition=3.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c, item_d, item_e]
    )

print(vars(tai.inventory))

# print(item_a.condition)
# print(tai.inventory)


# def get_best(self, category = ''): 
#     scores = []
#     for item in self.inventory: 
#         if item.category == category: 
#             scores.append(item.condition)

#     print(scores)

# print(tai, "Clothing")






