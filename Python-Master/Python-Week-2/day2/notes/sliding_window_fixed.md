# Fixed-Size Sliding Window

## Concept
A fixed-size sliding window maintains a window of exactly size `k` as it moves across the array or string. Typical operations involve calculating the sum, finding maximums, or tracking frequencies within every contiguous block of size `k`.

## Blueprint
```python
def fixed_sliding_window(arr, k):
    # 1. Initialize variables for window state
    window_sum = 0
    max_sum = float('-inf')
    
    # 2. Setup initial window (first k elements)
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum
    
    # 3. Slide the window
    for i in range(k, len(arr)):
        # Add new element, remove old element
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum
```

## When to use
- "Subarray/Substring of size k"
- "Contiguous elements of length k"
