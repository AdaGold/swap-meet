import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
def test_get_by_category_False():
    item_a = Item(category="clothing")
    item_b = Item(category="electronics")
    item_c = Item(category="clothing")
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("Decor")


    assert items == []
