# Drill 1: Maximum Sum Subarray of Size K
# Type: Fixed Window

def maximum_sum_subarray(arr, k):
    if len(arr) < k:
        return 0
    
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
        
    return max_sum

if __name__ == "__main__":
    print(maximum_sum_subarray([2, 1, 5, 1, 3, 2], 3)) # Expected: 9 (5,1,3)
