import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_item_overrides_to_string():
    item = Item()

    stringified_item = str(item)

    assert stringified_item == "Hello World!"

def test_swap_item_returns_true():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics")
    item_e = Item(category="decor")
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_item(jolie, item_b, item_d)

    assert len(fatimah.inventory) is 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) is 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_b in jolie.inventory
    assert result is True