import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

def test_swap_by_newest():
    # Arrange
    # me
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

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_f in jesse.inventory
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_d not in jesse.inventory



def test_swap_by_newest_empty():
    # Arrange
    # me
    item_a = Decor(age = 2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_b, item_a, item_c]
    )

    # them

    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )

    assert result == None