# Drill 8: Max Consecutive Ones III
# Type: Variable Window (Flips allowed)

def longest_ones(nums, k):
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
            
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
        
    return max_len

if __name__ == "__main__":
    print(longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2)) # Expected: 6
