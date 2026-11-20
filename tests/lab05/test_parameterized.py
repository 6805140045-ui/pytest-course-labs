
import pytest

from shop import add, apply_discount, is_valid_quantity


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, 20, 30),
        (-1, 1, 0),
        (0, 0, 0)
    ]
)
def test_addition(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "total, percentage, expected",
    [
        (100, 10, 90),
        (200, 25, 150),
        (100, 50, 50),
        (100, 0, 100),
        (100, 100, 0)
    ]
)
def test_discounts(total, percentage, expected):
    assert apply_discount(total, percentage) == expected


@pytest.mark.parametrize(
    "quantity, expected",
    [
        (1, True),
        (5, True),
        (10, True),
        (0, False),
        (-1, False),
        (2.5, False),
        (True, False)
    ]
)
def test_quantities(quantity, expected):
    assert is_valid_quantity(quantity) is expected


@pytest.mark.parametrize(
    "percentage",
    [-10, 110, 150]
)
def test_invalid_discounts(percentage):
    with pytest.raises(ValueError):
        apply_discount(100, percentage)
