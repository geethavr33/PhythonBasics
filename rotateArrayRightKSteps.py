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
