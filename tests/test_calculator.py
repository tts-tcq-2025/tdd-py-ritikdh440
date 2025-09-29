import pytest
from calculator import add


def test_add_empty_string():
    assert add("") == 0


def test_add_single_number():
    assert add("5") == 5


def test_add_two_numbers():
    assert add("1,2") == 3


def test_add_with_newline():
    assert add("1\n2,3") == 6


def test_add_custom_delimiter():
    assert add("//;\n1;2;3") == 6


def test_add_ignore_large_numbers():
    assert add("2,1001") == 2
    assert add("1000,1001,1") == 1001


def test_add_negative_raises_single():
    with pytest.raises(ValueError, match="negatives not allowed: -4"):
        add("1,-4,5")


def test_add_negative_raises_multiple():
    with pytest.raises(ValueError, match="negatives not allowed: -1, -3"):
        add("-1,2,-3")
