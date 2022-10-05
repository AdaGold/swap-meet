import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

''' 
**** TEST ADDED FOR [OPTIONAL] SWAP BY NEWEST FUNCTION *** 

'''

#@pytest.mark.skip

def test_newest_item_1():
    # Arrange
    item_a = Clothing(age=0.0)
    item_b = Electronics(age = 1.0)
    item_c = Decor(age = 4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    # Act
    result = tai.newest_item()

    #Assert
    assert result == item_a

def test_newest_item_2():
    #Arrange
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )
    # Act
    result = jesse.newest_item()

    #Assert
    assert result == item_d

import pytest
from swap_meet.vendor import Vendor

def test_swap_by_newest():
    # Arrange
    item_a = Clothing(age=0.0)
    item_b = Electronics(age=1.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(another_vendor=jesse)

    #Assert
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert all(item in [item_d, item_b, item_c] for item in tai.inventory)
    assert all(item in [item_a, item_e, item_f] for item in jesse.inventory)