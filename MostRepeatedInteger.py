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
