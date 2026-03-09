# Drill 6: Find All Anagrams in a String
# Combination of Sliding Window and Hashing

from collections import Counter

def find_anagrams(s, p):
    res = []
    if len(p) > len(s): return res
    
    p_count = Counter(p)
    window_count = Counter(s[:len(p)-1])
    
    k = len(p)
    for r in range(k - 1, len(s)):
        # add right char
        window_count[s[r]] += 1
        
        # compare
        if window_count == p_count:
            res.append(r - k + 1)
            
        # remove left char
        left_char = s[r - k + 1]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
            
    return res

if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc")) # Expected: [0, 6]
