# Drill 10: Longest Repeating Character Replacement
# Type: Variable Window (Max Frequency)

def character_replacement(s, k):
    count = {}
    res = 0
    left = 0
    maxf = 0
    
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)
        maxf = max(maxf, count[s[right]])
        
        while (right - left + 1) - maxf > k:
            count[s[left]] -= 1
            left += 1
            
        res = max(res, right - left + 1)
        
    return res

if __name__ == "__main__":
    print(character_replacement("AABABBA", 1)) # Expected: 4
