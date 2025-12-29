# Exercise 02: Loops and Lists
# Goal: Use loops to process data and filter results using src utilities.

from src.basics.examples import sum_range, filter_even

def analyze_numbers(max_n):
    """
    Analyze numbers from 1 to max_n.
    Requirements:
    1. Use sum_range() from src to get the total sum
    2. Create a list of all numbers from 1 to max_n
    3. Use filter_even() from src to get only even numbers
    4. Calculate the count of even numbers
    5. Return a dict with keys: 'total_sum', 'even_numbers', 'even_count'
    
    Example:
        analyze_numbers(5)
        # Returns: {
        #     'total_sum': 15,
        #     'even_numbers': [2, 4],
        #     'even_count': 2
        # }
    """
    # TODO: Implement this function
    pass

if __name__ == "__main__":
    result = analyze_numbers(10)
    print(f"Analysis for 1-10:")
    print(f"  Total sum: {result['total_sum']}")
    print(f"  Even numbers: {result['even_numbers']}")
    print(f"  Count of evens: {result['even_count']}")
