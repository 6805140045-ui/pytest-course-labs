
from unittest.mock import MagicMock, patch

import pytest

from shop import checkout, get_timestamp


def test_checkout_successful():
    payment_gateway = MagicMock()
    fake_clock = MagicMock(return_value=123456789)

    cart = [100, 200, 300]

    result = checkout(
        cart,
        payment_gateway,
        fake_clock
    )

    assert result["total"] == 600
    assert result["paid_at"] == 123456789

    payment_gateway.charge.assert_called_once_with(600)
    fake_clock.assert_called_once()


def test_checkout_empty_cart():
    payment_gateway = MagicMock()
    fake_clock = MagicMock()

    with pytest.raises(ValueError):
        checkout([], payment_gateway, fake_clock)

    payment_gateway.charge.assert_not_called()
    fake_clock.assert_not_called()


def test_payment_gateway_failure():
    payment_gateway = MagicMock()
    payment_gateway.charge.side_effect = RuntimeError(
        "Payment failed"
    )

    fake_clock = MagicMock(return_value=123456789)

    with pytest.raises(RuntimeError):
        checkout([100], payment_gateway, fake_clock)

    payment_gateway.charge.assert_called_once_with(100)


def test_mock_time():
    with patch("shop.time.time", return_value=123456789):
        result = get_timestamp()

    assert result == 123456789
