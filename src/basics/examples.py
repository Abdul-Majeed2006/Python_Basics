def add(x, y):
    """
    A simple example function to demonstrate testing.
    """
    return x + y

def greet(name):
    """
    A simple string manipulation example.
    """
    return f"Hello, {name}!"

def validate_age(age):
    """
    Validates that an age is a positive integer.
    Returns True if valid, False otherwise.
    """
    return isinstance(age, int) and age > 0

def sum_range(n):
    """
    Calculate the sum of numbers from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def filter_even(numbers):
    """
    Return only even numbers from a list.
    """
    return [num for num in numbers if num % 2 == 0]
