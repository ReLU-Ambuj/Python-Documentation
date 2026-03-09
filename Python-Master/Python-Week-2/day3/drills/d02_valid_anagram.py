# Drill 2: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

from collections import Counter

def is_anagram(s, t):
    if len(s) != len(t):
        return False
        
    # Space: O(1) since English alphabet is 26 chars max
    return Counter(s) == Counter(t)

    # Alternative frequency array approach:
    # count = [0] * 26
    # for i in range(len(s)):
    #     count[ord(s[i]) - ord('a')] += 1
    #     count[ord(t[i]) - ord('a')] -= 1
    # return all(c == 0 for c in count)

if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram")) # Expected: True
