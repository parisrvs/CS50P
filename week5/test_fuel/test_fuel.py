from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

    with pytest.raises(ValueError):
        convert("three/four")

    with pytest.raises(ValueError):
        convert("1/-3")

    with pytest.raises(ValueError):
        convert("1.5/3")

    with pytest.raises(ValueError):
        convert("1.5/3.3")

    with pytest.raises(ValueError):
        assert convert("5/4")

    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
