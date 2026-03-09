# Window Optimization

## Concept
Instead of recalculating state variables from scratch or shrinking the window using a `while` loop (in cases like "Longest Substring without Repeating Characters"), we can optimize using a Hash Map pointing to the last seen indices.

## Optimization: Jump `left` Pointer
When finding the longest substring without repeating characters, rather than incrementing `left` by 1 iteratively when a duplicate is found, simply update `left` to `last_seen_index + 1`.

```python
def longest_unique_substring_optimized(s):
    char_index_map = {}
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char = s[right]
        # If character is found and is within the current window
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1  # Jump directly
            
        char_index_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len
```
