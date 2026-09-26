import pytest
from working import convert

def test_convert_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")

def test_convert_invalid_hours():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
