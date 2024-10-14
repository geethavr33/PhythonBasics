# Understanding Generators in Python

## What are Generators?

Generators are a type of iterable in Python that allow you to iterate through a sequence of values without storing the entire sequence in memory. They are defined using a function and utilize the `yield` statement to produce a series of values lazily.

## Key Features of Generators

1. **Memory Efficiency**: Generators yield one value at a time, which makes them more memory efficient than lists, especially when dealing with large datasets.

2. **Lazy Evaluation**: Values are generated on-the-fly as you iterate over them, which can lead to performance improvements.

3. **State Retention**: Generators maintain their state between iterations, meaning they can remember where they left off.

## How to Create a Generator

### Using a Function with `yield`

A generator function is defined like a normal function, but instead of returning a value using `return`, it uses `yield`. When `yield` is encountered, the function's state is saved, and the value is returned to the caller. The next time the generator is called, it resumes execution right after the last `yield`.

### Example

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for number in counter:
    print(number)
```
### Explanation of the Example:
+ The count_up_to function generates numbers from 1 to max.
+ Each time yield is executed, it provides the next value.
+ When the function is called, it returns a generator object that can be iterated over.
### Benefits of Generators
1.**Performance:**

Generators can be faster than using lists, especially when dealing with large amounts of data.

2.**Convenience:**

They provide a clear and concise way to write iterators without needing to implement the iterator protocol.

3.**No Need for Additional Memory:**

Since they produce items one at a time, they do not require additional memory to store the entire collection of values.
### Use Cases
+ Reading Large Files:

Generators can read files line by line instead of loading the entire file into memory.
* Infinite Sequences:

Generators can be used to create infinite sequences, such as Fibonacci numbers.
* Data Streams:

They are useful for processing data streams in real-time.
### Conclusion
Generators are a powerful feature in Python that allow for efficient and flexible iteration over sequences of data. By using yield, you can create iterators that are both memory 
efficient and easy to implement. This makes them a great choice for scenarios where performance and resource management are critical.

# Object-Oriented Programming (OOP) Examples

---
## 1. Program to Check Whether a Number is Prime or Not

A **prime number** is a number greater than 1 that has no divisors other than 1 and itself.

### Python Code:
```python
def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    return primes

# Example usage:
limit = int(input("Enter a number: "))
prime_numbers = generate_primes(limit)
print(f"Prime numbers below {limit}: {prime_numbers}")
```
---
## 2. Find All Prime Numbers in a Given Range

```python
class PrimeRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_primes(self):
        primes = []
        for num in range(self.start, self.end + 1):
            if num > 1:
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    primes.append(num)
        return primes

# Example usage:
prime_range = PrimeRange(10, 50)
print(prime_range.get_primes())  # Output: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

```
---
## 3. Fibonacci Series Program
The Fibonacci series is a sequence in which each number is the sum of the two preceding ones, starting from 0 and 1.

```python
class Fibonacci:
    def __init__(self, n):
        self.n = n
    
    def generate(self):
        fib_sequence = [0, 1]
        for i in range(2, self.n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[:self.n]

# Example usage:
fib = Fibonacci(10)
print(fib.generate())  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

---
## 4. getattr() Function
The ```getattr()``` function is used to get the value of an object's attribute dynamically. If the attribute does not exist, it returns a default value (if specified).

Example:
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

# Main program to demonstrate getattr
car = Car("Toyota", "Corolla", 2020)

# Using getattr to access attributes
brand = getattr(car, 'brand')
model = getattr(car, 'model')
year = getattr(car, 'year')

print(f"Brand: {brand}")   # Outputs: Brand: Toyota
print(f"Model: {model}")   # Outputs: Model: Corolla
print(f"Year: {year}")     # Outputs: Year: 2020
```

---
## 5. yield and next() in Python
The yield keyword is used to make a function a generator, allowing it to yield values one at a time instead of returning them all at once. The next() function is used to retrieve the next value from a generator.

Example Using yield and next():
```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fib_gen = fibonacci_generator()

# Get the first five Fibonacci numbers using next()
print(next(fib_gen))  # Output: 0
print(next(fib_gen))  # Output: 1
print(next(fib_gen))  # Output: 1
print(next(fib_gen))  # Output: 2
print(next(fib_gen))  # Output: 3
```
In this example:

yield produces values one at a time when the generator is called.
```next()``` retrieves the next value generated by ```yield```.


### Summary of Topics Covered:
1. **Prime number checking**: A class-based solution to check if a number is prime and to find all prime numbers in a given range.
2. **Fibonacci series**: A class-based implementation to generate a Fibonacci sequence.
3. **`getattr()`**: A built-in function used to dynamically access object attributes.
4. **`yield` and `next()`**: Demonstrated how generators work with `yield` and how to get values from them using `next()`.