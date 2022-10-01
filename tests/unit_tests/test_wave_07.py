import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_condition_description():
    item_a = Item(category="clothing", condition = 0.5)
    item_b = Item(category="clothing", condition = 1.5)
    item_c = Item(category="clothing", condition = 2.4)
    item_d = Item(category="clothing", condition = 3.5)
    item_e = Item(category="clothing", condition = 4.5)
    item_f = Item(category="clothing", condition = 7)
    # result = item_a.condition_description()
    assert item_a.condition_description() == "Just trash it!"
    assert item_b.condition_description() == "Enjoy the last moments!"
    assert item_c.condition_description() == "As good as 30 year old wine!"
    assert item_d.condition_description() == "Better than the new one"
    assert item_e.condition_description() == "No need to ask!"
    assert item_f.condition_description() == False
