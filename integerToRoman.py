def int_to_roman(num):
    
    roman_dict = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"
    }

    
    roman_numeral = ""
    
   
    for value in sorted(roman_dict.keys(), reverse=True):
        while num >= value:
            roman_numeral += roman_dict[value]
            num -= value

    return roman_numeral


num = int(input("Enter an integer to convert to Roman numeral: "))

if num <= 0:
    print("Roman numerals are not defined for numbers less than 1.")
else:
    print(int_to_roman(num))
