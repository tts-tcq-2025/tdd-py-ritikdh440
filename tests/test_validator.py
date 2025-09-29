import pytest
from validator import has_content, no_negatives


def test_has_content():
    assert not has_content("")
    assert has_content("1")


def test_no_negatives_valid():
    no_negatives(["1", "2", "3"])  # Should not raise


def test_no_negatives_raises_single():
    with pytest.raises(ValueError, match="negatives not allowed: -1"):
        no_negatives(["-1", "2", "3"])


def test_no_negatives_raises_multiple():
    with pytest.raises(ValueError, match="negatives not allowed: -2, -5"):
        no_negatives(["-2", "0", "-5"])
