# Drill 5: Subarray Sum Equals K
# Prefix sum + Hash Map pattern

def subarray_sum(nums, k):
    count = 0
    current_sum = 0
    prefix_map = {0: 1} # base case: sum is exactly k
    
    for num in nums:
        current_sum += num
        # If current_sum - k exists in map, it means there is a subarray 
        # ending here that sums to k
        diff = current_sum - k
        count += prefix_map.get(diff, 0)
        
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        
    return count

if __name__ == "__main__":
    print(subarray_sum([1,1,1], 2)) # Expected: 2
