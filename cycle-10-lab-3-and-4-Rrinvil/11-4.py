def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence


try:
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n <= 0:
        raise ValueError("Please enter a positive integer.")
    
    result = fibonacci(n)
    print(result)
except ValueError as e:
    print(f"Error: {e}. Please enter a valid positive integer.")

