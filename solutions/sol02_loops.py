# Solution 02: Loops

def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    print(f"Sum of 1-5 is: {sum_numbers(5)}")
