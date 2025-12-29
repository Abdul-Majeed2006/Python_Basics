# Exercise 01: Variables and Validation
# Goal: Practice variable creation AND data validation using src utilities.

from src.basics.examples import validate_age, greet

def create_user_profile(name, age):
    """
    Create a user profile dictionary.
    Requirements:
    1. Use validate_age() from src to check if age is valid
    2. If invalid, return None
    3. If valid, return a dict with 'name', 'age', and 'greeting' keys
    4. Use greet() from src to generate the greeting
    
    Example:
        create_user_profile("Alice", 25)
        # Returns: {'name': 'Alice', 'age': 25, 'greeting': 'Hello, Alice!'}
    """
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    # Test your implementation
    print(create_user_profile("Alice", 25))
    print(create_user_profile("Bob", -5))  # Should return None
    print(create_user_profile("Charlie", "30"))  # Should return None
