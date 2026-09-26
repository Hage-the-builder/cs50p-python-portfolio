import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/4") == 0

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_convert_value_errors():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("5/4")
   
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
