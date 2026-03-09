# Variable-Size Sliding Window

## Concept
Variable sliding windows dynamically adjust their size (both `left` and `right` pointers) based on a condition constraint. Typical operations include finding the longest or shortest subarray matching a condition.

## Blueprint
```python
def variable_sliding_window(arr, target):
    left = 0
    window_sum = 0
    max_len = 0
    
    for right in range(len(arr)):
        # 1. Add current element to window state
        window_sum += arr[right]
        
        # 2. Shrink window from left if condition is violated
        while window_sum > target and left <= right:
            window_sum -= arr[left]
            left += 1
            
        # 3. Update result if condition is perfectly met
        if window_sum == target:
            max_len = max(max_len, right - left + 1)
            
    return max_len
```

## When to use
- "Longest/Shortest subarray..."
- "...with sum exactly K"
- "...with at most/exactly K distinct characters"
