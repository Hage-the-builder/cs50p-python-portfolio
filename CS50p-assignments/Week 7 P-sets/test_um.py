from um import count

def test_count_isolated():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_count_subwords():
    assert count("yummy") == 0
    assert count("aluminum") == 0

def test_count_multiple():
    assert count("um, hello, um, world") == 2
