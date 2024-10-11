# Python Decorator

A decorator in Python is a function that modifies the behavior of another function or method. Decorators allow you to add functionality to an existing function in a clean, readable, and reusable way.

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
## **2. get() method in Dictionaries** ##

The get() method in Python dictionaries is used to retrieve the value associated with a specified key. It provides a safer way to access dictionary elements compared to using square brackets, as it allows you to handle cases where the key might not exist without raising an error. If the specified key is not found, get() returns None or a specified default value, which makes it particularly useful for avoiding KeyError exceptions.

### *Syntax* ###

```python
dict.get(key, default=None)
```
### *Parameters* ###

* key: The key you want to look up in the dictionary.

* default (optional): The value to return if the specified key does not exist in the dictionary. If not provided, it defaults to None.
  
### Example ###

```python
# Creating a dictionary
person = {
    "name": "Geetha",
    "age": 40,
    "city": "Thiruvananthapuram"
}

# Using get() to access an existing key
name = person.get("name")  # Returns "Geetha"

# Using get() to access a non-existing key
country = person.get("country")  # Returns None

# Using get() with a default value
country_with_default = person.get("country", "Thiruvananthapuram")  # Returns "Thiruvananthapuram"

# Printing the results
print(name)                   # Output: Geetha
print(country)                # Output: None
print(country_with_default)    # Output: Thiruvananthapuram
```

### Explanation ###

1. Creating a Dictionary: 

* We define a dictionary called person with keys name, age, and city.

2. Accessing an Existing Key:

*  The get() method is used to access the value associated with the key "name". Since "name" exists in the dictionary, it returns "Geetha".
  
3. Accessing a Non-Existing Key:

* When we try to access the key "country" using get(), it returns None since that key does not exist in the dictionary. This prevents a KeyError from being raised.
  
4. Using a Default Value:

* We use get() again to access "country" but this time we provide a default value of "USA". Since "country" does not exist in the dictionary, get() returns the default value "Thiruvananthapuram" instead of None.
  
5. Printing Results: Finally, we print the results of the get() method calls to see the output.

## **3. List Comprehension** 

List comprehension is a concise and efficient way to create lists in Python. It provides a more readable and expressive syntax for generating lists compared to using traditional loops. List comprehensions allow you to create a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string), optionally filtering items based on a condition.

### Syntax ###

```python
new_list = [expression for item in iterable if condition]
```

* expression: The value or operation to be applied to each item.

* item: The variable representing each element in the iterable.

* iterable: Any Python iterable (like a list, tuple, or string).

* condition (optional): A filter that determines whether the item should be included in the new list.
  
### Example 1 ###

Here’s a basic example of using list comprehension to create a list of squares of numbers:

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# List comprehension to create a list of squares
squares = [x ** 2 for x in numbers]

print(squares)  # Output: [1, 4, 9, 16, 25]
```

### *Explanation* ###

* Input List: The original list numbers contains integers from 1 to 5.

* List Comprehension: The expression x ** 2 computes the square of each number in the numbers list.

* Output List: The resulting list squares contains the squares of the original numbers.


### Example 2 ###

We can also add a condition to filter the items included in the new list. Here’s an example that creates a list of even numbers:

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension to create a list of even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

### *Explanation* ###

1. Condition: The condition if x % 2 == 0 filters out only the even numbers from the numbers list.

2. Output List: The resulting list even_numbers contains only the even numbers from the original list.

## **Exercises** ##

### 1. Majority Element ###

It counts how many times each element appears and then finds all elements that have the highest frequency. This is particularly useful for understanding the distribution of elements in the list.

## Code ##
```python
def most_repeated_integer(lst):
    if not lst:
        return None  # Return None if the list is empty

    count_dict = {}

    # Count occurrences using get()
    for num in lst:
        if count_dict.get(num, False):  # If key exists, increment its value
            count_dict[num] += 1
        else:  # Otherwise, initialize it with 1
            count_dict[num] = 1

    # Find the key with the highest value in the dictionary
    most_repeated = max(count_dict, key=count_dict.get)

    return most_repeated

# Example usage:
numbers = [1, 2, 3, 4, 2, 5, 2, 3, 4, 4, 4, 5]
result = most_repeated_integer(numbers)
print(f"The most repeated integer is: {result}")

```

### *Output* ###

```python
The most repeated integer is: 4
```
### *Explanation:* ###


count_dict.get(num, False) checks if the number num exists in the dictionary. If it does, we increment its value; if not, we set it to 1.  

This approach mirrors the logic you're referring to, using get() to handle the existence check and initialization of the count dictionary.

Step 1: We first check if the input list is empty. If it is, we return None, as there are no integers to count.

Step 2: We initialize an empty dictionary count_dict. This will store each unique integer from the list as the key, and the count of occurrences as the value.

Step 3: We iterate through each integer num in the list lst.

count_dict.get(num, False):

What it does: The get(num, False) checks if the integer num already exists as a key in count_dict.
If the key exists: get() will return the value associated with that key (i.e., the current count of the integer).
If the key does not exist: get() returns False. This mimics the behavior of the default value you're referring to (e.g., get("1", False) returns False if "1" is not a key).
Checking if count_dict.get(num, False):

If the key num exists in count_dict, the value (the current count) will be a truthy value, so the if statement is true, and we increment the count for that key.
If the key num does not exist, get() returns False, and we initialize the count of that integer to 1 (since this is the first occurrence of the number).
### 2. Palindrome ###

A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. In simpler terms, a palindrome remains unchanged when its characters are reversed. Here we are only consider the alphanumeric characters in the given string.

## Code ##

```python
string1 = input("Enter the string: ")

# Create an empty string called string2 to store only the alphanumeric characters from the original input
string2 = ''

# Iterate through each character in the input string
for char in string1:
    # Check if the character is alphanumeric
    if char.isalnum():
        # Convert to lowercase and add to the string2
        string2 += char.lower()

# Check if the string2 is a palindrome
if string2 == string2[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
```
The logic of the code is as follows:

The provided code snippet checks if a given input string is a palindrome. A palindrome is a sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and case differences. This code filters out only alphanumeric characters from the input, converts them to lowercase, and then checks if the resulting string is a palindrome.

### 3. Best Time To Buy and  Sell ###

Given a list of stock prices where each index represents a day, the code calculates the maximum profit that can be achieved by buying on one day and selling on a future day. It also identifies the specific days for buying and selling based on this maximum profit.

## Code ##

```python
# Given list of prices
a = [7, 1, 3, 4]

max_diff = 0 #max_diff is initialized to 0 to track the maximum price difference found.
buy_day = -1  # Initialize to -1 to indicate no valid day found
sell_day = -1  # Initialize to -1 to indicate no valid day found

# Iterate through the list to find max difference
for i in range(len(a)): #The outer loop iterates through each price in the list using index i.
    for j in range(i + 1, len(a)): #The inner loop iterates through the prices that come after the current price (using index j), specifically starting from i + 1. 
        #This ensures that we only look at future prices to simulate buying first and then selling later.
        diff = a[j] - a[i] #For each pair of prices a[i] (buy price) and a[j] (sell price), the code calculates the price difference:
        if diff > max_diff: #If the calculated difference (diff) is greater than the current max_diff
            #max_diff to the new maximum difference.
            # buy_day to the current index i (the index of the buying day).
            #sell_day to the current index j (the index of the selling day).
            max_diff = diff
            buy_day = i  # Index of buy day
            sell_day = j  # Index of sell day

# Print the best day to buy and sell
if buy_day != -1 and sell_day != -1:
    print(f"Best day to buy: Day {buy_day + 1} (Price: {a[buy_day]})")
    print(f"Best day to sell: Day {sell_day + 1} (Price: {a[sell_day]})")
else:
    print("No profitable buy/sell days found.")
```

The basic logic of the code can be summarized as follows:

1. Initialize Variables: Start by setting up variables to track the maximum profit (max_diff), the best day to buy (buy_day), and the best day to sell (sell_day).

2. Nested Loop: Use two loops:

* The outer loop iterates through each price in the list, treating the current price as the buying price.

* The inner loop iterates through the subsequent   prices, treating each one as a potential selling price.
  
3. Calculate Profit: For each pair of buying and selling prices.

* Calculate the profit as the difference between the selling price and the buying price.

4. Update Maximum Profit: If the calculated profit is greater than the previously recorded maximum profit:

* Update the maximum profit.
* Record the current indices as the best buying and selling days.
  
5. Output Results: After checking all possible pairs:

* If valid buy and sell days are found, print them along with their prices.

* If no profitable transaction is found, print a message indicating that.
