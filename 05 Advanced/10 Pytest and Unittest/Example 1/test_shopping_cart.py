import pytest
from pytest import MonkeyPatch
from item_database import ItemDatabase
from shopping_cart import ShoppingCart


@pytest.fixture
def cart():
    return ShoppingCart(max_size=5)


def test_add_item(cart):
    cart.add_item("apple")
    assert cart.get_size() == 1


def test_get_items(cart):
    cart.add_item("apple")
    assert "apple" in cart.get_items()


def test_max_size_items(cart):
    for _ in range(5):
        cart.add_item("apple")
    with pytest.raises(OverflowError):
        cart.add_item("apple")


def test_get_total_price(cart: ShoppingCart, monkeypatch: MonkeyPatch):
    cart.add_item("apple")
    cart.add_item("apple")
    cart.add_item("orange")
    item_database = ItemDatabase()
    
    # mock function
    def mock_get(self, item: str):
        if item == "apple":
            return 20
        if item == "orange":
            return 50
    monkeypatch.setattr(ItemDatabase, "get", mock_get)

    assert cart.get_total_price(item_database) == 90

