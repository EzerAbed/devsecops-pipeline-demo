from app import add, is_even, greet

def test_add():
    assert add(2, 3) == 5

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

def test_greet():
    assert greet("Ace") == "Hello, Ace!"