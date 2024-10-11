# Python Decorator

A decorator in Python is a function that modifies the behavior of another function or method. Decorators allow you to add functionality to an existing function in a clean, readable, and reusable way.

## Table of Contents
- [Python Decorator](#python-decorator)
  - [Table of Contents](#table-of-contents)
  - [Basic Structure of a Decorator](#basic-structure-of-a-decorator)
    - [Python Code:](#python-code)
  - [Applying a Decorator](#applying-a-decorator)
    - [Python Code:](#python-code-1)
    - [The @decorator\_function syntax is shorthand for:](#the-decorator_function-syntax-is-shorthand-for)
    - [Python Code:](#python-code-2)
    - [Example of a Simple Decorator](#example-of-a-simple-decorator)
    - [Python Code:](#python-code-3)
  - [Output:](#output)

---

## Basic Structure of a Decorator

### Python Code:

```python
def decorator_function(func):
    def wrapper(*args, **kwargs):
        # Code to execute before the wrapped function
        result = func(*args, **kwargs)
        # Code to execute after the wrapped function
        return result
    return wrapper
```

 **Bubble Sort** and **Merge Sort**, along with a utility for **sorting words in a list**.

## Applying a Decorator
### Python Code:

```python
@decorator_function
def my_function():
    print("Function is running")
```

### The @decorator_function syntax is shorthand for:
### Python Code:

```python
my_function = decorator_function(my_function)
```


### Example of a Simple Decorator

### Python Code:

```python
ddef say_hello_decorator(func):
    def wrapper():
        print("Hello!")
        return func()
    return wrapper

@say_hello_decorator
def greet():
    print("Good morning!")

greet()
```

## Output:

Hello!  
Good morning!

