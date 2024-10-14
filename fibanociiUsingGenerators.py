def generate(l1):
        a, b = 0, 1
        while a < limit:
            yield a  # Yield the next number in the Fibonacci sequence
            a, b = b, a + b  # Move to the next Fibonacci numbers

        

limit = int(input("Enter a number: "))
fibonacci_numbers = generate(limit)

for i in fibonacci_numbers:
    print(i)
