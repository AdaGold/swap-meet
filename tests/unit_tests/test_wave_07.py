import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

@pytest.mark.skip
#this one is done
def test_get_newest():
    item_a = Clothing(age=0.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item.age == 0

@pytest.mark.skip
#this one is done
def test_get_newest_empty_inventory():
    tai = Vendor(
        inventory=[]
    )

    newest_item = tai.get_newest()

    assert newest_item is None

@pytest.mark.skip
#this one is done more or less
def test_get_newest_by_category():
    item_a = Clothing(age=0.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(0.0)

@pytest.mark.skip
#this one is done more or less
def test_get_newest_by_category_no_matches_is_none():
    item_a = Decor(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_newest_by_category("Electronics")

    assert best_item is None

# @pytest.mark.skip
# def test_best_by_category_with_duplicates():
#     # Arrange
#     item_a = Clothing(condition=2.0)
#     item_b = Clothing(condition=4.0)
#     item_c = Clothing(condition=4.0)
#     tai = Vendor(
#         inventory=[item_a, item_b, item_c]
#     )

#     # Act
#     best_item = tai.get_best_by_category("Clothing")

#     # Assert
#     assert best_item.category == "Clothing"
#     assert best_item.condition == pytest.approx(4.0)

@pytest.mark.skip
#this one is done 
def test_swap_newest():
    # Arrange
    # me
    item_a = Decor(age=1.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=0.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_newest(
        other=jesse,        
    )

    
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_d in tai.inventory 
    assert item_a in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_a not in tai.inventory

@pytest.mark.skip
#this one is done 
def test_swap_newest_by_category():
    # Arrange
    # me
    item_a = Decor(age=1.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=0.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_d in tai.inventory 
    assert item_a in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_a not in tai.inventory


# @pytest.mark.skip
# def test_swap_best_by_category_reordered():
#     # Arrange
#     item_a = Decor(condition=2.0)
#     item_b = Electronics(condition=4.0)
#     item_c = Decor(condition=4.0)
#     tai = Vendor(
#         inventory=[item_c, item_b, item_a]
#     )

#     item_d = Clothing(condition=2.0)
#     item_e = Decor(condition=4.0)
#     item_f = Clothing(condition=4.0)
#     jesse = Vendor(
#         inventory=[item_f, item_e, item_d]
#     )

#     # Act
#     result = tai.swap_best_by_category(
#         other=jesse,
#         my_priority="Clothing",
#         their_priority="Decor"
#     )

#     assert result == True
#     assert len(tai.inventory) == 3
#     assert len(jesse.inventory) == 3
#     assert item_f in tai.inventory 
#     assert item_c in jesse.inventory
#     assert item_f not in jesse.inventory
#     assert item_c not in tai.inventory
#     # raise Exception("Complete this test according to comments below.")
#     # *********************************************************************
#     # ****** Complete Assert Portion of this test **********
#     # *********************************************************************
#     # Assertions should check:
#     # - That result is truthy
#     # - That tai and jesse's inventories are the correct length
#     # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there

@pytest.mark.skip
#this one is done
def test_swap_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_newest_by_category(
        other=jesse,
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


@pytest.mark.skip
#this one is done
def test_swap_newest_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


@pytest.mark.skip
#this one is done
def test_swap_newest_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(age=1.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    
