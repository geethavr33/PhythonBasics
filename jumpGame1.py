def canJump(nums):
    # Variable to store the farthest index we can reach
    maxReach = 0
    
    # Iterate over each index in the array
    for i in range(len(nums)):
        # If the current index is beyond the farthest we can reach, return False
        if i > maxReach:
            return False
        # Update maxReach to the farthest index we can jump to from this position
        maxReach = max(maxReach, i + nums[i])
        # If maxReach reaches or exceeds the last index, return True
        if maxReach >= len(nums) - 1:
            return True
    
    # If we complete the loop and can't reach the end, return False
    return False

# Test cases
print(canJump([2, 3, 1, 1, 4]))  # Output: True
print(canJump([3, 2, 1, 0, 4]))  # Output: False

