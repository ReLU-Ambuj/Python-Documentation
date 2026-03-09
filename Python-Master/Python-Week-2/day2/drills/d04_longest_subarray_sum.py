# Drill 4: Longest Subarray with Sum K
# Type: Variable Window (Positive numbers only)

def longest_subarray_sum(arr, k):
    left = 0
    current_sum = 0
    max_len = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
            
        if current_sum == k:
            max_len = max(max_len, right - left + 1)
            
    return max_len

if __name__ == "__main__":
    print(longest_subarray_sum([4, 1, 1, 1, 2, 3, 5], 5)) # Expected: 4 (1,1,1,2)
