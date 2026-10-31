
import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# Baggage fee tests

def test_baggage_fee_invalid_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)


def test_baggage_fee_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_baggage_fee_within_allowance():
    assert baggage_fee("economy", 15, "domestic", False) == 0


def test_baggage_fee_member_allowance():
    assert baggage_fee("economy", 20, "domestic", True) == 0


def test_baggage_fee_business_member():
    assert baggage_fee("business", 40, "domestic", True) == 0


def test_baggage_fee_domestic_excess():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_baggage_fee_international_excess():
    assert baggage_fee("economy", 20, "international", False) == 225


def test_baggage_fee_domestic_excess_over_20():
    assert baggage_fee("economy", 36, "domestic", False) == 840


def test_baggage_fee_international_excess_over_20():
    assert baggage_fee("economy", 36, "international", False) == 2100


# Carry-on baggage tests

def test_carry_on_infant_allowed():
    assert carry_on_ok(20, 2, True) is True


def test_carry_on_infant_rejected():
    assert carry_on_ok(5, 3, True) is False


def test_carry_on_excess_weight():
    assert carry_on_ok(8, 1, False) is False


def test_carry_on_one_item_allowed():
    assert carry_on_ok(7, 1, False) is True


def test_carry_on_multiple_items_rejected():
    assert carry_on_ok(7, 2, False) is False


# Check-in status tests

def test_checkin_open_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_checkin_late_with_baggage():
    assert check_in_status(50, True, False) == "late"


def test_checkin_closed_with_baggage():
    assert check_in_status(44, True, False) == "closed"


def test_checkin_open_international_without_baggage():
    assert check_in_status(105, False, True) == "open"


def test_checkin_late_international_without_baggage():
    assert check_in_status(90, False, True) == "late"


def test_checkin_closed_international_without_baggage():
    assert check_in_status(89, False, True) == "closed"
