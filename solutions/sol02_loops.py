# Solution 02: Loops and Lists

from src.basics.examples import sum_range, filter_even

def analyze_numbers(max_n):
    """
    Analyze numbers from 1 to max_n using src utilities.
    """
    # Get total sum using utility
    total_sum = sum_range(max_n)
    
    # Create list of all numbers
    all_numbers = list(range(1, max_n + 1))
    
    # Filter to get only evens
    even_numbers = filter_even(all_numbers)
    
    # Count the evens
    even_count = len(even_numbers)
    
    return {
        'total_sum': total_sum,
        'even_numbers': even_numbers,
        'even_count': even_count
    }

if __name__ == "__main__":
    result = analyze_numbers(10)
    print(f"Analysis for 1-10:")
    print(f"  Total sum: {result['total_sum']}")
    print(f"  Even numbers: {result['even_numbers']}")
    print(f"  Count of evens: {result['even_count']}")
