# Solution 01: Variables and Validation

from src.basics.examples import validate_age, greet

def create_user_profile(name, age):
    """
    Create a user profile dictionary with validation.
    """
    if not validate_age(age):
        return None
    
    return {
        'name': name,
        'age': age,
        'greeting': greet(name)
    }

if __name__ == "__main__":
    print(create_user_profile("Alice", 25))
    print(create_user_profile("Bob", -5))  # Returns None
    print(create_user_profile("Charlie", "30"))  # Returns None
