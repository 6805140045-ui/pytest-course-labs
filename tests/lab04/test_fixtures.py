
from shop import calculate_total


def test_total_with_fixture(sample_prices):
    result = calculate_total(sample_prices)

    assert result == 600


def test_empty_prices(empty_prices):
    result = calculate_total(empty_prices)

    assert result == 0


def test_product_factory(product_factory):
    product = product_factory("Keyboard", 500)

    assert product["name"] == "Keyboard"
    assert product["price"] == 500


def test_inventory_fixture(setup_inventory):
    assert setup_inventory["apples"] == 10

    setup_inventory["apples"] = 20

    assert setup_inventory["apples"] == 20
