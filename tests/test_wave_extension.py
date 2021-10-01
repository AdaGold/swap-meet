import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_when_all_items_have_ages():
    item_a = Decor(condition=2.0, age=10)
    item_b = Electronics(condition=4.0, age=5)
    item_c = Decor(condition=4.0, age=45)
    arie = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=3)
    item_e = Decor(condition=4.0, age=45)
    item_f = Clothing(condition=4.0, age=1)
    jessica = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = arie.swap_by_newest(
        other=jessica
    )

    assert not result
    assert len(arie.inventory) == 3
    assert len(jessica.inventory) == 3
    assert item_a in arie.inventory
    assert item_b not in arie.inventory
    assert item_c in arie.inventory
    assert item_f in arie.inventory
    assert item_d in jessica.inventory
    assert item_b in jessica.inventory
    assert item_e in jessica.inventory
    assert item_f not in jessica.inventory

def test_swap_by_newest_when_at_least_one_age_is_default_None():
    item_a = Decor(condition=2.0, age=10)
    item_b = Electronics(condition=4.0, age=5)
    item_c = Decor(condition=4.0, age=45)
    arie = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=3)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jessica = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = arie.swap_by_newest(
        other=jessica
    )

    assert not result
    assert len(arie.inventory) == 3
    assert len(jessica.inventory) == 3
    assert item_a in arie.inventory
    assert item_b not in arie.inventory
    assert item_c in arie.inventory
    assert item_d in arie.inventory
    assert item_d not in jessica.inventory
    assert item_b in jessica.inventory
    assert item_e in jessica.inventory
    assert item_f in jessica.inventory

def test_swap_by_newest_when_no_items_have_ages():
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    arie = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jessica = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    result = arie.swap_by_newest(
        other=jessica
    )

    assert result == False
    assert len(arie.inventory) == 3
    assert len(jessica.inventory) == 3
    assert item_a in arie.inventory
    assert item_b in arie.inventory
    assert item_c in arie.inventory
    assert item_d in jessica.inventory
    assert item_e in jessica.inventory
    assert item_f in jessica.inventory