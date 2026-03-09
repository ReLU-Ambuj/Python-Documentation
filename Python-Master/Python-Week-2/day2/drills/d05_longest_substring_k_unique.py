# Drill 5: Longest Substring with K Unique Characters
# Type: Variable Window + Hash Map

def longest_substring_k_unique(s, k):
    left = 0
    char_count = {}
    max_len = -1
    
    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
            
        if len(char_count) == k:
            max_len = max(max_len, right - left + 1)
            
    return max_len

if __name__ == "__main__":
    print(longest_substring_k_unique("araaci", 2)) # Expected: 4 (araa)
