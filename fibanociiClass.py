class FibonacciGenerator:
    def __init__(self, limit):
        self.limit = limit  # Set the upper limit for the Fibonacci series
        self.a, self.b = 0, 1  # Start with the first two Fibonacci numbers

    def next_fibonacci(self):
        # Generate the next Fibonacci number
        if self.a < self.limit:
            fib = self.a
            self.a, self.b = self.b, self.a + self.b  # Update to the next Fibonacci numbers
            return fib  # Return the current Fibonacci number
        return None  # Return None when the limit is reached

# Example usage:
limit = int(input("Enter a number: "))
fib_gen = FibonacciGenerator(limit)

# Print all Fibonacci numbers below the limit
while True:
    fib_number = fib_gen.next_fibonacci()
    if fib_number is None:  # Stop if there are no more Fibonacci numbers
        break
    print(fib_number)
