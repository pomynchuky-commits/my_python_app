from app import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 7) == 7

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_positive_and_negative():
    assert add(10, -4) == 6
