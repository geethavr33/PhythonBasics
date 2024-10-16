def jump(nums):
   
    jumps = 0         
    farthest = 0      
    end = 0            
    
    # Iterate through the array except the last index
    for i in range(len(nums) - 1):
        # Update the farthest index we can reach
        farthest = max(farthest, i + nums[i])
        
        # If we've reached the end of the current jump range
        if i == end:
            jumps += 1      # Make a jump
            end = farthest  # Update the end to the farthest point we can reach

    return jumps


print(jump([2, 3, 1, 1, 4]))  # Output: 2
print(jump([2, 2, 0, 1, 4]))  # Output: 2
