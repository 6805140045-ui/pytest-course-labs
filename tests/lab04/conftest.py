
import pytest


@pytest.fixture
def sample_prices():
    return [100, 200, 300]


@pytest.fixture
def empty_prices():
    return []


@pytest.fixture
def product_factory():
    def create_product(name="Product", price=100):
        return {
            "name": name,
            "price": price
        }

    return create_product


@pytest.fixture
def setup_inventory():
    inventory = {"apples": 10}

    yield inventory

    inventory.clear()
