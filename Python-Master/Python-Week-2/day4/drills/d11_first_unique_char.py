# Drill 11: First Unique Character in a String

from collections import Counter

def first_uniq_char(s):
    count = Counter(s)
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
            
    return -1

if __name__ == "__main__":
    print(first_uniq_char("leetcode")) # Expected: 0
