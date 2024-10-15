# Day 5 Tasks
## I.Factorial using a recursive function

Here’s a Python program that calculates the factorial of a number using a recursive function:

```python
def factorial(n):
    # Base case: if n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number to find its factorial: "))

# Checking if the number is negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")
```
### Explanation:
* The factorial function is a recursive function that computes the factorial of n.
* The base case is when n is 0 or 1, where the factorial is 1 (because 0! = 1! = 1).
* The recursive case is n * factorial(n - 1), which breaks the problem into smaller subproblems until it reaches the base case.

## II.Integer to Roman

To implement the conversion of an integer to a Roman numeral, we need to address the core principles of Roman numeral formation:

1. **Subtractive Notation**: When the number starts with 4 or 9, we use the subtractive form (like IV for 4, IX for 9, etc.).
2. **Maximal Value Selection**: When the number does not start with 4 or 9, we select the largest symbol that can be subtracted and repeatedly append it.
3. **Repeating Symbols**: Only I, X, C, and M (powers of 10) can appear consecutively, up to three times.

Here’s how we can translate this logic into Python:

```python
def int_to_roman(num):
    # Define the values and symbols for Roman numerals
    roman_dict = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"
    }

    # Roman numeral result string
    roman_numeral = ""
    
    # Start from the highest decimal place and move to the lowest
    for value in sorted(roman_dict.keys(), reverse=True):
        # Subtractive form (if the number starts with 4 or 9)
        while num >= value:
            roman_numeral += roman_dict[value]
            num -= value

    return roman_numeral

# Input from the user
num = int(input("Enter an integer to convert to Roman numeral: "))

if num <= 0:
    print("Roman numerals are not defined for numbers less than 1.")
else:
    print(f"The Roman numeral of {num} is {int_to_roman(num)}")
```
### Explanation of Key Points in the Code:
### 1.Subtractive Forms for 4 and 9:

* In Roman numerals, 4 is represented as IV (1 less than 5), and 9 is represented as IX (1 less than 10). These rules are also applied for other decimal place values like 40 (XL), 90 (XC), 400 (CD), and 900 (CM).

```python
roman_dict = {
    1: "I", 4: "IV", 5: "V", 9: "IX",
    10: "X", 40: "XL", 50: "L", 90: "XC",
    100: "C", 400: "CD", 500: "D", 900: "CM",
    1000: "M"
}
```
### 2.Maximal Value Selection:

* For numbers that don’t involve subtractive notation, like 3 or 8, the largest numeral that fits into the number is selected, appended to the result, and subtracted from the number.
* For instance, for 3, we append "I" three times (3 = I + I + I), while for 8, we append "V" and "III" (8 = V + I + I + I).
### 3.Powers of 10 can be repeated:

* I, X, C, and M can appear consecutively, but only up to three times.
* For instance, 3 is "III", and 30 is "XXX". If a number would require more than three consecutive repetitions, the subtractive form is used (e.g., 40 becomes "XL" instead of "XXXX").
### 4.How the Program Works:

* The loop processes the number starting with the largest Roman numeral (1000 = M) and works downwards.
* At each step, the program subtracts the largest possible numeral value from the input number and appends the corresponding Roman numeral symbol.

# III.Reverse Words in a String

Here’s a Python program that reverses the order of words in a string using a class:

```python
class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Split the string into words, reverse the list of words, and join them back into a string
        words = self.input_string.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words

# Input from the user
user_input = input("Enter a string to reverse the order of words: ")

# Create an instance of StringReverser
reverser = StringReverser(user_input)

# Call the reverse_words method and display the result
reversed_string = reverser.reverse_words()
print(f"The string with reversed word order is: {reversed_string}")
```
## Explanation:
### 1.Class Definition (StringReverser):

* The __init__ method initializes the class with the input string.
* The reverse_words method:
>* Splits the input string into a list of words using split().
>* Reverses the list of words using reversed().
>* Joins the reversed words back into a single string with " ".join().
### 2.Input:

* The user provides a string with multiple words.
### 3.Reversing the Words:

* The program reverses the order of words in the input string, but not the characters within the words.
  
## IV.Remove Duplicates from Sorted Array

Here’s a Python program that removes excess duplicates from a sorted array, allowing each unique element to appear at most twice, and replaces the remaining elements with underscores (`_`).

```python
def remove_excess_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)  # If the array has 2 or fewer elements, return its length
    
    # Pointer to place the next valid element
    i = 2  # Start from the third position since the first two can always be kept
    
    # Iterate through the array starting from the third element
    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    
    # Replace the remaining elements after the valid ones with '_'
    for x in range(i, len(nums)):
        nums[x] = '_'
    
    return i  # 'i' is the count of valid elements

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = remove_excess_duplicates(nums)

# Output the modified array and the count of valid elements
print(f"Number of valid elements: {k}")
print(f"Modified array: {nums}")
```
### Explanation of the Changes:
1. Valid Elements (i): The i pointer tracks the next valid position where an element should be placed. It starts from 2 because the first two elements can always be kept.

2. Removing Duplicates: As the function iterates through the array, if the current element nums[j] is not the same as nums[i-2], it means it can be placed in the i-th position.

3. Replacing Excess Elements: After all valid elements are placed in the array, the remaining positions (from i to the end of the array) are filled with underscores (_).

4. Return the Count (k): The function returns i, which is the count of valid elements.

Example:
For the input nums = [1, 1, 1, 2, 2, 3]:

After running the function, k = 5 (there are 5 valid elements), and the array becomes [1, 1, 2, 2, 3, '_'].

## V Array Rotator

Here’s a Python program that defines a class to rotate an array to the right by a specified number of steps:

```python
class ArrayRotator:
    def __init__(self, nums):
        self.nums = nums

    def reverse(self, start, end):
        """Helper method to reverse elements of the array in-place between start and end."""
        while start < end:
            self.nums[start], self.nums[end] = self.nums[end], self.nums[start]
            start += 1
            end -= 1

    def rotate(self, k):
        """Method to rotate the array to the right by k steps."""
        n = len(self.nums)
        k = k % n  # Handle cases where k is larger than the array size
        
        # Step 1: Reverse the entire array
        self.reverse(0, n-1)
        
        # Step 2: Reverse the first k elements
        self.reverse(0, k-1)
        
        # Step 3: Reverse the remaining elements
        self.reverse(k, n-1)

# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

rotator = ArrayRotator(nums)
rotator.rotate(k)

# Output the rotated array
print(f"Rotated array: {rotator.nums}")
```
## Explanation:
### 1.Class ArrayRotator:

* The class is initialized with the array nums. The array is stored as an instance variable self.nums.
### 2. Reverse Method:

* This is a helper method that reverses a portion of the array in-place, from index start to index end.
### 3.rotate Method:

* This method performs the array rotation in three steps:
>* It first reverses the entire array.
>* Then, it reverses the first k elements.
>* Finally, it reverses the remaining elements.
### 4.Object Instantiation and Usage:

* We create an instance of ArrayRotator with the input array nums, and then call the rotate method with the value k.