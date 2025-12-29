from src.basics.examples import add, greet

def test_variables():
    x = 5
    y = 10
    assert x + y == 15

def test_string_methods():
    text = "python"
    assert text.upper() == "PYTHON"

def test_loop_sum():
    total = 0
    for i in range(5):
        total += i
    assert total == 10

def test_imported_function():
    assert add(2, 3) == 5

def test_greet():
    assert greet("World") == "Hello, World!"
