#pair programming

def kadane_algorithm(nums):
    # Initialize the current_sum with the first element
    current_sum = nums[0]
    
    # Start with the maximum sum also as the first element
    max_sum = nums[0]
    
    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        # Calculate the maximum sum ending at the current position
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update the global maximum sum found so far
        max_sum = max(max_sum, current_sum)
        
        # Debug output to understand the process
        print(f"Step {i}: current_sum = {current_sum}, max_sum = {max_sum}")
    
    return max_sum

# Example usage:
S = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = kadane_algorithm(S)
print("Maximum subarray sum is:", result)