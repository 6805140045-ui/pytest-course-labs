
import pytest

from shop import add, calculate_total, apply_discount


class TestShoppingCart:

    def test_cart_total(self):
        prices = [100, 200, 300]

        assert calculate_total(prices) == 600

    def test_empty_cart(self):
        prices = []

        assert calculate_total(prices) == 0


class TestDiscount:

    def test_discount_result(self):
        assert apply_discount(100, 10) == 90

    def test_full_discount(self):
        assert apply_discount(100, 100) == 0


def test_addition():
    assert add(5, 5) == 10


def test_multiple_conditions():
    result = calculate_total([10, 20, 30])

    assert result == 60
    assert result > 0
    assert isinstance(result, int)


@pytest.mark.smoke
def test_basic_smoke_test():
    assert add(2, 3) == 5


@pytest.mark.skip(reason="Demonstration of skipping a test")
def test_skipped_example():
    assert add(1, 1) == 2


@pytest.mark.xfail(reason="Demonstration of an expected failure")
def test_expected_failure():
    assert add(1, 1) == 3
