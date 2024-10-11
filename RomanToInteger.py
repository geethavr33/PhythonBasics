def roman_to_integer(roman):
    # Define a dictionary for Roman numeral values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through the Roman numeral from right to left
    for char in reversed(roman):
        value = roman_values[char]
        
        # If the current value is less than the previous one, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

# Example usage
roman_numeral = "XVI"
print(f"The integer value of {roman_numeral} is {roman_to_integer(roman_numeral)}")
