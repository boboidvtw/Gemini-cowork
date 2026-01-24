# math_check.py

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Calculate Fibonacci numbers and factorial of 15
fib_numbers = fibonacci(20)
factorial_15 = factorial(15)

print("Fibonacci Numbers:", fib_numbers)
print("Factorial of 15:", factorial_15)