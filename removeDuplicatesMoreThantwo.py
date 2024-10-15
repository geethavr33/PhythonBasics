def remove_excess_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)  
    i = 2 
    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    
    for x in range(i, len(nums)):
        nums[x] = '_'
    
    return i 

nums = [1, 1, 1, 2, 2, 3,3,3]
k = remove_excess_duplicates(nums)

print(f"Number of valid elements: {k}")
print(f"Modified array: {nums}")
