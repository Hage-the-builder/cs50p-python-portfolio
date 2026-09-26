from numb3rs import validate

def test_validate_good():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True

def test_validate_out_of_range():
    assert validate("256.1.1.1") is False
    assert validate("1.512.1.1") is False
    assert validate("1.1.1.300") is False

def test_validate_format():
    assert validate("1.1.1") is False
    assert validate("1.1.1.1.1") is False
    assert validate("cat") is False
