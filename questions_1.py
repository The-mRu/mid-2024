def fibonacci(n):
    # Initialize the first two numbers
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] < n:     
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) # Calculate the next Fibonacci number
    return fib_sequence


n = int(input("enter the value of n : ")) #enter the value of n


# Print the generated Fibonacci sequence
print(f"The generated Fibonacci sequence :  {fibonacci(n)}")