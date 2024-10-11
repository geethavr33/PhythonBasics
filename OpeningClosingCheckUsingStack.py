
var = "{()[]}"
dict1 = {"{": "}", "(": ")", "[": "]", "<": ">"}
length = len(var)
 
# Check if the length of the string is even
if length % 2 == 0:
    stack = []  # Initialize an empty stack to keep track of opening brackets
 
    # Iterate through each character in the string
    for i in var:
        if i in dict1.keys():  # If it's an opening bracket
            stack.append(i)  # Push the opening bracket onto the stack
        elif i in dict1.values():  # If it's a closing bracket
            if stack and dict1[stack[-1]] == i:  # Check if the stack is not empty and matches
                stack.pop()  # Pop the matched opening bracket
            else:
                print("Brackets are not balanced.")
                break
    else:
        # If we exit the loop without breaking, check if the stack is empty
        if not stack:
            print("Brackets are balanced.")
        else:
            print("Brackets are not balanced.")
else:
    print("Brackets are not balanced.")
 
 