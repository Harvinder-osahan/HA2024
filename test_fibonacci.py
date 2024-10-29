# test_fib.py

from Fibonacci import fib

def run_tests():
    with open('fibonacci_test_cases.txt', 'r') as file:
        for line in file:
            n, expected = map(int, line.split())
            result = fib(n)
            print(f"Fibonacci of {n} is: {result} (Expected: {expected})")
            assert result == expected, f"Test case failed for {n}: expected {expected}, got {result}"

if __name__ == "__main__":
    run_tests()
