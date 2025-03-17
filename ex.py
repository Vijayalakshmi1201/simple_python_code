# factorial.py

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        eturn 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Calculate factorial using iteration."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial (Recursive): {factorial_recursive(num)}")
            print(f"Factorial (Iterative): {factorial_iterative(num)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
