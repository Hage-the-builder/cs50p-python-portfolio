from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello, friend") == 0

def test_value_h():
    assert value("hi") == 20
    assert value("Hey there") == 20

def test_value_other():
    assert value("What's up?") == 100
    assert value("Good morning") == 100
