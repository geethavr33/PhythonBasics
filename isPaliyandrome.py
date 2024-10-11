class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a new string with only alphanumeric characters and convert to lowercase
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string is the same forwards and backwards
        return cleaned_string == cleaned_string[::-1]

# Example usage
solution = Solution()
input_string = "A man, a plan, a canal, Panama!"
if solution.isPalindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
