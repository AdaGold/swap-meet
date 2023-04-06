import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_returns_True():
    # Arrange
    item1 = Item(age=5)
    item2 = Item(age=3)
    item3 = Item(age=2)
    vendor1 = Vendor([item1, item2])
    vendor2 = Vendor([item3])

    # Act
    result = vendor1.swap_by_newest(vendor2)

    # Assert
    assert result == True
    assert item3 in vendor1.inventory
    assert item2 in vendor2.inventory

def test_swap_by_newest_when_one_inv_list_is_empty_returns_False():
    # Arrange
    item1 = Item(age=5)
    vendor1 = Vendor([item1])
    vendor2 = Vendor([])

    # Act
    result = vendor1.swap_by_newest(vendor2)

    # Assert
    assert result == False
    assert item1 in vendor1.inventory
    assert len(vendor2.inventory) == 0

def test_swap_by_newest_success_when_same_age():
    # Arrange
    item1 = Item(age=5)
    item2 = Item(age=3)
    item3 = Item(age=3)
    vendor1 = Vendor([item1, item2])
    vendor2 = Vendor([item3])

    # Act
    result = vendor1.swap_by_newest(vendor2)

    # Assert
    assert result == True
    assert item3 in vendor1.inventory
    assert item2 in vendor2.inventory

def test_swap_by_newest_both_empty_inventories():
    # Arrange
    vendor1 = Vendor([])
    vendor2 = Vendor([])

    # Act
    result = vendor1.swap_by_newest(vendor2)

    # Assert
    assert result == False
    assert len(vendor1.inventory) == 0
    assert len(vendor2.inventory) == 0